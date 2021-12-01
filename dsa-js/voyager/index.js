import WebSocket from 'ws'
import { logUpdateStderr } from 'log-update'
import { PriceDb } from './price-db.js'

const API_KEY = process.env.CRYPTOCOMPARE_API_KEY

class PriceWebSocket {
    constructor() {
        this.prices = {}
        this.priceDb = new PriceDb()
        this.priceDb.connect()
        this.updateStatus = this.updateStatus.bind(this)
        const _updateStatus = this.updateStatus

        const ws = new WebSocket(
            `wss://streamer.cryptocompare.com/v2?api_key=${API_KEY}`,
            {
                perMessageDeflate: false,
            }
        )

        // const subs = ['2~Coinbase~BTC~USD', '2~Binance~BTC~USDT']
        const subs = [
            '2~Kraken~BTC~USD',
            '2~Gemini~BTC~USD',
            '2~Coinbase~BTC~USD',
            '2~Binance~BTC~USDT',
            '2~Kraken~ETH~USD',
            '2~Gemini~ETH~USD',
            '2~Coinbase~ETH~USD',
            '2~Binance~ETH~USDT',
        ]

        ws.on('open', function open() {
            const sub = {
                action: 'SubAdd',
                subs: subs,
            }
            ws.send(JSON.stringify(sub))
        })

        ws.on('message', async function message(data) {
            // console.log('received: %s', JSON.parse(data))
            await _updateStatus(JSON.parse(data))
        })

        ws.on('error', (error) => {
            console.log(error)
        })
    }

    async updateStatus(msg) {
        if (msg.TYPE === '2') {
            const priceKey =
                msg.MARKET + '_' + msg.FROMSYMBOL + '_' + msg.TOSYMBOL
            if (msg.PRICE) {
                await this.priceDb.savePrice(msg)
                this.prices[priceKey] = msg.PRICE
                let logMsg = ''
                for (const key in this.prices) {
                    logMsg += `${key}: ${this.prices[key]}\n`
                }
                logUpdateStderr(logMsg)
            }
        }
    }
}

new PriceWebSocket()
