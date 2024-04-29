import base64
def base64_decode(base64_string:str) -> str:
    # Decode the Base64 string
    decoded_bytes = base64.b64decode(base64_string)

    # Convert the decoded bytes to a string
    decoded_string = decoded_bytes.decode('utf-8')

    return decoded_string

