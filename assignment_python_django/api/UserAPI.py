from django.http import JsonResponse
from django.db import connection
from assignment_python_django.model.ResponseEntity import ResponseEntity
from rest_framework.decorators import api_view
from assignment_python_django.services.UserService import UserService

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
        result_data.set_message("Success when call API")
    else:
        result_data.set_status(False)
        result_data.set_message("Fail when call API")

    return JsonResponse(result_data.get_json_data(), safe=False)


