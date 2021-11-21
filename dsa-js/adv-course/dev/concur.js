import { logUpdateStderr } from 'log-update'
import { promisify } from 'util'
import * as fs from 'fs'
var toX = () => 'X'
const writeFile = promisify(fs.writeFile)
const unlink = promisify(fs.unlink)
const readdir = promisify(fs.readdir)
const delay = (seconds) => {
    return new Promise((resolves) => {
        console.log(`Delaying for ${seconds}...`)
        setTimeout(resolves, seconds * 1000)
    })
}

const tasks = []
for (let i = 0; i < 50; i++) {
    tasks.push(delay(Math.floor(Math.random() * 20)))
}

class PromiseQueue {
    constructor(promises = [], concurrentCount = 1) {
        this.concurrentCount = concurrentCount
        this.total = promises.length
        this.todo = promises
        this.running = []
        this.complete = []
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
}

var delayQueue = new PromiseQueue(tasks, 2)
delayQueue.run()

// Promise.all([
//   writeFile('readme.txt', 'Hello World!'),
//   writeFile('readme.md', 'Hello World!'),
//   delay(3),
//   writeFile('readme.json', JSON.stringify({ "hello": "Hello World!" })),
// ]).then(() => readdir(__dirname))
//   .then(console.log)

// const start = async() => {
//   console.log("start...")
//   await writeFile("test.txt", "testing...")
//   await delay(3)
//   console.log("done waiting 3...")
//   await delay(2)
//   console.log("done waiting 2...")
//   await delay(1)
//   console.log("done waiting 1...")
//   // throw new Error("this thing failed")
//   return Promise.resolve()
// }

// start().then(() => {
//   console.log("finished!")
// }).catch(error => {
//   console.log(error)
// })
