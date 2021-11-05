import fetch from 'node-fetch';
import * as fs from 'fs';

async function getList(listId, name){
    const _promise = await fetch("https://leetcode.com/graphql/", {
    "headers": {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "",
        "content-type": "application/json",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "n4vVR50dXMTH51EMydbdT6cd5LcCS7KPLrpEIRrQf1EKpB8HcC3BBhckV0aZWZ25",
        "cookie": "_gid=GA1.2.1173187878.1635371827; gr_user_id=7caa4e43-eb13-4a69-9199-1f7cf1408a9a; csrftoken=n4vVR50dXMTH51EMydbdT6cd5LcCS7KPLrpEIRrQf1EKpB8HcC3BBhckV0aZWZ25; messages=\"e7a24f1e88a44b49b2e44a2ca25f591d5a82b80c$[[\\\"__json_message\\\"\\0540\\05425\\054\\\"Successfully signed in as brandonvio.\\\"]]\"; 87b5a3c3f1a55520_gr_last_sent_cs1=brandonvio; _gcl_au=1.1.251687955.1635371855; intercom-id-pq9rak4o=40b24bcb-35d4-44c6-899b-e654c017b06e; intercom-session-pq9rak4o=; _ga_DKXQ03QCVK=GS1.1.1635371854.1.1.1635371870.44; _ga=GA1.2.844351375.1635371827; __stripe_mid=66bf1ab6-d357-4e6a-a334-6ffde4af61488403ee; NEW_PROBLEMLIST_PAGE=1; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjcwMTI1MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzkzMGU2YWQ3M2UyMmEwN2Y5MTJlZDNkNGQ0NmFjOWY4ZjdiMmMzNSIsImlkIjoyNzAxMjUzLCJlbWFpbCI6ImJyYW5kb252aW9Ab3V0bG9vay5jb20iLCJ1c2VybmFtZSI6ImJyYW5kb252aW8iLCJ1c2VyX3NsdWciOiJicmFuZG9udmlvIiwiYXZhdGFyIjoiaHR0cHM6Ly93d3cuZ3JhdmF0YXIuY29tL2F2YXRhci85Nzc3ZWQ5ODRlNWU3N2QyNDEwMDEwZWVlYzViZGUxNS5wbmc_cz0yMDAiLCJyZWZyZXNoZWRfYXQiOjE2MzU1NDY0NDYsImlwIjoiNjcuMjA0LjE1My44MiIsImlkZW50aXR5IjoiM2E5YjNkNjE5NGEzYmYzNzIxZDNmYTJlZmNjNTIyZjEiLCJzZXNzaW9uX2lkIjoxNDA2NzkzNiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.-yRNzfDbBegVhp2jTsAO-ir1BZO6h1nrkK9eUJXhMFU; __atuvc=32%7C43; c_a_u=\"YnJhbmRvbnZpbw==:1mgwqw:0Yq3XSiaV2QqD7Mm1dSWix7FTG8\"; 87b5a3c3f1a55520_gr_session_id=00a8557f-17d2-4677-a7e9-fa6c4fc14122; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=00a8557f-17d2-4677-a7e9-fa6c4fc14122; 87b5a3c3f1a55520_gr_session_id_00a8557f-17d2-4677-a7e9-fa6c4fc14122=true; 87b5a3c3f1a55520_gr_cs1=brandonvio",
        "Referer": "https://leetcode.com/problem-list/7p59281/?sorting=W3sic29ydE9yZGVyIjoiQVNDRU5ESU5HIiwib3JkZXJCeSI6IkZST05URU5EX0lEIn1d",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": `{\"query\":\"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    \",\"variables\":{\"categorySlug\":\"\",\"skip\":0,\"limit\":100,\"filters\":{\"orderBy\":\"FRONTEND_ID\",\"sortOrder\":\"ASCENDING\",\"listId\":\"${listId}\"}},\"operationName\":\"problemsetQuestionList\"}`,
    "method": "POST"
    });
    const _data = await _promise.json()
    const _questions = _data.data.problemsetQuestionList.questions
    _questions.forEach(p => {
        p["listName"] = name
    })
    console.log(listId, name, _data.data.problemsetQuestionList.questions.length)
    return _data.data.problemsetQuestionList.questions
}

// Google: 7p55wqm
// Facebook: 7p59281
// Amazon: p5x763
// Microsoft: 55vr69d7
const listIds = [
    {
        "name" : "goog",
        "listId" : "7p55wqm"
    },
    {
        "name" : "fb",
        "listId" : "7p59281"
     },
     {
        "name" : "amzn",
        "listId" : "p5x763"
     },
     {
        "name" : "msft",
        "listId" : "55vr69d7"
     },
]
let _allQuestions = []

for (let list of listIds){
    let _data = await getList(list.listId, list.name)
    _allQuestions = _allQuestions.concat(..._data)    
}

console.log(_allQuestions.length)

_allQuestions.sort((a, b) => (Number.parseInt(a.frontendQuestionId) > Number.parseInt(b.frontendQuestionId)) ? 1 : -1)

const _questions = {}
_allQuestions.forEach(p => {
    if (p.frontendQuestionId in _questions){
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
        if (_tagsCounter[p.name] == undefined){
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
console.log(_allQuestions[0])

const _tags = Object.entries(_tagsCounter).sort((a, b) => b[1] - a[1])

let _tagsContent = ""
for (let p of _tags) {
    let _line = `${p[0]}: ${p[1]}`
    _tagsContent += _line + "\n"
    console.log(_line)
}
fs.writeFileSync("leet-questions-tags.txt", _tagsContent)