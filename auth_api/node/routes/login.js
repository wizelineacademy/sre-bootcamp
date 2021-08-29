import { LoginService } from '../services/login';
const database = require("../config/database")
const loginService = new LoginService(database)

export const login = async (req, res, next) => {
  let username = req.body.username;
  let password = req.body.password;
  const token = await loginService.login(username, password);
  if (!token) {
    res.status(401).send({"message": "UNAUTHORIZED"})
  } else {
    res.status(200).send({data: token})
    next();
  }
}
