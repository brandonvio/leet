import * as fs from 'fs';
import questions from "./questions-all.json"


const listIds = [
    {
        "name": "goog",
        "listId": "7p55wqm"
    },
    {
        "name": "fb",
        "listId": "7p59281"
    },
    {
        "name": "amzn",
        "listId": "7p5x763"
    },
    {
        "name": "msft",
        "listId": "55vr69d7"
    },
]
const _questionList = questions.questions
_questionList.sort((a, b) => (Number.parseInt(a.frontendQuestionId) > Number.parseInt(b.frontendQuestionId)) ? 1 : -1)


const _questions = {}
_questionList.forEach(p => {
    if (p.frontendQuestionId in _questions) {
        _questions[p.frontendQuestionId].listName += "|" + p.listName
    } else {
        _questions[p.frontendQuestionId] = p
    }
});

console.log(_questions)

let _fileContent = "id,title,difficulty,freq,listName,tags" + "\n"

const _tagsCounter = {}

for (const [key, p] of Object.entries(_questions)) {
    let tags = "|"
    p.topicTags.forEach(p => {
        tags += p.name + "|"
        if (_tagsCounter[p.name] == undefined) {
            _tagsCounter[p.name] = 1
        } else {
            _tagsCounter[p.name] += 1
        }
    })
    let _line = `${p.frontendQuestionId},"=HYPERLINK(""https://leetcode.com/problems/${p.titleSlug}/"",""${p.title}"")",${p.difficulty},${p.freqBar},${p.listName},${tags}`
    _fileContent += _line + "\n"
    console.log(_line)
}

fs.writeFileSync("leet-questions.csv", _fileContent)
console.log(questions[0])

const _tags = Object.entries(_tagsCounter).sort((a, b) => b[1] - a[1])

let _tagsContent = ""
for (let p of _tags) {
    let _line = `${p[0]}: ${p[1]}`
    _tagsContent += _line + "\n"
    console.log(_line)
}
fs.writeFileSync("leet-questions-tags.txt", _tagsContent)

