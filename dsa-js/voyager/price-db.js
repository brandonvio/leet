import pg from 'pg'

export class PriceDb {
    constructor() {
        const connectionString =
            'postgresql://postgres:Pass2020!@localhost:5432/leet'

        this.client = new pg.Client({
            connectionString,
        })
    }

    async connect() {
        await this.client.connect()
        const result = await this.client.query('SELECT NOW()')
        return JSON.stringify(result.rows[0])
    }

    async savePrice(record) {
        const sql =
            'INSERT INTO core.prices(symbol, to_symbol, exchange, price_time, price_value, price_json) VALUES($1, $2, $3, $4, $5, $6) RETURNING *'
        const values = [
            record.FROMSYMBOL,
            record.TOSYMBOL,
            record.MARKET,
            new Date(record.LASTUPDATE),
            record.PRICE,
            record,
        ]
        try {
            await this.client.query(sql, values)
        } catch (error) {
            console.log(error)
        }
    }
}

// const db = new PriceDb()
// db.connect()
//     .then((data) => {
//         console.log(`connected! ${data}`)
//     })
//     .catch((error) => {
//         console.log(error)
//     })
