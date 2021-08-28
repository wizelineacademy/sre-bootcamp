import { protectFunction } from '../services/protected';

export const protect = (req, res, next) => {
  let bearerToken = req.headers.authorization.split(" ");
  if (!(bearerToken.length === 2 && bearerToken[0] === "Bearer")) {
    res.status(403).send({data: "Forbidden Client"});
    return;
  }
  const protectedData = protectFunction(bearerToken[1])
  if (protectedData) {
    let response = {
      "data": protectFunction(bearerToken[1])
    };
    res.send(response);
    next();
  } else {
    res.status(500).send({data: "Internal Server Error"});
  }
}
