import sys
import requests
import json

def authenticate(client_id, client_secret):
    uri = "https://xray.cloud.getxray.app/api/v1/authenticate"
    headers = {"Content-Type": "application/json"}
    body = json.dumps({"client_id": client_id, "client_secret": client_secret})

    try:
        response = requests.post(uri, headers=headers, data=body)
        response.raise_for_status()
        return response.text  # Assuming the response is a plain string
    except requests.exceptions.RequestException as e:
        print(f"Error during authentication: {e}")
        return None


def import_execution_junit(token, test_id, file_path):
    uri = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={test_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml",
    }

    try:
        with open(file_path, "rb") as file:
            response = requests.post(uri, headers=headers, files={"file": file})
            response.raise_for_status()
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error during import: {e}")

def main():
    if len(sys.argv) != 6:
        print("Usage: python uploadtest.py <client_id> <client_secret> <file_path> <test_id> <test_exec_id>")
        sys.exit(1)

    client_id, client_secret, file_path, test_id, test_exec_id = sys.argv[1:]

    print(f"Testplan id: {test_id}")
    print(f"Test exec id: {test_exec_id}")
    print(f"Received client_id: {client_id}")
    print(f"Received client_secret: {client_secret}")
    print(f"Received filePath: {file_path}")

    token = authenticate(client_id, client_secret)
    if token:
        import_execution_junit(token, test_id, file_path)
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
