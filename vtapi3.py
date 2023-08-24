import os
import argparse
import requests
import json
import sys

API_KEY_FILE = "./apikey.json"
API_URL = "https://www.virustotal.com/api/v3/files"

def main():
    parser = argparse.ArgumentParser(description='VirusTotal scanner')
    parser.add_argument("-d", "--directory", type=str, help="Specify directory containing the files to be scanned")
    parser.add_argument("-o", "--output", type=str, help="Output file")
    args = parser.parse_args()

    if not args.directory:
        sys.exit("Please specify a directory location to be scanned to proceed")
    if not args.output:
        sys.exit("Please specify an output file name to proceed")

    api_key = get_api_key(API_KEY_FILE)

    directory = args.directory.rstrip('/') + '/'
    dir_list = os.listdir(directory)

    scan_results = {}

    for filename in dir_list:
        file_path = os.path.join(directory, filename)
        scan_result = scan_file(file_path, api_key)
        scan_results[filename] = scan_result

    output_file_path = f"./results/{args.output}.json"
    with open(output_file_path, 'w') as outfile:
        json.dump(scan_results, outfile, indent=2)

def get_api_key(api_key_file):
    with open(api_key_file, 'r') as api_file:
        api_json = json.load(api_file)
        return api_json["apikey"]

def scan_file(file_path, api_key):
    with open(file_path, 'rb') as file_content:
        headers = {
            "x-apikey": api_key
        }
        response = requests.post(API_URL, headers=headers, files={"file": file_content})
        return response.json()

if __name__ == "__main__":
    main()
