import requests


def test_listrecords(base_url):
    headers = {
        "x-api-key": "pro_00ff42027c7f89605e5391eebc80324d616fd57400494999b4aa2718c17c146e",
        "X-Reqres-Env": "prod"
    }
    response = requests.get(
        url=f"{base_url}/collections/products/records",
        headers=headers,
    )

    body_data = response.json()
    print(body_data)
    assert response.status_code == 200
    assert body_data is not None
    assert body_data["data"] is not None
    assert body_data["data"][0]["project_id"] == 55866
