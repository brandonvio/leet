import * as fs from 'fs'

const readStream = fs.createReadStream('./powder-day.mp4')

readStream.on('data', (chunk) => {
    console.log('reading a little chunk:\n', chunk)
})

readStream.on('end', () => {
    console.log('done...')
})

readStream.on('error', (error) => {
    console.log('an error has occurred', error)
})

process.stdin.on('data', (chunk) => {
    const text = chunk.toString().trim()
    console.log('chunk:', text)
})
