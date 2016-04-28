#compute-predict.py


import csv
import json
import sys
import moment

from elasticsearch import helpers
from elasticsearch import Elasticsearch

import Geohash


# print 'Geohash for 42.6, -5.6:', Geohash.encode(42.6, -5.6)
# print 'Coordinate for Geohash ezs42:', Geohash.decode('ezs42')
# print 'Exact coordinate for Geohash ezs42:\n', Geohash.decode_exactly('ezs42')


es = Elasticsearch("localhost:9201")



def prettyPrint(doc):
	print json.dumps(doc, indent=4, sort_keys=True)

writeBatchSize = 5000
fromIndex = "bike-dc"
toIndex = 'bike-dc_geopredict'
fromType = "logs"
toType = "logs"

es.indices.delete(index=toIndex, ignore=[400, 404])

# .es(index=bike-dc, timefield=startDate, q="startStation:'Lincoln Memorial'").label(actual).bars().color(#ddddFF), .es(index=bike-dc_predict, metric="max:the_movingavg").label("simple moving average"),.es(index=bike-dc_predict, metric="max:the_holtwinters").label("holt winters prediction").color(black)

# .es(index=bike-dc, timefield=startDate).label(actual).bars().color(#ddddFF),  .es(index=bike-dc_predict, metric="max:the_movingavg").label("simple moving average"),.es(index=bike-dc_predict, metric="max:the_holtwinters").label("holt winters prediction").color(black)


body = {
  # "query": {
  #   "bool": {
  #     "must": [
  #       {
  #         "range": {
  #           "startDate": {
  #             "gte": "2013-06-01",
  #             "lte": "2014-08-01"
  #           }
  #         }
  #       }
  #     ]
  #   } 
  # }, 
  "aggs": {
    "mygrid": {
      "geohash_grid": {
        "field": "startLocation",
        "precision": 7
      },
      "aggs": {
        "ingridhist": {
          "date_histogram": {
            "field": "startDate",
            "interval": "hour"
          },
          "aggs": {
            "the_count": {
              "value_count": {
                "field": "memberType"
              }
            },
            "prediction": {
              "moving_avg": {
                "buckets_path": "the_count",
                "window": 672,
                "model": "holt_winters",
                "minimize": True,
                "settings": {
                  "type": "mult",
                  "period": 168,
                  "pad": True
                }
              }  
            }
          }
        }
      }
    }
  }
}

res = es.search(index=fromIndex, search_type="count",body=body, request_timeout=3600)
buckets = res["aggregations"]["mygrid"]["buckets"]

# prettyPrint(buckets)

bulkActions = []
for geobucket in buckets:
	geo = Geohash.decode_exactly(geobucket['key'])
	print geobucket['key'], geo[0], geo[1]
	for bucket in geobucket['ingridhist']['buckets']:
		m = moment.unix(bucket['key']).date ##.add(hours=4).date
		doc = {
			"@timestamp": bucket['key_as_string'],
			"startLocation": [geo[1], geo[0]]
		}
		if("the_count" in bucket):
			doc["the_count"] = bucket["the_count"]["value"]
		if("prediction" in bucket):
			doc["prediction"] = bucket["prediction"]["value"]
		if('prediction' in doc and 'the_count' in doc):
			doc['surprise'] = max(0, 10.0 * (doc["the_count"] - doc["prediction"]) / doc["prediction"])
		action = {
			"_index": toIndex,
			"_type": toType,
			"_source": doc
		}

		bulkActions.append( action )
		if(len(bulkActions) >= writeBatchSize ):
			helpers.bulk( es,  bulkActions )
			bulkActions = []

if(len(bulkActions) > 0):
    helpers.bulk( es,  bulkActions )
    bulkItems = []
