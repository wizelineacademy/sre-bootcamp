const crypto = require("crypto")
const jwt = require("jsonwebtoken")
const { SECRET } = require("../config/config")

class LoginService {
  constructor(database) {
    this.database = database
  }

  async login(username, password) {
    try {
      const results = await this.database.query(
        "select * from users where username = ?",
        [username]
      )
      const user = results[0]
      this.database.end()
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
}

module.exports = { LoginService }
