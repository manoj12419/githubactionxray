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

def authenticate_xray(client_id, client_secret):
    auth_url = "https://xray.cloud.getxray.app/api/v1/authenticate"
    auth_data = {
        'client_id': client_id,
        'client_secret': client_secret
    }
    auth_response = requests.post(auth_url, data=auth_data)
    return auth_response

def upload_junit_results(args):
    url = "https://xray.cloud.getxray.app/api/v1/authenticate"

    payload = json.dumps({
        "client_id": "C2DDC03EB801485E93A8A1BBF29A60F8",
        "client_secret": "f25bc582a1c9a41875413da9a083f5ff082bb241f446780cc705636dbb5feb8c"
            })
    headers = {
         'Content-Type': 'application/json'
        }

    response1 = requests.request("POST", url, headers=headers, data=payload)

    print(response1.text)

    url = "https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK"

   
    headers = {
     'Authorization': 'Bearer '+response1.text,
     'Content-Type': 'application/xml'
        }
    with open(args.file_path, 'rb') as file:
        xml_data = file.read()
    print('file')
    print(xml_data)
    response2 = requests.request("POST", url, headers=headers, data=xml_data)
    
    print(response2.text)

    print(f"Test ID or test plan key: {args.test_id}")
    print(f"Client ID: {args.client_id}")
    print(f"Client secret: {args.client_secret}")
    print(f"File path: {args.file_path}")

    auth_response = authenticate_xray(args.client_id, args.client_secret)
    print(auth_response.status_code)
    auth_token = auth_response.headers.get('Authorization')
    print("Auth Token:", auth_token)
    print(f"Authorization token: {auth_response.text}")
    bearertoken="Bearer "+response1.text
    print("My bearer token "+bearertoken)
    num_chars = len(auth_response.text)
    print('nO OF CHAR')
    print(num_chars)
    import_url = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    headers = {
        "Authorization": bearertoken,
        "Content-Type": "application/xml",
    }
    print(headers)
    with open(args.file_path, 'rb') as file:
        xml_data = file.read()
    response = requests.post(import_url, headers=headers, data=xml_data)
    print(response.text)

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
