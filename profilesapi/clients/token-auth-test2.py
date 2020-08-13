import requests


def client():
    data = {"username": "fernando", "email": "asd@asd.com", "password1": "fernando",
            "password2": "fernando"}

    response = requests.post(
            "http://127.0.0.1:8000/api/rest-auth/registration/",
            data=data
    )

    print(response.status_code, response.json())


if __name__ == "__main__":
    client()
