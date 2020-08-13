import requests


def client():
    # credentials = {"username": "admin", "password": "admin"}

    response = requests.get(
            "http://127.0.0.1:8000/api/profiles/",
    )

    print(response.status_code, response.json())


if __name__ == "__main__":
    client()
