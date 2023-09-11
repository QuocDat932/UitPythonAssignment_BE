from django.http import JsonResponse
from assignment_python_django.model.ResponseEntity import ResponseEntity
from rest_framework.decorators import api_view
from assignment_python_django.services.DeviceService import DeviceService
from assignment_python_django.model.Device import Device
import json

@api_view(["GET"])
def get_all_devices(request):
    result_data = ResponseEntity()
    try:
        data_service = DeviceService.get_all_devices()
        if data_service != -1:
            result_data.set_data(data_service)
            result_data.set_message("Success when get all devices")
            result_data.set_status(True)
        else:
            result_data.set_message("Fail when get all devices")
            result_data.set_status(False)
        return JsonResponse(result_data.get_json_data(), safe = False, status = 200)
    except Exception as e:
        print("Fail when call api - get_all_devices : ", str(e))
        result_data.set_message("Fail when get all devices")
        result_data.set_status(False)
        return JsonResponse(result_data.get_json_data(), safe = False, status = 500)


@api_view(["POST"])
def post_save_devices(request):
    result_data = ResponseEntity()
    try:
        request_data = json.loads(request.body.decode("utf-8"))
        devices_param = Device(request_data.get("device_id"), request_data.get("device_name"), request_data.get("brand"),
                               request_data.get("vendor"), request_data.get("description"))
        data_service = DeviceService.save_device(devices_param)

        if data_service != -1:
            result_data.set_message("Success when save device ")
            result_data.set_status(True)
        else:
            result_data.set_message("Fail when save device ")
            result_data.set_status(False)
        return JsonResponse(result_data.get_json_data(), safe = False, status = 200)
    except Exception as e:
        print("Fail when call api - post_save_devices : ", str(e))
        result_data.set_message("Fail when save device ")
        result_data.set_status(False)
    return JsonResponse(result_data.get_json_data(), safe = False, status = 500)


