def read_file(filename: str) -> str:
    with open(filename) as file:
        return file.read()
