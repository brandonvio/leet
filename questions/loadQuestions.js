const { Client } = require('pg')
const {
    DynamoDBClient,
    ListTablesCommand,
} = require('@aws-sdk/client-dynamodb')
const fs = require('fs')

async function main() {
    try {
        const connectionString =
            'postgresql://postgres:Pass2020!@localhost:5432/leet'

        const client = new Client({
            connectionString,
        })

        await client.connect()
        await client.query('SELECT NOW()')

        const questions = JSON.parse(fs.readFileSync('questions-all.json'))

        for (const question of questions.questions) {
            const detail = JSON.parse(
                fs.readFileSync(
                    `question-details/question-${question.frontendQuestionId}-${question.titleSlug}.json`
                )
            )
            const record = {
                questionId: detail.data.question.questionId,
                titleSlug: detail.data.question.titleSlug,
                difficulty: detail.data.question.difficulty,
            }
            console.log(record)
            const sql =
                'INSERT INTO core.questions(question_id, title_slug, difficulty, question_json) VALUES($1, $2, $3, $4) RETURNING *'
            const values = [
                record.questionId,
                record.titleSlug,
                record.difficulty,
                detail.data.question,
            ]
            try {
                const queryResult = await client.query(sql, values)
                console.log(queryResult.rowCount)
            } catch (error) {
                console.log(error)
            }
        }
    } catch (error) {
        console.log(error)
    } finally {
        return true
    }
}

const result = main()
result.then((p) => {
    console.log(p)
})
