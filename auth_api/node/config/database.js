const mysql = require("mysql")
const util = require("util")
const { DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT } = require("./config")

const db = mysql.createConnection({
  host: DB_HOST,
  user: DB_USER,
  password: DB_PASSWORD,
  database: DB_NAME,
  port: DB_PORT
})

db.query = util.promisify(db.query)

module.exports = db
