import csv
import json
import sys

csvfile = sys.argv[1]
csvfilename = csvfile.split('.')[0]
# A solution without requests module for sending POST requests
from urllib.parse import urlencode
from urllib.request import Request, urlopen

token = "<token>"
docId = "64a7e8b5109059c1be4e19bf"
api_url = "https://careers.turtl.co/api/v1/personalizations"

with open(csvfile, "r") as csvfile:
    with open(csvfilename + "-done.csv", "w") as csvdonefile:

        csvreader = csv.reader(csvfile, delimiter=",")
        csvwriter = csv.writer(csvdonefile, delimiter=",")
        next(csvreader)
        csvwriter.writerow(
            [
                "name",
                "company",
                "logo",
                "sector",
                "url",
                "cover",
                "animation",
                "twitter",
                "facebook",
            ]
        )
        for row in csvreader:
            body = {
                "docId": docId,
                "fields": {
                    "name": row[0],
                    "company": row[1],
                    "logo": row[2],
                    "sector": row[3],
                },
            }
            request = Request(
                api_url,
                json.dumps(body).encode('utf-8'),
                headers={
                    "Authorization": "Bearer " + token,
                    'Content-Type':'application/json'
                    },
            )
            response = urlopen(request).read().decode()
            response_dict = json.loads(response)
            csvwriter.writerow(
                [
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    response_dict["url"],
                    response_dict["assets"]["coverLocation"],
                    response_dict["assets"]["animationLocation"],
                    response_dict["assets"]["socialLocations"]["twitter"],
                    response_dict["assets"]["socialLocations"]["facebook"],
                ]
            )
