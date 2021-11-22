import express from 'express'
import axios from 'axios'
const app = express()
const port = 3000

app.get('/price/:symbol/:tracker', async (req, res) => {
    const symbol = req.params.symbol.toUpperCase()
    const response = await axios.get(
        `https://min-api.cryptocompare.com/data/price?fsym=${symbol}&tsyms=USD,JPY,EUR`
    )
    const returnPayload = {
        tracker: req.params.tracker,
        symbol: req.params.symbol,
        timestamp: new Date(),
        cryptocompare: response.data,
    }
    console.log(returnPayload)
    res.send(returnPayload)
})

app.listen(port, () => {
    console.log(`Example app listening at http://127.0.0.1:${port}`)
})
