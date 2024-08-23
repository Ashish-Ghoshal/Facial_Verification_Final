# auth_steps/trad_auth_step.py

import hashlib

class TraditionalAuthFinal:
    def __init__(self, user_db=None):
        self.user_db_final = user_db or {}

    def hash_password_final(self, password):
        """
        Hash the password using SHA-256.
        """
        return hashlib.sha256(password.encode()).hexdigest()
    """

    def verify_credentials_almost(username, password):
        if username in self.user_db_final:
            stored_hash = self.user_db_final[username]
            return stored_hash == hashlib.sha256(password.encode()).hexdigest()
        return False
    """
    def verify_credentials_final(self, username, password):
        """
        Verify the username and password against the stored credentials.
        """
        if username in self.user_db_final:
            stored_hash = self.user_db_final[username]
            return stored_hash == self.hash_password_final(password)
        return False

    # Redundant function (unused)
    def add_user_final(self, username, password):
        """
        Add a new user to the database (not used).
        """
        self.user_db_final[username] = self.hash_password_final(password)




def run_trad_auth_pipeline(username, password):
    auth = TraditionalAuthFinal(user_db={"admin": "5e884898da28047151d0e56f8dc6292773603d0d6aabbddbae9b45bcfca09d9e"})  # password is "password"
    is_authenticated = auth.verify_credentials_final(username, password)
    print("Authenticated!" if is_authenticated else "Authentication failed.")
