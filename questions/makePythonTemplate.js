const { Client } = require('pg')
const {
    DynamoDBClient,
    ListTablesCommand,
} = require('@aws-sdk/client-dynamodb')
const fs = require('fs')
const handlebars = require('handlebars')

async function main() {
    try {
        const pyTemplateString = String(
            fs.readFileSync('templates/leet-python.handlebars')
        )
        console.log(pyTemplateString)
        const pyTemplateCompiled = handlebars.compile(pyTemplateString)

        const connectionString =
            'postgresql://postgres:Pass2020!@localhost:5432/leet'
        const client = new Client({ connectionString })
        await client.connect()
        await client.query('SELECT NOW()')

        const query = {
            name: 'get-questions',
            text: 'SELECT * FROM core.questions ORDER BY question_id',
        }

        const queryResult = await client.query(query)
        console.log(queryResult.rowCount)
        const questions = {}
        questions.question = []
        for (const row of queryResult.rows) {
            const questionJson = row.question_json
            const pythonSnippet = questionJson.codeSnippets.find(
                (p) => p.lang == 'Python3'
            )
            const question = {
                difficulty: row.difficulty,
                title: questionJson.title,
                content: questionJson.content,
                title_slug: row.title_slug,
                pythonSnippet: pythonSnippet.code + 'pass',
            }
            questions.question.push(question)
            // console.log(questionJson.codeSnippets)
            // console.log(pythonSnippet)
        }
        // console.log(questionJson)
        const renderedTemplate = pyTemplateCompiled(questions)
        // console.log(renderedTemplate)
        fs.writeFileSync('templates/leet-questions.py', renderedTemplate)
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
