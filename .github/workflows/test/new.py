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

    # Step 1: Authenticate and get the token
    auth_url = "https://xray.cloud.getxray.app/api/v1/authenticate"
    auth_data = {
        'client_id': args.client_id,
        'client_secret': args.client_secret,
        'grant_type': 'client_credentials'
    }
    auth_response = requests.post(auth_url, data=auth_data)

    print(f"Authorization token: {auth_response.text}")

    # Step 2: Upload JUnit results using the obtained token
    import_url = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    headers = {
        "Authorization": f"Bearer {auth_response.text}",
        "Content-Type": "application/xml",
    }
    with open(args.file_path, 'rb') as file:
        xml_data = file.read()
        response = requests.post(import_url, headers=headers, data=xml_data)
        print(response.text)

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
