import requests

from utility import config


def test_updaterecords(base_url):
    headers = config.headers
    response = requests.put(
        f'{base_url}/collections/products/records/{config.product_to_update}?project_id={config.project_id}',
        headers=headers, json={
            "data": {
                "name": "Wirelesss_Test Headphones_JP",
                "price": 55.98,
                "category": "Electronics",
                "in_stock": True
            }}
    )

    body_data = response.json()
    print(body_data)
    assert response.status_code==200
    assert body_data["data"]["data"]["price"] == 55.98
    assert body_data["data"]["data"]["name"] == "Wirelesss_Test Headphones_JP"
