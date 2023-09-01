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
    def __init__(self, number, device_name, brand, date_provide, date_recall, description ):
        self._number = number
        self._device_name = device_name
        self._brand = brand
        self._date_provide = date_provide
        self._date_recall = date_recall
        self._description = description

    def get_json_data_device_is_provided_for_user(self):
        return {
            "number": self._number,
            "device_name": self._device_name,
            "date_provide": self._date_provide,
            "date_recall": self._date_recall,
            "description": self._description
        }
