# Implementation Checklist
- [x] API Code
- [x] Services Code
- [x] Unit-tests
- [x] Dockerfile
- [x] It Compiles
- [x] It runs

# Api Services
- Receives a valid username and password and returns a JWT.
- Returns protected data with a valid token, otherwise returns unauthenticated.

# Set up
1. copy .env.example into .env and set up the project settings database connection credentail and jwt secrt
    ```cp .env.example .env```
2. run development environment
    ```docker-compose -f docker-compose.yml -f docker-compose.dev.yml up```
3. run production environment
    ```docker-compose -f docker-compose.yml -f docker-compose.prod.yml up```

Use ```--build``` only when you have made changes to the instance, otherwise it can be omitted.
