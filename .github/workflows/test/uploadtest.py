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
    return response.text  # Assuming the response is a plain string

def import_execution_junit(token, test_id, file_content):
    uri = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={test_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml",
    }

    print("Import request:")
    print(f"URI: {uri}")
    print(f"Headers: {headers}")
    print("File content:")
    print(file_content)

    response = requests.post(uri, headers=headers, data=file_content)
    response.raise_for_status()
    print("Import successful.")
    print(response.text)  # Print API response for debugging

client_id, client_secret, file_content, test_id, test_exec_id = sys.argv[1:]

print(f"Testplan id: {test_id}")
print(f"Test exec id: {test_exec_id}")
print(f"Received client_id: {client_id}")
print(f"Received client_secret: {client_secret}")
print(f"Received file content: {file_content}")

token = authenticate(client_id, client_secret)
if token:
    import_execution_junit(token, test_id, file_content)
else:
    print("Authentication failed.")
