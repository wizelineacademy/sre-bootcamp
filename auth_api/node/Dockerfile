FROM node:9-alpine

WORKDIR /app

COPY package.json /app

ARG NODE_ENV

RUN if [ "$NODE_ENV" = "development" ]; \
        then npm install; \
        else npm install --only=production; \
    fi

COPY . /app

ENV PORT 8000

EXPOSE $PORT

CMD ["node", "index.js"]

# App must run on port 8000
# Add your instructions to dockerize the application
