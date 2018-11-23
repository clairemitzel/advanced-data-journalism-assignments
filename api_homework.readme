1. What URL would you use to get a list of the the most recent votes in the House?
https://api.propublica.org/congress/v1/house/votes/recent.json


2. How about to get a list of all members of Congress from Missouri?
'https://api.propublica.org/congress/v1/members/both/mo/current.json' and GET https://api.propublica.org/congress/v1/members/house/mo/{district}/current.json

3. The New York Times used a version of this API to do this interactive about the sequence of votes leading up to the confirmation of Neil Gorsuch to the Supreme Court. How would you use the API to get the information about these votes? Hint: The votes were on April 6/7, 2017.

Several searches would need to be done. First, you can search the date the vote took place to look at the final numbers('https://api.propublica.org/congress/v1/both/votes/2017-04-06/2017-04-07.json'). You can also search by roll call ('https://api.propublica.org/congress/v1/115/{chamber}/sessions/1/votes/111.json). Senate nominations can also be looked at to find info on how members voted ('https://api.propublica.org/congress/v1/115/nominations.json').

4. In this response, which details all members leaving office, how would you get the first and last name of the first result in the list? (Hint: Use dictionary and list lookup syntax ...)

import json
import requests

API_KEY = 'OylOqGPorg2UjpgDMgoGnVtRBKDhcNn7q6XF0rVb'

url = 'https://api.propublica.org/congress/v1/115/house/members/leaving.json'

response = requests.get(url, headers={"X-API-Key": API_KEY}).content

data = json.loads(response)

print data['results'][0]['members'][0]['first_name'], data['results'][0]['members'][0]['last_name']