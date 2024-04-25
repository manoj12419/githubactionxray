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
  
    url = 'https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey=YAK-4'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/xml'
    }

    #file_path = '/C:/Cypress-xray-integration/githubactionxray/cypress/results/junit/results.xml'
    with open(file_content, 'rb') as file:
        data = file.read()

    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    print(response.status_code)
    print(response.text)
# try:
#     # Make the request with authentication
#         response = requests.post(uri, headers=headers, data=file_content)
#         response.raise_for_status()
#         print("Import done.")
#         print(response)
#     except requests.exceptions.HTTPError as e:
#         if e.response.status_code == 401:
#             print("Authentication failed. Check your authentication token.")
#         else:
#             print(f"HTTP error occurred: {e}")

    
client_id, client_secret, file_content, test_id, test_exec_id = sys.argv[1:]

print(f"Testplan id: {test_id}")
print(f"Test exec id: {test_exec_id}")
print(f"Received client_id: {client_id}")
print(f"Received client_secret: {client_secret}")
print(f"Received file content: {file_content}")

token = authenticate(client_id, client_secret)
print("token = authenticate(client_id, client_secret)")
import_execution_junit(token, test_id, file_content)
