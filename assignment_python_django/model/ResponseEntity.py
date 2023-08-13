
class ResponseEntity:
    """ Result data of api

    :return
        {   data: data of api,
            status: status of API [True/False],
            message: notification of API
        }

    """
    data = {}
    status = False
    message = ""

    def set_data(self, data):
        self.data = data

    def set_status(self, status):
        self.status = status

    def set_message(self, message):
        self.message = message

    def get_data(self):
        return self

    def get_json_data(self):
        return {
            "data": self.data,
            "status": self. status,
            "message": self.message
        }
