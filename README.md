# Wizeline SRE Bootcamp Selection Challenge

Thank you for registering for the Wizeline Academy SRE Bootcamp, and welcome to the Selection Challenge!

In order to be accepted into the Wizeline Academy SRE Bootcamp, you must successfully complete the Selection Challenge. After registering, you will have until Tuesday, February 21, to complete it. The sooner you send it, the more chances you have of being selected.

We **do not** want you to think of this as a test or an exam, but instead, more like a project you have been assigned to complete. Communication is important, and we are here to help you if you get stuck or have any concerns - just open an issue in the source repository and our team of SRE experts will get back to you as soon as we can!
<br />
<br />

---

## Technical Challenge - Practical Applications

We would like you to fork **[this](https://github.com/wizelineacademy/sre-bootcamp)** repository. This will help us get an understanding of your operational skills, no matter which technology stack is used.


### Important notes:
- There is no specific time limitations, so you can go at your own pace.
- Once you have completed this part of the challenge, please fill out the **Google Form** that is mentioned at the bottom of this page with your forked repository.


### Overview

This repository contains an API skeleton where you can add the code, which is the auth_api folder. Use the language of your preference.

You need to complete a functionality in our API that provides a basic authentication.

The API has 2 missing endpoints. The first endpoint receives a username and password. When these parameters are correct it returns a JWT token; otherwise it should return a 403 HTTP error message.


You will have a read only database with these access:

|&nbsp;|&nbsp;|
| -------- | --------------------------                                                          |
| engine   | `mysql`                                                                             |
| user     | `secret`                                                                            |
| password | `jOdznoyH6swQB9sTGdLUeeSrtejWkcw`                                                   |
| endpoint | `http://sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com/` |
| port     | `3306`                                                                              |
| DB       | `bootcamp_tht`                                                                      |
<br />

In the database three valid users with their passwords are stored:

Table **`users`**
| username | password             | salt         | role   |
| -------- | -------------------- | ------------ | ------ |
| admin    | `encrypted-password` | `F^S%QljSfV` | admin  |
| noadmin  | `encrypted-password` | `KjvFUC#K*i` | editor |
| bob      | `encrypted-password` | `F^S%QljSfV` | viewer |
<br />

Passwords in plain text:
| username | password                |
| -------- | ----------------------- |
| admin    | `secret`                |
| noadmin  | `noPow3r`               |
| bob      | `thisIsNotAPasswordBob` |
<br />

Passwords have [appended the salt value](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/#Mitigating-Password-Attacks-with-Salt) and hashed with the [SHA512 Algorithm](https://en.wikipedia.org/wiki/SHA-2).
If the username and password combination is valid, you should return a JWT Token with the role in the payload of the token.
<br />

You should use this 256 bit secret to encrypt your token:
`my2w7wjd7yXF64FIADfJxNs1oupTGAuW`
```
curl -d "username=admin&password=secret" http://localhost:8000/login
{
  "data": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```
<br />

For the second endpoint you must use the generated token to access a restricted area:
```
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" localhost:8000/protected
{
  "data": "You are under protected data"
}
```
<br />

### Coding
  * Complete the following endpoints.
    - **`/login`**
    - **`/protected`**
  * Make sure your tests are passing.
  * Add missing tests. Feel free to add any additional tests that you think are valuable.
  * As mentioned above, you may work in the language of your choice. Please pick one from the list of available languages:
    - **[Python](auth_api/python)**
    - **[Java](auth_api/java)**
    - **[NodeJS](auth_api/node)**

### Docker
  * Dockerize the application located in **src**
  * Push it to a public image in DockerHub tagged as **`wize-<firstName>-<lastName>:latest`**
  * Application should run in port **`8000`**
<br />
<br />

---
## Don’t forget to fill out the Google Form with your forked repository!

Remember, you must send your forked repository by filling out the following **[Google Form](https://forms.gle/AoKSKKdPn8dPRbuv7)** you will have until Tuesday, February 21, to be considered for the Wizeline Academy SRE Bootcamp! (The sooner you send it, the more chances you have of being selected). 

Thanks for completing the challenge, we can’t wait to see you soon!

