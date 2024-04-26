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

    # Read the XML file and remove the Unicode character \ufeff
    with open(args.file_path, 'r', encoding='utf-8') as file:
        xml_data = file.read().replace("\ufeff", "")

    url = "https://xray.cloud.getxray.app/api/v1/authenticate"
    data = {
        'client_id': args.client_id,
        'client_secret': args.client_secret,
        'grant_type': 'client_credentials'
    }
    response_authenticate = requests.post(url, data=data)
    print(response_authenticate)
    print(response_authenticate.text)
    
    header = {
        "Authorization": f"Bearer {response_authenticate.text}",
        "Content-Type": "application/xml",
    }

    url2 = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    request2 = requests.post(url2, headers=header, data=xml_data.encode('utf-8'))
    print(request2.text)

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
