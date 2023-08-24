# VirusTotal Scanner

This is a simple tool to scan files using the VirusTotal API v3.

## Usage

1. **Get Your VirusTotal API Key**

   Before using this tool, you need to obtain a VirusTotal API key. You can sign up for a VirusTotal account and create an API key from their website.

2. **Add Your API Key**

   Once you have the API key, add it to the `apikey.json` file in the following format:

   ```json
   {
       "apikey": "YOUR_API_KEY_HERE"
   }
   ```

3. **Scanning Files**

   To scan files in a directory, use the following command:

   ```shell
   python3 vtapi3.py -d /directory_to_be_scanned -o /results_directory
   ```

   Replace `/directory_to_be_scanned` with the path of the directory containing the files you want to scan. Replace `/results_directory` with the desired output directory for the scan results.

4. **Viewing Results in Firefox**

   If you prefer to view the results in the Firefox browser, you can use the following command:

   ```shell
   python3 resultsinfirefox.py -r result.json
   ```

   Replace `result.json` with the path to the JSON file containing the scan results.

Feel free to customize and adapt the tool to your needs! If you encounter any issues or have questions, please refer to the official VirusTotal API documentation or seek help from the community.
