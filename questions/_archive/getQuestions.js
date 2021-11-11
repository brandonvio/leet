import fetch from 'node-fetch';
import * as fs from 'fs';

const titleSlug = 'two-sum'

const result = await fetch("https://leetcode.com/graphql", {
    "headers": {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"95\", \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "n4vVR50dXMTH51EMydbdT6cd5LcCS7KPLrpEIRrQf1EKpB8HcC3BBhckV0aZWZ25",
        "x-newrelic-id": "UAQDVFVRGwEAXVlbBAg=",
        "cookie": "gr_user_id=7caa4e43-eb13-4a69-9199-1f7cf1408a9a; csrftoken=n4vVR50dXMTH51EMydbdT6cd5LcCS7KPLrpEIRrQf1EKpB8HcC3BBhckV0aZWZ25; 87b5a3c3f1a55520_gr_last_sent_cs1=brandonvio; _gcl_au=1.1.251687955.1635371855; intercom-id-pq9rak4o=40b24bcb-35d4-44c6-899b-e654c017b06e; _ga_DKXQ03QCVK=GS1.1.1635371854.1.1.1635371870.44; _ga=GA1.2.844351375.1635371827; __stripe_mid=66bf1ab6-d357-4e6a-a334-6ffde4af61488403ee; _gid=GA1.2.1021860214.1636400560; NEW_PROBLEMLIST_PAGE=1; __atuvc=32%7C43%2C0%7C44%2C4%7C45; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjcwMTI1MyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzkzMGU2YWQ3M2UyMmEwN2Y5MTJlZDNkNGQ0NmFjOWY4ZjdiMmMzNSIsImlkIjoyNzAxMjUzLCJlbWFpbCI6ImJyYW5kb252aW9Ab3V0bG9vay5jb20iLCJ1c2VybmFtZSI6ImJyYW5kb252aW8iLCJ1c2VyX3NsdWciOiJicmFuZG9udmlvIiwiYXZhdGFyIjoiaHR0cHM6Ly93d3cuZ3JhdmF0YXIuY29tL2F2YXRhci85Nzc3ZWQ5ODRlNWU3N2QyNDEwMDEwZWVlYzViZGUxNS5wbmc_cz0yMDAiLCJyZWZyZXNoZWRfYXQiOjE2MzY3NTQ3NTYsImlwIjoiNjcuMjA0LjE1My44MiIsImlkZW50aXR5IjoiM2E5YjNkNjE5NGEzYmYzNzIxZDNmYTJlZmNjNTIyZjEiLCJzZXNzaW9uX2lkIjoxNDA2NzkzNiwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.8T-JvZZ7qJV5BUteMBYw2ysJtqQDDIu4RkurZpuCxWA; 87b5a3c3f1a55520_gr_session_id=46ed20e3-9050-4b74-afd0-2bce11f248d0; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=46ed20e3-9050-4b74-afd0-2bce11f248d0; 87b5a3c3f1a55520_gr_session_id_46ed20e3-9050-4b74-afd0-2bce11f248d0=true; 87b5a3c3f1a55520_gr_cs1=brandonvio; c_a_u=\"YnJhbmRvbnZpbw==:1mlz1A:Gqnh6LgWBq1Tcz_260kOdOdd_Cs\"; _gat=1",
        "Referer": "https://leetcode.com/problems/lru-cache/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    "body": `{\"operationName\":\"questionData\",\"variables\":{\"titleSlug\":\"${titleSlug}\"},\"query\":\"query questionData($titleSlug: String!) {\\n  question(titleSlug: $titleSlug) {\\n    questionId\\n    questionFrontendId\\n    boundTopicId\\n    title\\n    titleSlug\\n    content\\n    translatedTitle\\n    translatedContent\\n    isPaidOnly\\n    difficulty\\n    likes\\n    dislikes\\n    isLiked\\n    similarQuestions\\n    exampleTestcases\\n    contributors {\\n      username\\n      profileUrl\\n      avatarUrl\\n      __typename\\n    }\\n    topicTags {\\n      name\\n      slug\\n      translatedName\\n      __typename\\n    }\\n    companyTagStats\\n    codeSnippets {\\n      lang\\n      langSlug\\n      code\\n      __typename\\n    }\\n    stats\\n    hints\\n    solution {\\n      id\\n      canSeeDetail\\n      paidOnly\\n      hasVideoSolution\\n      paidOnlyVideo\\n      __typename\\n    }\\n    status\\n    sampleTestCase\\n    metaData\\n    judgerAvailable\\n    judgeType\\n    mysqlSchemas\\n    enableRunCode\\n    enableTestMode\\n    enableDebugger\\n    envInfo\\n    libraryUrl\\n    adminUrl\\n    challengeQuestion {\\n      id\\n      date\\n      incompleteChallengeCount\\n      streakCount\\n      type\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\"}`,
    "method": "POST"
});

const _data = await result.json()
console.log(JSON.stringify(_data, null, 4))
fs.writeFileSync(`question-${titleSlug}.json`, JSON.stringify(_data, null, 4));