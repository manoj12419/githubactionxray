import argparse
import requests
import json
import xmltodict
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Upload JUnit results to Xray.")
    parser.add_argument("client_id", help="Xray client ID")
    parser.add_argument("client_secret", help="Xray client secret")
    parser.add_argument("file_path", help="Path to the JUnit results XML file")
    parser.add_argument("test_id", help="Test ID or test plan key")
    return parser.parse_args()

def convert_xml_to_json(xml_file):
    with open(xml_file, 'r') as f:
        xml_data = f.read()
        json_data = xmltodict.parse(xml_data)
        with open('results.json', 'w') as json_file:
            json.dump(json_data, json_file)

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
    print(request)
    print(request.text)
    header = {
        "Authorization": f"Bearer {request.text}",
        "Content-Type": "application/xml",
    }

    convert_xml_to_json(args.file_path)  # Convert XML to JSON
    files = {'file': open('results.json', 'rb')}  # Use the JSON file for upload
    url_import_execution = f"https://xray.cloud.getxray.app/api/v1/import/execution/junit?projectKey=YAK&testPlanKey={args.test_id}"
    response_import_execution = requests.post(url_import_execution, headers=header, files=files)
    print(response_import_execution.text)

if __name__ == "__main__":
    args = parse_args()
    upload_junit_results(args)
