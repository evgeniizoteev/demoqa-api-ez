import requests


def test_add_and_remove_book(api_user):
    user_id = api_user["user_id"]
    headers = api_user["headers"]

    payload = {
        "userId": user_id,
        "collectionOfIsbns": [
            {"isbn": "9781449325862"},
        ],
    }
    add_response = requests.post(
        "https://demoqa.com/BookStore/v1/Books",
        json=payload,
        headers=headers,
        timeout=15,
    )
    assert add_response.status_code == 201

    get_response = requests.get(
        f"https://demoqa.com/Account/v1/User/{user_id}",
        headers=headers,
        timeout=15,
    )
    assert get_response.status_code == 200
    user_body = get_response.json()
    books = user_body["books"]
    assert len(books) == 1
    assert books[0]["isbn"] == "9781449325862"

    delete_payload = {
        "isbn": "9781449325862",
        "userId": user_id,
    }
    delete_response = requests.delete(
        "https://demoqa.com/BookStore/v1/Book",
        json=delete_payload,
        headers=headers,
        timeout=15,
    )
    assert delete_response.status_code == 204

    final_response = requests.get(
        f"https://demoqa.com/Account/v1/User/{user_id}",
        headers=headers,
        timeout=15,
    )
    assert final_response.status_code == 200
    final_body = final_response.json()
    assert final_body["books"] == []
