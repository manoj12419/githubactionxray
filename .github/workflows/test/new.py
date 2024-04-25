import argparse
import requests
import json

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
    headers_authenticate = {"Content-Type": "application/json"}
    data = {
        'client_id':args.client_id,
        'client_secret': args.client_secret,
        'grant_type' : 'client_credentials'
    }
    request= requests.post(url,data=data)
    print(request)
    print(request.text)

    # response_authenticate = requests.post(uri_authenticate, headers=headers_authenticate, data=data)
 
    # print(f"MN 2 Authorization: Bearer {response_authenticate.text}")
    # print(f"MN 1 Authorization: Bearer {response_authenticate}")
    # print(response_authenticate.text)
    # # Assuming the response is a plain string
    # #uri_import_execution = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    
    # uri_import_execution = "https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey=YAK-4"
    # headers_import_execution = {
    #     "Authorization": f"Bearer {response_authenticate.text}",
    #     "Content-Type": "application/xml",
    # }

    # response_import_execution = requests.post(uri_import_execution, headers=headers_import_execution, files=args.file_path)
    # print(response_import_execution.text)  # Print API response for debugging
    # #response_import_execution.raise_for_status()  # Keep this line to raise HTTPError if response status is not successful

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
