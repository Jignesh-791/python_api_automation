import requests

from utility import config


def test_createnewrecord(base_url):
    project_id = config.project_id
    response = requests.post(
        headers=config.headers,
        url=f"{base_url}/collections/products/records?project_id={project_id}",

        json={
            "data":
                {"name": "Wirelesss_Test Headphones",
                 "price": 59.98,
                 "category": "Electronics",
                 "in_stock": True
                 }
        }

    )
    response_body = response.json()
    print(response_body)
    assert response.status_code == 201
    assert response_body["data"]["data"]["price"] == 59.98
    assert response_body["data"]["data"]["name"] == "Wirelesss_Test Headphones"
