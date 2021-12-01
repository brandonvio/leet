// https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&e=Coinbase
// https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&e=Bitfinex
// https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD&e=Bittrex

const PRICE_ENDPOINT = 'https://min-api.cryptocompare.com/data/pricemultifull?'
/**
 * @param {string}
 * @param {string}
 * @return {number}
 */
async function voyagerPrice(coinSymbol = 'BTC', currencySymbol = 'USD') {
    const exchangeApi = new ExchangeApi()
    const priceCalculator = new PriceCalculator(exchangeApi)
    const price = await priceCalculator.getPrice(coinSymbol, currencySymbol)
    return price
}

class PriceCalculator {
    constructor(exchangApi, acceptableVariance) {
        this.exchangApi = exchangApi
        this.exchanges = ['Coinbase', 'Bitfinex', 'Bittrex'] // Maybe this should be a call to another service
        this.acceptableVariance = acceptableVariance
    }

    async getPrice(symbol, toSymbol) {
        const exchangePrices = await this.getExchangePrices(symbol, toSymbol)
        return this.calculateVoyagerPrice(exchangePrices)
    }

    async getExchangePrices(symbol, toSymbol) {
        const exchangePrices = []
        for (const exchange in this.exchanges) {
            try {
                const price = this.exchangApi.getPrice(
                    exchange,
                    symbol,
                    toSymbol
                )
                exchangePrices.push({
                    exchange,
                    price,
                })
            } catch (error) {
                // sturctured log
                console.log({
                    eventType: 'error',
                    errorMesage: error.message,
                })
            }
        }
        return exchangePrices
    }

    getAveragePrice(exchangePrices) {
        const totalPrice = exchangePrices.reduce((a, b) => a.price + b.price)
        const averagePrice = totalPrice / exchangePrices.length
        return averagePrice
    }

    calculateVoyagerPrice(exchangePrices) {
        if (!exchangePrices.length) {
            throw new Error('no prices')
        }
        const averagePrice = this.getAveragePrice(exchangePrices)
        for (let i = 0; i < exchangePrices.length; i++) {
            const priceDiff = Math.abs(averagePrice - exchangePrice)
            const percentageDiff = priceDiff / averagePrice
            if (
                percentageDiff > acceptableVariance &&
                exchangePrices.length > 1
            ) {
                exchangePrices.splice(i, 1)
                this.calculateVoyagerPrice(exchangePrices)
            }
        }
        return averagePrice
    }
}

class ExchangeApi {
    async getPrice(exchange, fromSymbol, toSymbol) {
        try {
            const endpoint =
                PRICE_ENDPOINT +
                `fsyms=${fromSymbol}&tsyms=${fromSymbol}&e=${exchange}`
            const result = await axios.get(endpoint)
            return result.data.RAW[fromSymbol][toSymbol].PRICE
        } catch {
            // log error
            // raise
        }
    }
}

// A class just to call the API endpoints. Basiacally think wrapper around axios. No business logic. ExchangeApi
// A class for the bussiness logic that calls...  PriceCalculator
// A dictionary or an array of Exchanges
//      look through this array and get the price for the symbol for each exchange
//          if exchange throws an error... peform calculation with the other echanges....
//      store that in a dictionary or array of objects
// Once I have all the prices from exchange... perfrom the price algorithm calculation
//      get the average... add up all the numbers.. divide my the number of exchanges....
// Compare the average to each exchange price... if the average is a give % variance from the exchange... recalcuate the price minus that exchange...
// return that result to the user
