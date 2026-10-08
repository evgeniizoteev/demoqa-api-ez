from uuid import uuid4

import requests


def test_create_user():
    username = f"QAStudent_{uuid4().hex}"
    payload = {
        "userName": username,
        "password": "Practice123!",
    }

    response = requests.post(
        "https://demoqa.com/Account/v1/User",
        json=payload,
        timeout=15,
    )
    assert response.status_code == 201
    body = response.json()
    user_id = body["userID"]

    token_response = requests.post(
        "https://demoqa.com/Account/v1/GenerateToken",
        json=payload,
        timeout=15,
    )
    assert token_response.status_code == 200
    token_body = token_response.json()
    assert token_body["status"] == "Success"
    token = token_body["token"]
    assert isinstance(token, str) and token

    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        assert body["username"] == username

        get_response = requests.get(
            f"https://demoqa.com/Account/v1/User/{user_id}",
            headers=headers,
            timeout=15,
        )
        assert get_response.status_code == 200
        user_body = get_response.json()
        assert user_body["username"] == username
        assert user_body["userId"] == user_id
    finally:
        delete_response = requests.delete(
            f"https://demoqa.com/Account/v1/User/{user_id}",
            headers=headers,
            timeout=15,
        )
        assert delete_response.status_code == 204
    deleted_response = requests.get(
        f"https://demoqa.com/Account/v1/User/{user_id}",
        headers=headers,
        timeout=15,
    )
    assert deleted_response.status_code == 401
    deleted_body = deleted_response.json()
    assert deleted_body["code"] == "1207"
    assert deleted_body["message"] == "User not found!"
