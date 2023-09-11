from django.http import JsonResponse
from django.db import connection
from assignment_python_django.model.Device import Device, DevicesAreProvidedForUser

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