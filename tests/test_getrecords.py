import requests
import utility.config
from utility import config


def test_getrecords(base_url):
    product_record = config.product_record
    print(product_record)
    response = requests.get(
        url=f"{base_url}/collections/products/records/{product_record}",
        headers=utility.config.headers,
    )

    body_data = response.json()
    print(body_data)
    assert response.status_code == 200
    assert body_data["data"]["id"] == product_record
    assert body_data["data"]["project_id"] == 55866
