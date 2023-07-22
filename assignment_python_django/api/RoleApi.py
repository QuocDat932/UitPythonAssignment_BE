from django.http import JsonResponse
from django.db import connection
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
            'is_use': 'Active' if str(role.is_use)*1 == 1 else 'inActive'
        }
        data.append(role_data)

    return JsonResponse(data, safe=False)


@api_view(["GET"])
def get_role_by_id(request):
    role_id = request.GET.get('role_id')
    query = "SELECT role_id, role_name, is_use FROM UIT_ROLE WHERE role_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [role_id])
        result = cursor.fetchone()

    if result:
        role_data = {
            "role_id": result[0],
            "role_name": result[1],
            "is_use": 'Active' if str(result[2])[-2] == '1' else 'inActive',
        }
        return JsonResponse(role_data)
    else:
        return JsonResponse({"error": "Role not found"}, status=404)

