import fetch from 'node-fetch';
import * as fs from 'fs';

async function getList(listId, name) {
    const result = await fetch("https://leetcode.com/graphql/", {
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
            "cookie": "gr_user_id=7caa4e43-eb13-4a69-9199-1f7cf1408a9a; csrftoken=n4vVR50dXMTH51EMydbdT6cd5LcCS7KPLrpEIRrQf1EKpB8HcC3BBhckV0aZWZ25; 87b5a3c3f1a55520_gr_last_sent_cs1=brandonvio; _gcl_au=1.1.251687955.1635371855; intercom-id-pq9rak4o=40b24bcb-35d4-44c6-899b-e654c017b06e; _ga_DKXQ03QCVK=GS1.1.1635371854.1.1.1635371870.44; _ga=GA1.2.844351375.1635371827; __stripe_mid=66bf1ab6-d357-4e6a-a334-6ffde4af61488403ee; NEW_PROBLEMLIST_PAGE=1; __atuvc=32%7C43%2C0%7C44%2C4%7C45; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjcwMTI1MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzkzMGU2YWQ3M2UyMmEwN2Y5MTJlZDNkNGQ0NmFjOWY4ZjdiMmMzNSIsImlkIjoyNzAxMjUzLCJlbWFpbCI6ImJyYW5kb252aW9Ab3V0bG9vay5jb20iLCJ1c2VybmFtZSI6ImJyYW5kb252aW8iLCJ1c2VyX3NsdWciOiJicmFuZG9udmlvIiwiYXZhdGFyIjoiaHR0cHM6Ly93d3cuZ3JhdmF0YXIuY29tL2F2YXRhci85Nzc3ZWQ5ODRlNWU3N2QyNDEwMDEwZWVlYzViZGUxNS5wbmc_cz0yMDAiLCJyZWZyZXNoZWRfYXQiOjE2MzY5NTYyMDksImlwIjoiNjcuMjA0LjE1My44MiIsImlkZW50aXR5IjoiM2E5YjNkNjE5NGEzYmYzNzIxZDNmYTJlZmNjNTIyZjEiLCJzZXNzaW9uX2lkIjoxNDA2NzkzNiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.kM4106SW2Ki2pZxSjYWPoPGPI0RbD91bwx-fvCOIEwY; _gid=GA1.2.976869266.1636956209; c_a_u=\"YnJhbmRvbnZpbw==:1mn5jC:p3ivs9RpeB4NVoR_zGtzjZDFB_8\"; 87b5a3c3f1a55520_gr_session_id=49839c40-8949-4b0f-a839-b29ae62e9011; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=49839c40-8949-4b0f-a839-b29ae62e9011; 87b5a3c3f1a55520_gr_cs1=brandonvio; 87b5a3c3f1a55520_gr_session_id_49839c40-8949-4b0f-a839-b29ae62e9011=true",
            "Referer": `https://leetcode.com/problem-list/${listId}/?sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D`,
            "Referrer-Policy": "strict-origin-when-cross-origin"
        },
        "body": `{\"query\":\"\\n    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {\\n  problemsetQuestionList: questionList(\\n    categorySlug: $categorySlug\\n    limit: $limit\\n    skip: $skip\\n    filters: $filters\\n  ) {\\n    total: totalNum\\n    questions: data {\\n      acRate\\n      difficulty\\n      freqBar\\n      frontendQuestionId: questionFrontendId\\n      isFavor\\n      paidOnly: isPaidOnly\\n      status\\n      title\\n      titleSlug\\n      topicTags {\\n        name\\n        id\\n        slug\\n      }\\n      hasSolution\\n      hasVideoSolution\\n    }\\n  }\\n}\\n    \",\"variables\":{\"categorySlug\":\"\",\"skip\":0,\"limit\":50,\"filters\":{\"listId\":\"${listId}\"}},\"operationName\":\"problemsetQuestionList\"}`,
        "method": "POST"
    });
    const _data = await result.json()

    fs.writeFileSync(`questions-${name}-${listId}.json`, JSON.stringify(_data.data, null, 4));

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

let _allQuestions = []

for (let list of listIds) {
    let _data = await getList(list.listId, list.name)
    _allQuestions = _allQuestions.concat(..._data)
    console.log(list.name, _allQuestions.length)
}

fs.writeFileSync(`questions-all.json`, JSON.stringify(_allQuestions, null, 4));
