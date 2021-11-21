const { promisify } = require('util')
const fs = require('fs')

const writeFile = promisify(fs.writeFile)

async function start() {
    return Promise.resolve()
    await writeFile('test.txt', 'testing...')
}

start()
    .then(console.log('done!'))
    .catch((error) => {
        console.log(error)
    })
