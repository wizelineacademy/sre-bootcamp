const crypto = require("crypto")
const jwt = require("jsonwebtoken")
const database = require("../config/database")
const { SECRET } = require("../config/config")

export const loginFunction = async (username, password) => {
  try {
    const results = await database.query(
      "select * from users where username = ?",
      [username]
    )
    const user = results[0]
    const hash = crypto.createHash("sha512").update(password + user.salt).digest("hex")
    if (user.password !== hash) {
      return null
    }
    const token = jwt.sign({role: user.role}, SECRET)
    return token
  } catch (e) {
    console.log(e)
    return null
  }
}
