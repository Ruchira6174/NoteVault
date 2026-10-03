import uuid
import pytest

def test_resource_lifecycle(client):
    # 1. Register
    unique_suffix = str(uuid.uuid4())[:8]
    register_data = {
        "full_name": "Test User",
        "username": f"testuser_{unique_suffix}",
        "email": f"testuser_{unique_suffix}@example.com",
        "password": "testpassword123",
        "college": "Test College",
        "branch": "Computer Science",
        "semester": 5,
        "bio": "Test bio"
    }

    reg_response = client.post("/api/v1/auth/register", json=register_data)
    assert reg_response.status_code == 201, f"Registration failed: {reg_response.text}"
    
    # 2. Login
    login_data = {
        "username": register_data["email"],
        "password": register_data["password"]
    }
    
    login_response = client.post("/api/v1/auth/login", data=login_data)
    assert login_response.status_code == 200, f"Login failed: {login_response.text}"
    
    tokens = login_response.json()
    assert "access_token" in tokens
    
    headers = {
        "Authorization": f"Bearer {tokens['access_token']}"
    }

    # 3. Create Resource
    resource_data = {
        "title": "Quantum Computing Fundamentals",
        "description": "Automated integration test resource",
        "subject": "Quantum Computing",
        "university": "Test University",
        "course": "BTech",
        "branch": "Data Science",
        "semester": 1,
        "tags": ["quantum", "computing", "test"],
        "visibility": "PRIVATE",
        "is_paid": False,
        "price": "0.00",
        "currency": "USD"
    }
    
    create_res = client.post("/api/v1/resources", json=resource_data, headers=headers)
    assert create_res.status_code == 201, f"Create resource failed: {create_res.text}"
    created_resource = create_res.json()
    assert "id" in created_resource
    assert created_resource["title"] == "Quantum Computing Fundamentals"
    assert created_resource["visibility"] == "PRIVATE"
    resource_id = created_resource["id"]
    
    # 4. Get My Resources
    my_res_resp = client.get("/api/v1/resources/me", headers=headers)
    assert my_res_resp.status_code == 200, f"Get my resources failed: {my_res_resp.text}"
    
    resources_list = my_res_resp.json()
    assert any(r["id"] == resource_id for r in resources_list), "Resource not found in my resources"
    
    # 5. Get Resource
    get_res_resp = client.get(f"/api/v1/resources/{resource_id}", headers=headers)
    assert get_res_resp.status_code == 200, f"Get resource failed: {get_res_resp.text}"
    fetched_res = get_res_resp.json()
    assert fetched_res["id"] == resource_id
    assert fetched_res["title"] == "Quantum Computing Fundamentals"
    
    # 6. Update Resource
    update_data = {
        "title": "Quantum Computing Advanced",
        "description": "Updated automated test description",
        "tags": ["quantum", "computing", "advanced"]
    }
    
    update_res_resp = client.patch(f"/api/v1/resources/{resource_id}", json=update_data, headers=headers)
    assert update_res_resp.status_code == 200, f"Update resource failed: {update_res_resp.text}"
    updated_res = update_res_resp.json()
    assert updated_res["title"] == "Quantum Computing Advanced"
    assert updated_res["description"] == "Updated automated test description"
    assert "advanced" in updated_res["tags"]
    
    # 7. Publish
    publish_data = {"publish": True}
    pub_res_resp = client.patch(f"/api/v1/resources/{resource_id}/publish", json=publish_data, headers=headers)
    assert pub_res_resp.status_code == 200, f"Publish resource failed: {pub_res_resp.text}"
    pub_res = pub_res_resp.json()
    assert pub_res["visibility"] == "PUBLIC"
    
    # 8. Verify Published Resource
    get_pub_res_resp = client.get(f"/api/v1/resources/{resource_id}", headers=headers)
    assert get_pub_res_resp.status_code == 200
    assert get_pub_res_resp.json()["visibility"] == "PUBLIC"
    
    # 9. Unpublish
    unpublish_data = {"publish": False}
    unpub_res_resp = client.patch(f"/api/v1/resources/{resource_id}/publish", json=unpublish_data, headers=headers)
    assert unpub_res_resp.status_code == 200, f"Unpublish resource failed: {unpub_res_resp.text}"
    unpub_res = unpub_res_resp.json()
    assert unpub_res["visibility"] == "PRIVATE"
    
    # 10. Delete
    del_res_resp = client.delete(f"/api/v1/resources/{resource_id}", headers=headers)
    assert del_res_resp.status_code == 204, f"Delete resource failed: {del_res_resp.text}"
    
    # 11. Verify Deletion
    get_del_res_resp = client.get(f"/api/v1/resources/{resource_id}", headers=headers)
    assert get_del_res_resp.status_code == 404, f"Resource still exists after deletion: {get_del_res_resp.text}"
