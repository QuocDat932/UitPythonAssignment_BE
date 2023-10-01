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


class UserWithNumberOfDevice:
    def __init__(self, number: int, user_id: str, mssv: str, user_name: str, total_provided: int, total_recall: int):
        self._number = number
        self._user_id = user_id
        self._mssv = mssv
        self._user_name = user_name
        self._total_provided = total_provided
        self._total_recall = total_recall
        self._total_owe = total_provided - total_recall

    def get_json_data(self):
        return {
            "number": self._number,
            "user_id": self._user_id,
            "mssv":self._mssv,
            "user_name":self._user_name,
            "total_provided":self._total_provided,
            "total_recall":self._total_recall,
            "total_owe":self._total_owe
        }

class UserByProvidedDevice:
    def __init__(self, mssv, user_name, date_provided, date_recall):
        self._mssv = mssv
        self._user_name = user_name
        self._date_provided = date_provided
        self._date_recall = date_recall

    def get_json_data_user_by_provided_device(self):
        return {
            "mssv": self._mssv,
            "user_name": self._user_name,
            "date_provided": self._date_provided,
            "date_recall": self._date_recall
        }