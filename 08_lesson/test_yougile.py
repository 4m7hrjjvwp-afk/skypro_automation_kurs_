from ProjectsAPI import ProjectsAPI
from dotenv import load_dotenv
import os

load_dotenv()

api = ProjectsAPI("https://ru.yougile.com")


# Проверка получения списка ключей
def test_get_keys():
    login = os.getenv("login")
    password = os.getenv("password")
    result = api.get_keys_list(login, password)
    assert result["key"]


# Проверка создания проекта
def test_create_project():
    login = os.getenv("login")
    password = os.getenv("password")
    my_token = api.get_keys_list(login, password)
    response.json().get(my_token)
    title = "Старый проект"
    result = api.create_project(title)
    new_id = result.json().get("id")
    new_project = api.create_project("new_id")
    assert new_project.status_code == 200
    assert new_project.json()["id"] == new_id


# Провека изменения проекта
def test_update_project():
    login = os.getenv("login")
    password = os.getenv("password")
    my_token = api.get_keys_list(login, password)
    response.json().get(my_token)
    new_title = "Новый проект"
    result = api.update_project(new_title)
    assert result.status_code == 200
    assert result["title"] == new_title


# Проверка получения проекта по ID
def test_get_project_id():
    login = os.getenv("login")
    password = os.getenv("password")
    my_token = api.get_keys_list(login, password)
    response.json().get(my_token)
    found_project = api.get_project_id(id)
    assert found_project

