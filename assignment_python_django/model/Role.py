class Role():
    def __init__(self, role_id, role_name, description, color, is_use):
        self._role_id = role_id
        self._role_name = role_name
        self._description = description
        self._color = color
        self._is_use = is_use
        self._is_use_text = 'Đang Hoạt Động' if is_use == 1 else 'Vô Hiệu Hoá'

    def get_json_data(self):
        return {
            "role_id": self._role_id,
            "role_name": self._role_name,
            "description": self._description,
            "color": self._color,
            "is_use":self._is_use,
            "is_use_text": self._is_use_text
        }


# class to statistic the number of user by role
class RoleStatisticUserByRole:
    def __init__(self, role_name, value, color):
        self._role_name = role_name
        self._value = value
        self._color = color
    def get_json_data_statistic_the_number_of_user_by_role(self):
        return {
            "role_name": self._role_name,
            "color": self._color,
            "value": self._value
        }

# class to statistic the number of user by is_use
class RoleStatisticUserByIsUse:
    def __init__(self, status_id, label, value):
        self._status_id = status_id
        self._label = label
        self._value = value

    def get_json_data_statistic_the_number_of_user_by_is_use(self):
        return {
            "status_id": self._status_id,
            "label": self._label,
            "value": self._value
        }