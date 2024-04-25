import argparse
import os
import requests
import json

def upload_junit_results():
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

    uri_authenticate = "https://xray.cloud.getxray.app/api/v1/authenticate"
    headers_authenticate = {"Content-Type": "application/json"}
    body_authenticate = json.dumps({"client_id": args.client_id, "client_secret": args.client_secret})

    response_authenticate = requests.post(uri_authenticate, headers=headers_authenticate, data=body_authenticate)
    response_authenticate.raise_for_status()
    print("Authentication response:")
    print(response_authenticate.text)
    token = response_authenticate.text  # Assuming the response is a plain string
    bT="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnQiOiI3MTc5OGI0YS1jNzdmLTM5NTctYjdhMC1kMjVlNmE3OWI0MDYiLCJhY2NvdW50SWQiOiI2M2I3NGI0NzZmMDY4ZWZlYzhmOGUxOWUiLCJpc1hlYSI6ZmFsc2UsImlhdCI6MTcxNDA4MzU1MiwiZXhwIjoxNzE0MTY5OTUyLCJhdWQiOiJDMkREQzAzRUI4MDE0ODVFOTNBOEExQkJGMjlBNjBGOCIsImlzcyI6ImNvbS54cGFuZGl0LnBsdWdpbnMueHJheSIsInN1YiI6IkMyRERDMDNFQjgwMTQ4NUU5M0E4QTFCQkYyOUE2MEY4In0.c4KrPOGbfPnSy59gCamekaNg8nEkLSfP0I5IkZEk9AY"
    #uri_import_execution = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    print(f"Authorization: Bearer {bT}")
    uri_import_execution = "https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey=YAK-4"
    headers_import_execution = {
        "Authorization": f"Bearer {bT}",
        "Content-Type": "application/xml",
    }

    response_import_execution = requests.post(uri_import_execution, headers=headers_import_execution, files=args.file_path)
    print(response_import_execution.text)  # Print API response for debugging
    response_import_execution.raise_for_status()  # Keep this line to raise HTTPError if response status is not successful

if __name__ == "__main__":
    upload_junit_results()
