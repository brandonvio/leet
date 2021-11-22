import { logUpdateStderr } from 'log-update'
import axios from 'axios'

var toX = () => 'X'
const getPrice = (symbol, tracker) => {
    return axios.get(`http://localhost:3000/price/${symbol}/${tracker}`)
}

const delay = (seconds) => {
    return new Promise((resolves) => {
        console.log(`Delaying for ${seconds}...`)
        setTimeout(resolves, seconds * 1000)
    })
}

const tasks = [
    delay(10),
    getPrice('btc', 1),
    getPrice('eth', 2),
    getPrice('ada', 3),
    getPrice('xrp', 4),
    getPrice('btc', 5),
    getPrice('eth', 6),
    getPrice('ada', 7),
    getPrice('xrp', 8),
    getPrice('btc', 9),
    getPrice('eth', 10),
    getPrice('ada', 11),
    getPrice('xrp', 12),
    getPrice('btc', 13),
    getPrice('eth', 14),
    getPrice('ada', 15),
    getPrice('xrp', 16),
    getPrice('btc', 17),
    getPrice('eth', 18),
    getPrice('ada', 19),
    getPrice('xrp', 20),
    getPrice('btc', 21),
    getPrice('eth', 22),
    getPrice('ada', 23),
    getPrice('xrp', 24),
]

class PromiseQueue {
    constructor(promises = [], concurrentCount = 2) {
        this.concurrentCount = concurrentCount
        this.total = promises.length
        this.todo = promises
        this.running = []
        this.complete = []
    }

    run() {
        while (this.runAnother()) {
            const promise = this.todo.shift()
            promise.then((response) => {
                console.log(response.data)
                this.complete.push(this.running.shift())
                this.graphTasks()
                this.run()
            })
            this.running.push(promise)
            this.graphTasks()
        }
    }

    runAnother() {
        return this.running.length < this.concurrentCount && this.todo.length
    }

    graphTasks() {
        var { todo, running, complete } = this
        logUpdateStderr(`
todo: [${todo.map(toX)}]
running: [${running.map(toX)}]
complete: [${complete.map(toX)}]
        `)
    }
}

var delayQueue = new PromiseQueue(tasks, 2)
delayQueue.run()
