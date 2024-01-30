import os.path

import requests
from auth import token

class CloudServer:

    def __init__(self, token, directory):
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = f"Authorization: OAuth {token}"
        self.directory = directory

        #self.create_folder(self.directory)

    def create_directory(self, path):
        url = f"{self.base_url}/resources"
        params = {"path": path}
        response = requests.put(url, self.headers, params=params)
        if response.status_code == 200:
            print(f"Папка {response} создана")
        elif response.status_code == 409:
            print(f"Папка {response} уже существует")
        else:
            print("Ошибка при создание папки", response)

    def upload_directory(self, path_file):
        file_name = os.path.basename(path_file)
        url = f"{self.base_url}/resources/upload"
        params = {"path": f"{self.directory}/{file_name}", "overwrite": "true"}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            with open(path_file, "r") as file:
                upload_file = response.json()
                requests.put(upload_file, files={"file": file})
                print(f"{path_file} загружен в {self.directory}")
        else:
            print("Ошибка при загрузки")

    def delete_direcory(self, file_name):
        url = f"{self.base_url}/resources"
        params = {"path": file_name, "permanently": "false"}
        response = requests.delete(url, headers=self.headers, params=params)
        if response.status_code == 200:
            print(f"файл {file_name} успешно удален")
        else:
            print("Ошибка при удаление файла")