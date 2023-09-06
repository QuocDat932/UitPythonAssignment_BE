from django.http import JsonResponse
from django.db import connection
from assignment_python_django.services.RoleService import RoleService

from assignment_python_django.model.ResponseEntity import ResponseEntity
from assignment_python_django.model.Role import Role
from assignment_python_django.model.RoleModel import RoleModel
from rest_framework.decorators import api_view
import json

@api_view(["GET"])
def get_all_role(request):
    roles = RoleModel.objects.all()
    data = []
    for role in roles:
        role_data = {
            'id': role.role_id,
            'name': role.role_name,
            "is_use": role.is_use,
            "is_use_text": 'Đang Hoạt Động' if role.is_use == 1 else 'Vô Hiệu Hoá'
        }
        data.append(role_data)

    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_role_by_id(request):
    role_id = request.GET.get('role_id')
    result_data = ResponseEntity()
    role_data = RoleService.get_role_by_id(role_id)
    if role_data != -1:
        result_data.set_data(role_data)
        result_data.set_status(True)
        result_data.set_message("Success when call API")
        return JsonResponse(result_data.get_json_data(), safe=False)
    else:
        result_data.set_status(False)
        result_data.set_message("Fail when call API")
        return JsonResponse(result_data.get_json_data(), safe=False)


@api_view(["POST"])
def save_role(request):
    result_data = ResponseEntity()
    try:
        request_data = json.loads(request.body.decode("utf-8"))
        role_param = Role(request_data.get("role_id"), request_data.get("role_name"), request_data.get("description"),
                          request_data.get("color"), request_data.get("is_use"))
        if not request_data.get("role_id"):
            # Case Insert
            role_data = RoleService.insert_role(role_param)
            if role_data != -1:
                result_data.set_data(role_data)
                result_data.set_status(True)
                result_data.set_message("Success when Insert Role ")
                return JsonResponse(result_data.get_json_data(), safe=False)
            else:
                result_data.set_status(False)
                result_data.set_message("Fail when Insert Role ")
                return JsonResponse(result_data.get_json_data(), safe=False)

        else:
            # Case Update
            role_data = RoleService.update_role(role_param)
            if role_data != -1:
                result_data.set_data(role_data)
                result_data.set_status(True)
                result_data.set_message("Success when Update Role ")
                return JsonResponse(result_data.get_json_data(), safe=False)
            else:
                result_data.set_status(False)
                result_data.set_message("Fail when Update Role ")
                return JsonResponse(result_data.get_json_data(), safe=False)
        result_data.set_status(True)
        result_data.set_message("Success when call API save role")
    except Exception as e:
        print("Fail when call API save role: "+ str(e))
        result_data.set_status(False)
        result_data.set_message("Fail when call API save role")
    return JsonResponse(result_data.get_json_data(), safe=False)

@api_view(["GET"])
def get_all_role_by_is_use(request):
    is_use = request.GET.get("is_use")

    result_data = ResponseEntity()
    data_services = RoleService.get_all_role_by_is_use(is_use)

    if data_services != -1:
        result_data.set_data(data_services)
        result_data.set_status(True)
        result_data.set_message("Success when call API")
    else:
        result_data.set_status(False)
        result_data.set_message("Fail when call API")

    return JsonResponse(result_data.get_json_data(), safe=False)

@api_view(["GET"])
def get_data_statistics_the_number_of_user_by_role(request):
    result_data = ResponseEntity()
    try:
        data = RoleService.statistics_the_number_of_user_by_role()
        if data != -1:
            result_data.set_data(data)
            result_data.set_status(True)
            result_data.set_message("Success when get data analysis the number of user by role")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when get data analysis the number of user by role")
        return JsonResponse(result_data.get_json_data(), safe=False, status = 200)
    except Exception as e:
        print("Fail when call api - get_data_analysis_the_number_of_user_by_role")
        return JsonResponse(result_data.get_json_data(), safe=False, status=500)

@api_view(["GET"])
def get_data_statistic_the_number_of_user_by_is_use(request):
    result_data = ResponseEntity()
    try:
        data_services = RoleService.statistics_the_number_of_user_by_is_use()
        if data_services != -1:
            result_data.set_data(data_services)
            result_data.set_status(True)
            result_data.set_message("Success when get data statistic the number of user by is use")
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when get data statistic the number of user by is use")
        return JsonResponse(result_data.get_json_data(), safe=False, status=200)
    except Exception as e:
        print("Fail when call api - get_data_statistic_the_number_of_user_by_is_use")
        return JsonResponse(result_data.get_json_data(), safe=False, status=500)

