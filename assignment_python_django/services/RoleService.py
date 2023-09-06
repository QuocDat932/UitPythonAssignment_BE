from django.http import JsonResponse
from django.db import connection


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
        query = "SELECT role_id, role_name, description, is_use FROM UIT_ROLE WHERE role_id = %s"
        with connection.cursor() as cursor:
            cursor.execute(query, [role_id])
            result = cursor.fetchone()

        if result:
            role_data = {
                "role_id": result[0],
                "role_name": result[1],
                "description": result[2],
                "is_use": result[3],
                "is_use_text": 'Đang Hoạt Động' if result[2] == 1 else 'Vô Hiệu Hoá'
            }
            return role_data
        else:
            return -1

    @staticmethod
    def update_role(role_name, description, is_use, role_id):
        try:
            update = "UPDATE UIT_ROLE SET role_name = %s, description = %s, is_use = %s WHERE role_id = %s"
            with connection.cursor() as cursor:
                cursor.execute(update, (role_name, description, is_use, role_id))
                connection.commit()

            return RoleService.get_role_by_id(role_id)

        except:
            print("Fail when Update Role: ")
            return -1

    @staticmethod
    def insert_role(role_name, description, is_use):
        try:
            new_role_id = RoleService.get_new_role_id()
            insert = "INSERT INTO UIT_ROLE (ROLE_ID, ROLE_NAME, DESCRIPTION, IS_USE) VALUES (%s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(insert, (new_role_id, role_name, description, is_use))
                connection.commit()

            return RoleService.get_role_by_id(new_role_id)

        except:
            print("Fail when Insert New Role: ")
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
