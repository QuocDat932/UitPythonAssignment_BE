from django.http import JsonResponse
from django.db import connection
from assignment_python_django.model.Device import Device, DevicesAreProvidedForUser, ProvidedDeviceForUser, DeviceTheNumberOfProvidedDeviceForUser

class DeviceService:
    @staticmethod
    def get_all_devices():
        try:
            list_data = []
            query = "SELECT DEVICE_ID, DEVICE_NAME, BRAND, VENDOR, DESCRIPTION FROM UIT_DEVICE"
            with connection.cursor() as cursor:
                 cursor.execute(query)
                 result = cursor.fetchall()

            for raw in result:
                device = Device(raw[0], raw[1], raw[2], raw[3], raw[4])
                list_data.append(device.get_json_data_device())

            return list_data;
        except Exception as e:
            print("Fail when run DeviceService - get_all_devices : ", str(e))
            return -1

    @staticmethod
    def save_device(device: Device):
        try:
            if device._device_id:
                print(">>> Case Update")
                update = "UPDATE UIT_DEVICE SET DEVICE_NAME = %s, BRAND = %s, VENDOR = %s, DESCRIPTION = %s WHERE DEVICE_ID = %s"
                with connection.cursor() as cursor:
                     cursor.execute(update, [device._device_name, device._brand, device._vendor, device._description, device._device_id])
                     connection.commit()
                return 1
            else:
                print(">>> Case Insert")
                insert = "INSERT UIT_DEVICE (DEVICE_NAME, BRAND, VENDOR, DESCRIPTION) VALUES (%s, %s, %s, %s)"
                with connection.cursor() as cursor:
                    cursor.execute(insert, [device._device_name, device._brand, device._vendor, device._description])
                    connection.commit()
                return 1
        except Exception as e:
            print("Fail when run DeviceService - save_device : ", str(e))
            return -1;

    @staticmethod
    def get_devices_for_popup_device(user_id):
        try:
            list_data = []
            query = "SELECT DEVICE_ID, DEVICE_NAME, BRAND, VENDOR, DESCRIPTION FROM UIT_DEVICE WHERE  DEVICE_ID NOT IN ( SELECT DEVICE_ID FROM UIT_PROVIDED_DEVICES prv WHERE prv.USER_ID = %s )"
            with connection.cursor() as cursor:
                 cursor.execute(query, [user_id])
                 result = cursor.fetchall()

            for raw in result:
                device = Device(raw[0], raw[1], raw[2], raw[3], raw[4])
                list_data.append(device.get_json_data_device())

            return list_data;
        except Exception as e:
            print("Fail when run DeviceService - get_devices_for_popup_device : ", str(e))
            return -1

    @staticmethod
    def check_provided_devices_for_user(user_id, device_id):
        try:
            query = "SELECT USER_ID, DEVICE_ID FROM UIT_ASSIGNMENT_PYTHON.UIT_PROVIDED_DEVICES WHERE USER_ID = %s AND DEVICE_ID = %s"
            with connection.cursor() as cursor:
                 cursor.execute(query, [user_id, device_id])
                 result = cursor.fetchone()

            if result:
                return 1
            else:
                return 0
        except Exception as e:
            print("Fail when run DeviceService - check_provided_devices_for_user : ", str(e))
            return -1

    @staticmethod
    def save_provided_device_for_user(provided : ProvidedDeviceForUser):
        try:
            isExistProvided = DeviceService.check_provided_devices_for_user(provided._user_id, provided._device_id)
            if isExistProvided == 1:
                if(provided._date_recall):
                    query = "UPDATE UIT_PROVIDED_DEVICES SET DATE_RECALL = %s, DESCRIPTION = %s WHERE USER_ID = %s AND DEVICE_ID = %s"
                    with connection.cursor() as cursor:
                         cursor.execute(query, [provided._date_recall, provided._description, provided._user_id, provided._device_id])
                         connection.commit()
                else:
                    query = "UPDATE UIT_PROVIDED_DEVICES SET DESCRIPTION = %s WHERE USER_ID = %s AND DEVICE_ID = %s"
                    with connection.cursor() as cursor:
                        cursor.execute(query, [provided._description, provided._user_id, provided._device_id])
                        connection.commit()
            else:
                if(provided._date_recall):
                    query = "INSERT INTO UIT_PROVIDED_DEVICES(USER_ID, DEVICE_ID, DATE_PROVIDED, DATE_RECALL, DESCRIPTION) VALUES (%s, %s, %s, %s, %s)"
                    with connection.cursor() as cursor:
                        cursor.execute(query, [provided._user_id, provided._device_id, provided._date_provided,
                                               provided._date_recall, provided._description])
                        connection.commit()
                else:
                    query = "INSERT INTO UIT_PROVIDED_DEVICES(USER_ID, DEVICE_ID, DATE_PROVIDED, DESCRIPTION) VALUES (%s, %s, %s, %s)"
                    with connection.cursor() as cursor:
                        cursor.execute(query, [provided._user_id, provided._device_id, provided._date_provided, provided._description])
                        connection.commit()
            return 1
        except Exception as e:
            print("Fail when run DeviceService - check_provided_devices_for_user : ", str(e))
            return -1

    @staticmethod
    def statistics_the_number_of_device_provided_for_user():
        try:
            result_data = []
            query = "SELECT a.device_id, a.device_name, COUNT(b.user_id) AS user_ FROM uit_device a JOIN uit_provided_devices b ON a.device_id = b.device_id GROUP BY a.device_id , a.device_name HAVING user_ >= 2 ORDER BY user_ DESC LIMIT 3"

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

            for raw in result:
                data = DeviceTheNumberOfProvidedDeviceForUser(raw[0], raw[1], raw[2])
                result_data.append(data.get_json_data_device_the_number_of_provided_device_user())
            cursor.close()
            return result_data
        except Exception as e:
            print("Fail when run DeviceService - statistics_the_number_of_device_provided_for_user", str(e))
            return -1

