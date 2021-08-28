import { loginFunction } from '../services/login';

export const login = async (req, res, next) => {
  let username = req.body.username;
  let password = req.body.password;

  const token = await loginFunction(username, password);
  if (!token) {
    res.status(401).send({"message": "UNAUTHORIZED"})
  } else {
    res.status(200).send({data: token})
    next();
  }
}
