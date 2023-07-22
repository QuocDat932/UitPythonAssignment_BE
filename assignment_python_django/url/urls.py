from django.urls import path
from assignment_python_django.api import RoleApi, LoginApi

urlpatterns = [
    path('roles/get-all-role', RoleApi.get_all_role, name='get_all_role'),
    path('roles/get-role-by-id', RoleApi.get_role_by_id, name='get_role_by_id'),

    path('users/get-user-login', LoginApi.get_user_login, name='get_user_login'),
]

