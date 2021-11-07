from fastapi.testclient import TestClient

from main import api, configure

client = TestClient(api)
configure()


def test_index_page():
    response = client.get("/")
    assert response.status_code == 200


def test_favicon():
    response = client.get("/favicon.ico")
    assert response.status_code == 200


def test_404():
    response = client.get("/api/podcasts/blackhole")
    assert response.status_code == 404


def test_all_podcast_api():
    response = client.get("/api/podcasts")
    assert response.status_code == 200


def test_one_podcast_api():
    response = client.get("/api/podcasts")
    assert response.status_code == 200
