from django.http import JsonResponse
from django.db import connection
from assignment_python_django.services.RoleService import RoleService
from assignment_python_django.model.User import User


class UserService:

    @staticmethod
    def get_user_by_mssv(mssv):
        try:
            if mssv:
                print("success When run Service UserService - get_user_by_mssv: ")
                query = "SELECT MSSV, USER_NAME, EMAIL, ADDRESS, CONVERT(BIRTHDAY, CHAR) AS BIRTHDAY, USER_ROLE, IS_USE FROM UIT_USER " \
                        "WHERE MSSV = %s"
                with connection.cursor() as cursor:
                    cursor.execute(query, [mssv])
                    result = cursor.fetchone()
                if result:
                    user = User(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
                    return user.get_json_data()
                else:
                    return -1
            else:
                return -1
        except Exception as e:
            print("Fail When run Service UserService - get_user_by_mssv: "+ str(e))
            return -1


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
                query = "SELECT USER_ID, USER_NAME, MSSV, EMAIL, IMG, ADDRESS, BIRTHDAY, USER_ROLE, IS_USE FROM UIT_USER"
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
            print("Fail When run Service UserService - get_user_by_is_use: ", e)
            return -1


    @staticmethod
    def generate_user_id():
        query = "SELECT MAX(USER_ID) + MAX(MSSV) FROM UIT_USER"
        with connection.cursor() as cursor:
             cursor.execute(query)
             result = cursor.fetchone()
        if result:
            return result
        else:
            return -1


    @staticmethod
    def save_user(user: User):
        try:
            if user._mssv:
                 # Update User
                 query = "UPDATE UIT_USER SET USER_NAME =%s, EMAIL =%s, ADDRESS =%s, BIRTHDAY =%s, USER_ROLE =%s, IS_USE =%s WHERE MSSV =%s"
                 with connection.cursor() as cursor:
                     cursor.execute(query, [user._user_name, user._email, user._address, user._birthday,
                                         user._role_id, user._is_use, user._mssv])
                     connection.commit()
                 return UserService.get_user_by_mssv(user._mssv)
            else:
                mssv_gen = UserService.generate_user_id()
                if mssv_gen != -1:
                    query = "INSERT INTO UIT_USER(USER_NAME, EMAIL, ADDRESS, BIRTHDAY, USER_ROLE, IS_USE, MSSV) " \
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    with connection.cursor() as cursor:
                        cursor.execute(query, [user._user_name, user._email, user._address, user._birthday,
                                               user._role_id, user._is_use, mssv_gen])
                        connection.commit()
                    return UserService.get_user_by_mssv(mssv_gen)
                else:
                    return -1
        except Exception as e:
            print("Fail When run Service UserService - save_user: "+ str(e))
            return -1


    @staticmethod
    def delete_user(mssv):
        try:
            print(">>>>>>>>>>", mssv)
            if mssv:
                query = "DELETE FROM UIT_USER WHERE MSSV = %s"
                with connection.cursor() as cursor:
                     cursor.execute(query, [mssv])
                     connection.commit()
                return 1
            else:
                return -1
        except Exception as e:
            print("Fail when run Services UserService - delete_user: "+ str(e))
            return -1
