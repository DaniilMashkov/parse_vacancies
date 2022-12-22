import json


class Connector:

    def __init__(self, filename: str):
        self.__data_file = filename

    def insert(self, data: list[dict]) -> None:
        with open(self.__data_file, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def eject(self) -> list[dict]:
        with open(self.__data_file, 'r') as file:
            return json.load(file)
