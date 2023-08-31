from django.urls import path
from assignment_python_django.api import RoleApi, LoginApi, UserAPI

urlpatterns = [
    path('roles/get-all-role', RoleApi.get_all_role, name='get_all_role'),
    path('roles/get-all-role-by-is-use', RoleApi.get_all_role_by_is_use, name='get_all_role_by_is_use'),
    path('roles/get-role-by-id', RoleApi.get_role_by_id, name='get_role_by_id'),
    path('roles/post-save-role', RoleApi.save_role, name='save_role'),

    path('roles/statistics-the-number-of-user-by-role', RoleApi.get_data_statistics_the_number_of_user_by_role
         , name='get_data_statistics_the_number_of_user_by_role'),
    path('roles/statistics-the-number-of-user-by-is-use', RoleApi.get_data_statistic_the_number_of_user_by_is_use
         , name='get_data_statistic_the_number_of_user_by_is_use'),

    path('users/get-user-login', LoginApi.get_user_login, name='get_user_login'),
    path('users/get-all-user-by-is-use', UserAPI.get_all_user_by_is_use, name='get_all_user_by_is_use'),
    path('users/post-save-user', UserAPI.save_user, name='save_user'),
    path('users/delete-user', UserAPI.delete_user, name='delete_user')
]

