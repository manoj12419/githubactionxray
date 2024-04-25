import sys
import requests
import json

def authenticate(client_id, client_secret):
    uri = "https://xray.cloud.getxray.app/api/v1/authenticate"
    headers = {"Content-Type": "application/json"}
    body = json.dumps({"client_id": client_id, "client_secret": client_secret})

    response = requests.post(uri, headers=headers, data=body)
    response.raise_for_status()
    print("Authentication response:")
    print(response.text)    
    return response.text

def import_execution_junit(token, test_id, file_path):
    print(f"Authorization: Bearer {token}")
    uri = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={test_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml",
    }
  
    with open(file_path, 'rb') as file:
        data = file.read()    
    response = requests.post(uri, headers=headers, data=data)
    print("Import response:")
    print(response.text)
    print("Status code:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python script.py <client_id> <client_secret> <file_path> <test_id> <test_exec_id>")
        sys.exit(1)

    client_id, client_secret, file_path, test_id, test_exec_id = sys.argv[1:]

    print(f"Test plan id: {test_id}")
    print(f"Test exec id: {test_exec_id}")
    print(f"Received client_id: {client_id}")
    print(f"Received client_secret: {client_secret}")
    print(f"Received file path: {file_path}")

    token = authenticate(client_id, client_secret)
    print(f"Authorization: Bearer {token}")
    import_execution_junit(token, test_id, file_path)
