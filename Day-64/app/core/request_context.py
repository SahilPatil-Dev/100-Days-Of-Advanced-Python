import uuid
from contextvars import ContextVar

request_id_ctx = ContextVar("request_id", default=None)

def set_request_id():
    request_id = str(uuid.uuid4())
    request_id_ctx.set(request_id)
    return request_id

def get_request_id():
    return request_id_ctx.get()