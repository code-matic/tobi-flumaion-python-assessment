
import datetime
from decimal import Decimal

def api_response(data: dict, code: int = 0):
    return {
        "data": data,
        "code": code
    }

def default_converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()  # convert date/datetime to ISO string
    if isinstance(o, Decimal):
        return float(o)       # convert Decimal to float
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")