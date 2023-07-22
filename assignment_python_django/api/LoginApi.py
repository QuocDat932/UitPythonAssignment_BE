from django.http import JsonResponse
from django.db import connection
from assignment_python_django.model.ResponseEntity import ResponseEntity
from rest_framework.decorators import api_view
from assignment_python_django.model.User import User


@api_view(["GET"])
def get_user_login1(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    query = "SELECT USER_ID, USER_NAME, MSSV, EMAIL, IMG, ADDRESS, BIRTHDAY, USER_ROLE, IS_USE " \
            "FROM UIT_USER WHERE EMAIL = %s AND MSSV = %s"

    with connection.cursor() as cursor:
        cursor.execute(query, [email, password])
        result = cursor.fetchone()

    response_data = ResponseEntity()

    if result:
        user_data = {
            "user_id": result[0],
            "user_name": result[1],
            "mssv": result[2],
            "email": result[3],
            "img": result[4],
            "address": result[5],
            "birthday": result[6],
            "role": result[7],
            "is_use": 'Active' if str(result[2])[-2] == '1' else 'inActive'
        }
        response_data.set_data(user_data)
        response_data.set_status(True)
        response_data.set_message("Get Success User")

        return JsonResponse(response_data.get_json_data(), safe=False)
    else:
        response_data.set_message("Get Fail User")
        return JsonResponse(response_data.get_json_data(), status=404)


@api_view(["GET"])
def get_user_login(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    response_data = ResponseEntity()

    try:
        user = User.objects.get(email=email, mssv=password)

        user_data = {
            'user_id': user.user_id,
            'user_name': user.user_name,
            'mssv': user.mssv,
            'email': user.email,
            'img': user.img,
            'address': user.address,
            'role': {
                'role_id': user.role.role_id,
                'role_name': user.role.role_name,
                'is_use': 'Active' if str(user.role.is_use) * 1 == 1 else 'inActive'
            },
            'is_use': 'Active' if str(user.is_use) * 1 == 1 else 'inActive'
        }

        response_data.set_data(user_data)
        response_data.set_status(True)
        response_data.set_message("Get Success User")

    except User.DoesNotExist:
        response_data.set_message("Does not exist User")

    return JsonResponse(response_data.get_json_data(), safe=False)


