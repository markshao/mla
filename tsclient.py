import tushare as ts
import os
__client = None

def get_client():
    global __client
    if not __client:
        __client = ts.pro_api(os.getenv("TUSHARE_TOKEN"))

    return __client