import requests


def client():
    token_h = "Token b5780394f3ea0530590202abf0a568c02aa79ffb"
    headers = {"Authorization": token_h}

    response = requests.get(
            "http://127.0.0.1:8000/api/profiles/",
            headers=headers
    )

    print(response.status_code, response.json())


if __name__ == "__main__":
    client()
