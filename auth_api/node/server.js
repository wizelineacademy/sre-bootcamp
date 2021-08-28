const express = require('express');
const app = express();
const bodyParser = require('body-parser');

import * as routes from './routes';

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
routes.init(app);

export default app;
