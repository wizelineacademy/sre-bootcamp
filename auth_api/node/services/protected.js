const jwt = require("jsonwebtoken")
const { SECRET } = require("../config/config")

export const protectFunction = (authorization) => {
  try {
    const data = jwt.verify(authorization, SECRET)
    if (!data) {
      return null
    }
    return "You are under protected data"
  } catch (error) {
    return null
  }
}
