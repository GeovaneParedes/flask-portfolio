from app import create_app

def test_index_status_code():
    app = create_app({"TESTING": True})
    client = app.test_client()

    resp = client.get("/")
    assert resp.status_code == 200
    assert b"@DevGege" in resp.data or b"DevGege" in resp.data
