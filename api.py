import json
import requests

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'

# Define cycle and committee ID, for organization purposes
cycle = '2018'
committee_id = 'C00501197' # Beto

# Create URL
url = "https://api.propublica.org/campaign-finance/v1/" + cycle + '/committees/' + committee_id + ".json"

# Make request and get JSON response
response = requests.get(url, headers={"X-API-Key": API_KEY}).content

# Turn JSON data into Python objects
data = json.loads(response)

# Dig through data to get specific items, using dictionary and list lookup tools
print data['results'][0]['total_receipts']