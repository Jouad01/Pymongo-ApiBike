# La key api de la base de datos Bicycle

import requests
import json

# FindOne = for search all the data of one document
# Find = for search all the data of all documents
# Aggregate = for search all the data of all documents with a filter (use pipeline)

url = "https://data.mongodb-api.com/app/data-ezbvq/endpoint/data/v1/action/aggregate?pretty=true"


payload = json.dumps({
    "collection": "Bicycle",
    "database": "BaleaBykes",
    "dataSource": "Sandbox01",
    # "projection": {
    # },
    # this query is for search all data with id and booking
    "pipeline": [
        {
            "$group": {
                "_id": "$_id",
                "total": {
                    "$sum": "$booking"
                }
            }
        }
    ]
})

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '7LebTujGs1Je3pwL9lHtejH7khTuCboQ7iUs7IPx8CqwTV2LsQGjeV7unUThumMd', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
