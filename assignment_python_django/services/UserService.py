from django.http import JsonResponse
from django.db import connection
from assignment_python_django.services.RoleService import RoleService

class UserService:

    @staticmethod
    def get_user_by_is_use(is_use):
        try:
            list_result = []
            if is_use:
                query = "SELECT USER_ID, USER_NAME, MSSV, EMAIL, IMG, ADDRESS, BIRTHDAY, USER_ROLE, IS_USE FROM UIT_USER " \
                        "WHERE IS_USE = %s"
                with connection.cursor() as cursor:
                    cursor.execute(query, [is_use])
                    result = cursor.fetchall()
            else:
                query = "SELECT USER_ID, USER_NAME, MSSV, EMAIL, IMG, ADDRESS, BIRTHDAY, USER_ROLE, IS_USE FROM UIT_USER "
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()

            for row in result:
                user_role = RoleService.get_role_by_id(row[7])
                if(user_role):
                    user_data = {
                        "user_id": row[0],
                        "user_name": row[1],
                        "mssv": row[2],
                        "email": row[3],
                        "img": row[4],
                        "address": row[5],
                        "birthday": row[6],
                        "role": {
                            'role_id': user_role["role_id"],
                            'role_name': user_role["role_name"]
                        },
                        "is_use": row[8],
                        "is_use_text": 'Đang Hoạt Động' if row[8] == 1 else 'Vô Hiệu Hoá'
                    }
                list_result.append(user_data)
            cursor.close()
            return list_result
        except Exception as e:
            print("Fail when get User By Is Use ", e)
            return -1

