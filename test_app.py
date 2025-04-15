from app import app
#  Here pytest will take this file for testing as it starts with test_.
def test_home():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Hello World!"
