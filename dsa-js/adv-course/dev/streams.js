import { Readable } from 'stream'

const peaks = [
    'Mt Bachelor',
    'Mt Washington',
    'Broken Top',
    'South Sister',
    'Middle Sister',
    'North Sister',
    'Mt Hood',
    'Mt Rainer',
    'Whistler',
]

class StreamFromArray extends Readable {
    constructor(array) {
        super({
            objectMode: true,
        })
        this.array = array
        this.index = 0
    }

    _read() {
        if (this.index <= this.array.length) {
            const chunk = {
                index: this.index,
                data: this.array[this.index],
            }
            this.push(chunk)
            this.index++
        } else {
            this.push(null)
        }
    }
}

const peakStream = new StreamFromArray(peaks)
peakStream.on('data', (chunk) => console.log(chunk))
peakStream.on('end', () => console.log('done!'))
