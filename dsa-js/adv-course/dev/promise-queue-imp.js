import { logUpdateStderr } from 'log-update'

var toX = () => 'X'
const delay = (seconds) => {
    return new Promise((resolves) => {
        console.log(`Delaying for ${seconds}...`)
        setTimeout(resolves, seconds * 1000)
    })
}

const tasks = []
for (let i = 0; i < 25; i++) {
    tasks.push(delay(i))
}

class PromiseQueue {
    constructor(promises = [], concurrentCount = 1) {
        this.concurrentCount = concurrentCount
        this.total = promises.length
        this.todo = promises
        this.running = []
        this.complete = []
    }

    run() {
        while (this.runAnother()) {
            const promise = this.todo.shift()
            promise.then(() => {
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

var delayQueue = new PromiseQueue(tasks, 5)
delayQueue.run()
