import json


class Connector:
    """Запись и чтение json"""

    def __init__(self, filename: str):
        self.__data_file = filename

    def insert(self, data: list[dict]) -> None:
        with open(self.__data_file, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def eject(self) -> list[dict]:
        with open(self.__data_file, 'r') as file:
            return json.load(file)

    def insert_parsed(self, data: list[dict]) -> None:
        with open(self.__data_file, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False, default=lambda el: el.get_parsed_dict())

