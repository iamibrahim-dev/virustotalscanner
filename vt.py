import requests
import os
import argparse
import json
import sys

parser = argparse.ArgumentParser(description='Virus total scanner')
parser.add_argument("-d", "--directory", type=str, help="Specify directory containing the files to be scanned")
parser.add_argument("-o", "--output", type=str, help="Output file")
args = parser.parse_args()

args_error_code = 0
if args.directory is None:
    args_error_code = 1
elif args.output is None:
    args_error_code = args_error_code + 2

if args_error_code == 1:
    sys.exit("Please specify directory location to be scanned to proceed")
elif args_error_code == 2:
    sys.exit("Please specify output file name to proceed")

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
api_file = open("./apikey.json", 'r')
api_json = json.loads(api_file.readline())
params = {'apikey': api_json["apikey"]}
directory = ""
response_json = {args.output: []}

if args.directory[len(args.directory)-1] != "/":
    directory = args.directory + '/'
else:
    directory = args.directory

dir_list = os.listdir(directory)

for file in dir_list:
    files = {'file': (directory+file, open(directory+file, 'rb'))}
    response = requests.post(url, files=files, params=params)
    print(response.json())
    response_json[args.output].append(response.json())

with open(str("./results/" + args.output + ".json"), 'w') as outfile:
    json.dump(response_json, outfile)
