from django.http import JsonResponse
from django.db import connection
from assignment_python_django.model.Role import Role, RoleStatisticUserByRole, RoleStatisticUserByIsUse

class RoleService:
    @staticmethod
    def get_new_role_id():
        query = "SELECT MAX(ROLE_ID) + 1 FROM UIT_ROLE"
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        if result:
            return result

    @staticmethod
    def get_role_by_id(role_id):
        query = "SELECT ROLE_ID, ROLE_NAME, DESCRIPTION, COLOR, IS_USE FROM UIT_ROLE WHERE ROLE_ID = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [role_id])
            result = cursor.fetchone()

        if result:
            role_data = Role(result[0], result[1], result[2], result[3], result[4])
            return role_data.get_json_data()
        else:
            return -1

    @staticmethod
    def update_role(role: Role):
        try:
            update = "UPDATE UIT_ROLE SET role_name = %s, description = %s, color = %s ,is_use = %s WHERE role_id = %s"
            with connection.cursor() as cursor:
                cursor.execute(update, [role._role_name, role._description, role._color, role._is_use, role._role_id])
                connection.commit()

            return RoleService.get_role_by_id(role._role_id)

        except:
            print("Fail when Update Role.py: ")
            return -1

    @staticmethod
    def insert_role(role: Role):
        try:
            new_role_id = RoleService.get_new_role_id()
            insert = "INSERT INTO UIT_ROLE (ROLE_ID, ROLE_NAME, DESCRIPTION, COLOR, IS_USE) VALUES (%s, %s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(insert, [new_role_id, role._role_name, role._description, role._color, role._is_use])
                connection.commit()

            return RoleService.get_role_by_id(new_role_id)

        except:
            print("Fail when Insert New Role.py: ")
            return -1

    @staticmethod
    def get_all_role_by_is_use(is_use):
        try:
            list_role = []
            if is_use:
                query = "SELECT role_id, role_name, description, is_use FROM UIT_ROLE WHERE is_use = %s"
                with connection.cursor() as cursor:
                    cursor.execute(query, [is_use])
                    result = cursor.fetchall()
            else:
                query = "SELECT role_id, role_name, description, is_use FROM UIT_ROLE"
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    result = cursor.fetchall()

            for row in result:
                role_data = {
                    "role_id": row[0],
                    "role_name": row[1],
                    "description": row[2],
                    "is_use": row[3],
                    "is_use_text": 'Đang Hoạt Động' if row[3] == 1 else 'Vô Hiệu Hoá'
                }
                list_role.append(role_data)
            cursor.close()
            return list_role
        except Exception as e:
            return -1

    @staticmethod
    def statistics_the_number_of_user_by_role():
        try:
            result_data = []
            query = "SELECT r.ROLE_NAME, COUNT(u.USER_ROLE), r.COLOR " \
                    "FROM UIT_ROLE r LEFT JOIN UIT_USER u ON u.USER_ROLE = r.ROLE_ID " \
                    "GROUP BY r.ROLE_NAME, r.COLOR"

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

            for raw in result:
                data = RoleStatisticUserByRole(raw[0], raw[1], raw[2])
                result_data.append(data.get_json_data_statistic_the_number_of_user_by_role())
            cursor.close()
            return result_data
        except Exception as e:
            print("Fail when run RoleService - analysis_the_number_of_user_by_account", str(e))
            return -1

    @staticmethod
    def statistics_the_number_of_user_by_is_use():
        try:
            result_data = []
            query = "SELECT s.STATUS_ID, s.DESCRIPTION, COUNT(u.IS_USE) `VALUE` " \
                    "FROM UIT_USER u LEFT JOIN UIT_STATUS s ON u.IS_USE = s.STATUS_ID " \
                    "GROUP BY s.STATUS_ID, s.DESCRIPTION"

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()

            for raw in result:
                data = RoleStatisticUserByIsUse(raw[0], raw[1], raw[2])
                result_data.append(data.get_json_data_statistic_the_number_of_user_by_is_use())
            cursor.close()
            return result_data
        except Exception as e:
            print("Fail when run RoleService - analysis_the_number_of_user_by_account", str(e))
            return -1

