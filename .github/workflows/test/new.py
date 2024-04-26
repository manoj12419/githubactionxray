import argparse
import requests
import xmltodict

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

    url = "https://xray.cloud.getxray.app/api/v1/authenticate"
    data = {
        'client_id': args.client_id,
        'client_secret': args.client_secret,
        'grant_type': 'client_credentials'
    }
    request = requests.post(url, data=data)
   
    print(f"Authorization token: {request.text}")

    header = {
        "Authorization": f"Bearer {request.text}",
        "Content-Type": "application/xml",
    }

    url_import_execution = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    print(url_import_execution)
    with open(args.file_path, 'rb') as file:
        xml_data = file.read()
        response = requests.post(url, headers=header, data=xml_data)
        print(response)
        print(response.text)
    # with open(args.file_path, 'rb') as file:
    #     xml_data = xmltodict.parse(file)
    #     response_import_execution = requests.post(url_import_execution, headers=header, data=xml_data)
    #     print(response_import_execution.text)

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
