import argparse
import requests

def parse_args():
    parser = argparse.ArgumentParser(description="Upload JUnit results to Xray.")
    parser.add_argument("client_id", help="Xray client ID")
    parser.add_argument("client_secret", help="Xray client secret")
    parser.add_argument("file_path", help="Path to the JUnit results XML file")
    parser.add_argument("test_id", help="Test ID or test plan key")
    return parser.parse_args()

def upload_junit_results(args):
    print(f"Test ID or test plan key: {args.test_id}")
    print(f"Client ID: {args.client_id}")
    print(f"Client secret: {args.client_secret}")
    print(f"File path: {args.file_path}")

    url_authenticate = "https://xray.cloud.getxray.app/api/v1/authenticate"
    data = {
        'client_id': args.client_id,
        'client_secret': args.client_secret,
        'grant_type': 'client_credentials'
    }
    response_authenticate = requests.post(url_authenticate, data=data)

    access_token = response_authenticate.json()['access_token']
    print(f"Access token: {access_token}")

    url_import_execution = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/xml",
    }

    with open(args.file_path) as file:
        uploadresponse=requests.post(url_import_execution, headers=headers, data=file)

    print(uploadresponse.text)

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
