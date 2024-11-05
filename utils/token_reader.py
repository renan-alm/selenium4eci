# utils/token_reader.py
def read_token(file_path='token.txt'):
    with open(file_path, 'r') as file:
        token = file.read().strip()
    return token
