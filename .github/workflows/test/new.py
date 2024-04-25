import argparse
import requests
import json
import os

def authenticate(client_id, client_secret):
    uri = "https://xray.cloud.getxray.app/api/v1/authenticate"
    headers = {"Content-Type": "application/json"}
    body = json.dumps({"client_id": client_id, "client_secret": client_secret})

    response = requests.post(uri, headers=headers, data=body)
    response.raise_for_status()
    print("Authentication response:")
    print(response.text)
    return response.text  # Assuming the response is a plain string

def import_execution_junit(token, test_id, file_path):
    uri = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={test_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/xml",
    }

    with open(file_path, "rb") as file:
        try:
            response = requests.post(uri, headers=headers, files={"file": file})
            response.raise_for_status()
            print("Import successful.")
            print(response.text)  # Print API response for debugging
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            print(f"Response content: {e.response.text}")  # Print response content for debugging


def main():
    parser = argparse.ArgumentParser(description="Upload JUnit results to Xray.")
    parser.add_argument("client_id", help="Xray client ID")
    parser.add_argument("client_secret", help="Xray client secret")
    parser.add_argument("file_path", help="Path to the JUnit results XML file")
    parser.add_argument("test_id", help="Test ID or test plan key")
    args = parser.parse_args()

    print(f"Test ID or test plan key: {args.test_id}")
    print(f"Client ID: {args.client_id}")
    print(f"Client secret: {args.client_secret}")
    print(f"File path: {args.file_path}")
    if not os.path.exists(args.file_path):
        print(f"Error: File '{args.file_path}' does not exist.")
        return
    token = authenticate(args.client_id, args.client_secret)
    if token:
        import_execution_junit(token, args.test_id, args.file_path)
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()
