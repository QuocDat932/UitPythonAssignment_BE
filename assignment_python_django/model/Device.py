class Device:
    def __init__(self, device_id, device_name, brand, vendor, description):
        self._device_id = device_id
        self._device_name = device_name
        self._brand = brand
        self._vendor = vendor
        self._description = description

    def get_json_data_device(self):
        return {
            "device_id": self._device_id,
            "device_name": self._device_name,
            "brand": self._brand,
            "vendor": self._vendor,
            "description": self._description
        }


class DevicesAreProvidedForUser:
    def __init__(self, number, device_id, device_name, brand, date_provide, date_recall, description ):
        self._number = number
        self._device_id = device_id
        self._device_name = device_name
        self._brand = brand
        self._date_provide = date_provide
        self._date_recall = date_recall
        self._description = description

    def get_json_data_device_is_provided_for_user(self):
        return {
            "number": self._number,
            "device_id": self._device_id,
            "device_name": self._device_name,
            "date_provide": self._date_provide,
            "date_recall": self._date_recall,
            "description": self._description
        }

class ProvidedDeviceForUser:
    def __init__(self, user_id, device_id, date_provided, date_recall, description):
        self._user_id = user_id
        self._device_id = device_id
        self._date_provided = date_provided
        self._date_recall = date_recall
        self._description = description

    def get_json_data_provide_device_for_user(self):
        return {
            "user_id": self._user_id,
            "device_id": self._device_id,
            "date_provide": self._date_provide,
            "date_recall": self._date_recall,
            "description": self._description
        }

class DeviceTheNumberOfProvidedDeviceForUser:
    def __init__(self, device_id, device_name, value):
        self._device_id = device_id
        self._device_name = device_name
        self._value = value

    def get_json_data_device_the_number_of_provided_device_user(self):
        return {
            "device_id": self._device_id,
            "device_name": self._device_name,
            "value": self._value
        }

class DeviceTheNumberOfProvidedDeviceForUser:
    def __init__(self, device_id, device_name, value):
        self._device_id = device_id
        self._device_name = device_name
        self._value = value

    def get_json_data_device_the_number_of_provided_device_user(self):
        return {
            "device_id": self._device_id,
            "device_name": self._device_name,
            "value": self._value
        }
