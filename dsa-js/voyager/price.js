import axios from 'axios'

const run = async () => {
    const response = await axios.get(
        'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
    )
    console.log(response.data)
}

run()
    .then(() => {
        console.log('done...')
    })
    .catch((error) => {
        console.log(error)
    })
