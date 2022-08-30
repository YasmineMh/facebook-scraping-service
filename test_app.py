from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "Default API is working!"}


def test_default_scraping():
    resp = client.get("/default_scraping")
    data_testing = open('data_testing.txt', 'r').read()
    assert resp.status_code == 200
    assert resp.json()[0] == data_testing


def test_custom_scraping():
    json_post = {"page_name": "Generalsoftwareengineeringposts-102394349277873", "posts_count": 10, "timeout": 600}
    resp = client.post("/custom_scraping", json=json_post)
    assert resp.status_code == 200
