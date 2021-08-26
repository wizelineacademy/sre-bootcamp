import mysql.connector as mysqlc
import hashlib
import jwt

db_config = {
    'user': 'secret',
    'password': 'noPow3r',
    'host': 'bootcamp-tht.sre.wize.mx',
    'port': 3306,
    'database': 'bootcamp_tht',
}

cnx = mysqlc.connect(**db_config)

# These functions need to be implemented
class Token:


    def verify_credentials(self, username, passw):
        pass_salt_qry = f"SELECT password, salt, role FROM users WHERE username = '{ username }'"
        cursor = cnx.cursor()
        cursor.execute(pass_salt_qry)

        db_data = {
            'db_pass': '',
            'role': '',
        }

        hashed_pass = ""

        for (password, salt, role) in cursor:
            pass_salt = passw + salt
            hashed_pass = hashlib.sha512(pass_salt.encode()).hexdigest()
            db_data['db_pass'] = password
            db_data['role'] = '' + role
        
        if hashed_pass != db_data['db_pass']:
            return False, {}

        return True, db_data

    def generate_token(self, username, password):
        # First verify the credentials
        success, data = self.verify_credentials(username, password)
        if not success:
            return success
        # print({"role": data["role"]})
        token = jwt.encode({"role": data["role"]}, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithm="HS256")
        
        return token


class Restricted:

    def access_data(self, authorization):
        # Check Token
        token = str.replace(str(authorization), 'Bearer ', '')
        payload = jwt.decode(token, "my2w7wjd7yXF64FIADfJxNs1oupTGAuW", algorithms=["HS256"])
        
        if 'role' not in payload:
            return False

        return "You are under protected data"
