var fs = require('fs')
var { promisify } = require('util')

var writeFile = promisify(fs.writeFile)

// writeFile('sample.txt', 'this is a file!')
//     .then(() => console.log('file created!'))
//     .catch((error) => console.log('error!'))

fs.writeFile('sample.txt', 'this is a file via writefile!', (error) => {
    console.log(error)
    console.log('file created via writefile!')
})
