import uuid


def generate_customized_uuid(prefix=""):
    uuid_string = str(uuid.uuid4())
    if prefix:
        return f"{prefix}-{uuid_string}"
    return uuid_string
