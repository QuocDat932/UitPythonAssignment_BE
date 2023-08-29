from django.http import JsonResponse
from django.db import connection
from assignment_python_django.services.RoleService import RoleService

from assignment_python_django.model.ResponseEntity import ResponseEntity
from assignment_python_django.model.Role import Role
from rest_framework.decorators import api_view


@api_view(["GET"])
def get_all_role(request):
    roles = Role.objects.all()
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
    role_id = request.data["role_id"]
    role_name = request.data["role_name"]
    description = request.data["description"]
    is_use = request.data["is_use"]

    result_data = ResponseEntity()

    if not role_id:
        # Case Insert
        role_data = RoleService.insert_role(role_name, description, is_use)
        if role_data != -1:
            result_data.set_data(role_data)
            result_data.set_status(True)
            result_data.set_message("Success when Insert Role")
            return JsonResponse(result_data.get_json_data(), safe=False)
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when Insert Role")
            return JsonResponse(result_data.get_json_data(), safe=False)

    else:
        # Case Update
        role_data = RoleService.update_role(role_name, description, is_use, role_id)
        if role_data != -1:
            result_data.set_data(role_data)
            result_data.set_status(True)
            result_data.set_message("Success when Update Role")
            return JsonResponse(result_data.get_json_data(), safe=False)
        else:
            result_data.set_status(False)
            result_data.set_message("Fail when Update Role")
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