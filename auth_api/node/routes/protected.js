import { protectFunction } from '../services/protected';

export const protect = (req, res, next) => {
  let authorization = req.headers.authorization;
  let response = {
    "data": protectFunction(authorization)
  };
  res.send(response);
  next();
}
