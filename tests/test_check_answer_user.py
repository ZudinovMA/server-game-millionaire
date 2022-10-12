import json

from tests.test_utils import setup  # type: ignore

user_response_correct = {"user_id": "test_user_id",
                         "answer_id": 1}

user_response_with_incorrect_type_answer_user = {"user_id": "test_user_id",
                                                 "answer_id": "answer_user"}


def test_check_answer_user_with_correct_user_response(setup) -> None:
    """
        Тестирование запроса с корректно переданными данными
    :param setup:
    :return:
    """

    # Подготовка данных
    global user_response_correct
    client = setup

    # Вызов тестируемой функции
    response_check_answer_user = client.post("/check_answer_user", data=json.dumps(user_response_correct))

    # Тестирование результатов
    assert response_check_answer_user.status_code == 200
    assert response_check_answer_user.json() == {"status": "success", "answer": True}


def test_check_answer_user_with_incorrect_type_answer_user(setup) -> None:
    """
        Тестирование запроса с неверным типом id ответа
    :param setup:
    :return:
    """

    # Подготовка данных
    global user_response_with_incorrect_type_answer_user
    client = setup

    # Вызов тестируемой функции
    response_check_answer_user = client.post("/check_answer_user",
                                             data=json.dumps(user_response_with_incorrect_type_answer_user))

    # Тестирование результатов
    assert response_check_answer_user.status_code == 422
    assert response_check_answer_user.json() == {"status": "error", "answer": "Invalid data type"}