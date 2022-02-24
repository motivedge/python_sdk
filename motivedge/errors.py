
class TokenError(Exception):
    def __init__(self, token: str, message: str):
        self.token = token
        self.message = message
        super().__init__(self.message)
    

class TokenMissError(TokenError):
    def __init__(self, token: str, message: str = "Token is missing"):
        super().__init__(token, message)



class HTTPError(Exception):
    def __init__(self, response_json: dict):
        self.response_json = response_json
        err_msg = f"HTTPError {response_json['status']}, Reason: {response_json['message']}"
        super().__init__(err_msg)
    

class YamlFileError(Exception):
    def __init__(self, path: str, message: str):
        self.path = path
        self.message = message
        super().__init__(self.message)
