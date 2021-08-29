class GetUserCredentialsDatabaseMock
{
    query(sql, params) {
        return [{
            salt: "F^S%QljSfV",
            password: "15e24a16abfc4eef5faeb806e903f78b188c30e4984a03be4c243312f198d1229ae8759e98993464cf713e3683e891fb3f04fbda9cc40f20a07a58ff4bb00788",
            role: "admin"
        }]
    }

    end() { }
}

module.exports = { GetUserCredentialsDatabaseMock }
