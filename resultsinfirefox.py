import json
import argparse
import webbrowser
import time

parser = argparse.ArgumentParser(description='Virus total results display')
parser.add_argument("-r", "--results", type=str, help="Result File Name")
args = parser.parse_args()

results_json_file = open("./results/" + args.results + ".json", "r")
results_json = json.loads(results_json_file.read())
for result in results_json[args.results]:
    webbrowser.get('firefox').open_new_tab(result["permalink"])
    time.sleep(5)
