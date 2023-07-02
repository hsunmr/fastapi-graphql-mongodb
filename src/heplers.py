from base64 import b64encode, b64decode

def encode_user_cursor(key: str, id: str) -> str:
  return b64encode(f"{key}:{id}".encode("ascii")).decode("ascii")


def decode_user_cursor(cursor: str) -> str:
  cursor_data = b64decode(cursor.encode("ascii")).decode("ascii")
  return str(cursor_data.split(":")[1])