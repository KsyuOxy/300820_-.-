from json import dump, load


class JSONDriver:  # -> позволяет получать и сохранять данные файла
    def __init__(self, path: str):
        self._path = path  # -> переменная для указания пути к файлу

    def load_data(self):  # -> получает данные из файла
        with open(self._path, 'r', encoding='utf-8') as data:
            result = load(data)
            return result

    def save_data(self, data: dict):  # -> сохраняет данные в файл
        with open(self._path, 'w', encoding='utf-8') as file:
            dump(data, file)

