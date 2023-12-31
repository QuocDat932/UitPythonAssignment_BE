from django.http import JsonResponse
from django.db import connection
from assignment_python_django.model.ResponseEntity import ResponseEntity
from rest_framework.decorators import api_view
from assignment_python_django.services.UserService import UserService
from assignment_python_django.model.User import User
from flask import Flask, request, jsonify
import json

#[TanPhan - Dev] - [Nha Uyen Test]
# Commit: BE0005 - Create API GetAllUser/GetUserByIsUse
@api_view(['GET'])
def get_all_user_by_is_use(request):
    is_use = request.GET.get('is_use')
    result_data = ResponseEntity()

    data_services = UserService.get_user_by_is_use(is_use)
    if data_services != -1:
        result_data.set_data(data_services)
        result_data.set_status(True)
        result_data.set_message("Success when get User")
    else:
        result_data.set_status(False)
        result_data.set_message("Fail when get User")

    return JsonResponse(result_data.get_json_data(), safe=False)

@api_view(["POST"])
def save_user(request):
    result_data = ResponseEntity()
    try:
        request_data = json.loads(request.body.decode("utf-8"))
        user_param = User(request_data.get("mssv"), request_data.get("user_name"), request_data.get("email"),
                          request_data.get("address"), request_data.get("birthday"), request_data.get("role_id"),
                          request_data.get("is_use"))
        data_service = UserService.save_user(user_param)
        if data_service != -1:
            result_data.set_data(data_service)
            result_data.set_status(True)
            result_data.set_message("Success when Save User")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when Save User")
        return JsonResponse(result_data.get_json_data(), status=200)
    except Exception as e:
        print("Fail when call API: " + str(e))
        result_data.set_status(False)
        result_data.set_message("Fail when call API: " + str(e))
        return JsonResponse(result_data.get_json_data(), status=500)

@api_view(["POST"])
def delete_user(request):
    mssv = request.data['mssv']
    result_data = ResponseEntity()
    try:
        data_service = UserService.delete_user(mssv)
        if data_service != -1:
            result_data.set_status(True)
            result_data.set_message("Success when Delete User")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when Delete User")

    except Exception as e:
        result_data.set_status(False)
        result_data.set_message("Fail when Delete User")

    return JsonResponse(result_data.get_json_data(), safe=False)

@api_view(['GET'])
def get_device_is_provided_for_user(request):
    result_data = ResponseEntity()
    try:
        user_id = request.GET.get("user_id")
        data_services = UserService.get_device_is_provided_for_user(user_id)
        if data_services != -1:
            result_data.set_data(data_services)
            result_data.set_status(True)
            result_data.set_message("Success when get device provided by user")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when get device provided by user")
        return JsonResponse(result_data.get_json_data(),  safe = False, status = 200)
    except Exception as e:
        print("Fail when call API - get_device_provided_by_user: ", str(e))
        result_data.set_status(False)
        result_data.set_message("Fail when get device provided by user")
        return JsonResponse(result_data.get_json_data(), safe = False, status = 500)

@api_view(['GET'])
def get_all_user_with_the_number_of_device(request):
    result_data = ResponseEntity()
    try:
        data_services = UserService.get_all_user_with_the_number_of_device()
        if data_services != -1:
            result_data.set_data(data_services)
            result_data.set_status(True)
            result_data.set_message("Success when get all user with the number of device")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when get all user with the number of device")
        return JsonResponse(result_data.get_json_data(), safe=False, status=200)
    except Exception as e:
        print("Fail when call API - get_all_user_with_the_number_of_device: ", str(e))
        result_data.set_status(False)
        result_data.set_message("Fail when get all user with the number of device")
        return JsonResponse(result_data.get_json_data(), safe=False, status=500)

@api_view(['GET'])
def get_data_user_by_provided_device(request):
    result_data = ResponseEntity()
    try:
        device_id = request.GET.get("device_id")
        data_services = UserService.get_data_user_by_provided_device(device_id)
        if data_services != -1:
            result_data.set_data(data_services)
            result_data.set_status(True)
            result_data.set_message("Success when get data user by provided device")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when get data user by provided device")
        return JsonResponse(result_data.get_json_data(), safe=False, status=200)
    except Exception as e:
        print("Fail when call API - get_data_user_by_provided_device: ", str(e))
        result_data.set_status(False)
        result_data.set_message("Fail when get data user by provided device")
        return JsonResponse(result_data.get_json_data(), safe=False, status=500)


