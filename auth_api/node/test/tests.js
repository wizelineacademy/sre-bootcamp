import chai from 'chai';
import { LoginService } from '../services/login'
import { protectFunction } from '../services/protected'
import { GetUserCredentialsDatabaseMock } from "./mocks/database/GetUserCredentialsDatabaseMock"

const expect = chai.expect;

describe('loginService', function () {
  it('Test login', async function () {
    const loginService = new LoginService(new GetUserCredentialsDatabaseMock)
    const token = await loginService.login("admin", "secret")
    expect(token).to.not.be.null;
    const data = token.split(".")[0]
    expect(data).to.equal("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
  })

  it('Test login: invalid password should return null', async function () {
    const loginService = new LoginService(new GetUserCredentialsDatabaseMock)
    const token = await loginService.login("admin", "wrongpassword")
    expect(token).to.equal(null)
  })
});

describe('protectFunction()', function () {
  it('Test protected', function () {
    expect("You are under protected data").to.be.equal(protectFunction("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI"));
  });

  it('Test protected: invalid credentials should return null', function () {
    expect(protectFunction("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBG")).to.be.null;
  });
});
