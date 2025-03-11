
def api_response(data: dict, code: int = 0):
    return {
        "data": data,
        "code": code
    }
