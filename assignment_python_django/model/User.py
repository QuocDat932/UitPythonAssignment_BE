class User:
    def __init__(self, mssv: str, user_name: str, email: str, address: str, birthday: str, role_id: int, is_use: int):
        self._mssv = mssv
        self._user_name = user_name
        self._email = email
        self._address = address
        self._birthday = birthday
        self._role_id = role_id
        self._is_use = is_use

    def get_json_data(self):
        return {
            "mssv": self._mssv,
            "user_name":self._user_name,
            "email":self._email,
            "address":self._address,
            "birthday":self._birthday,
            "role_id":self._role_id,
            "is_use":self._is_use
        }
