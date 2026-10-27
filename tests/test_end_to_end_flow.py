from utility import config
import requests

def test_end_to_end(base_url):
    # Step 1: Create a new record
    create_response = requests.post(
        headers=config.headers,
        url=f"{base_url}/collections/products/records?project_id={config.project_id}",
        json={
            "data": {
                "name": "EndToEnd_Test Headphones",
                "price": 49.99,
                "category": "Electronics",
                "in_stock": True
            }
        }
    )
    create_body = create_response.json()
    print("Create Response:", create_body)
    assert create_response.status_code == 201
    new_record_id = create_body["data"]["id"]

    # Step 2: Get the newly created record
    get_response = requests.get(
        url=f"{base_url}/collections/products/records/{new_record_id}",
        headers=config.headers,
    )
    get_body = get_response.json()
    print("Get Response:", get_body)
    assert get_response.status_code == 200
    assert get_body["data"]["id"] == new_record_id

    # Step 3: Update the newly created record
    update_response = requests.put(
        f'{base_url}/collections/products/records/{new_record_id}?project_id={config.project_id}',
        headers=config.headers, json={
            "data": {
                "name": "EndToEnd_Test Headphones Updated",
                "price": 59.99,
                "category": "Electronics",
                "in_stock": False
            }}
    )
    update_body = update_response.json()
    print("Update Response:", update_body)
    assert update_response.status_code == 200
    assert update_body["data"]["data"]["price"] == 59.99
    assert update_body["data"]["data"]["name"] == "EndToEnd_Test Headphones Updated"
