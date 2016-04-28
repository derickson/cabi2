#compute-predict.py


import csv
import json
import sys
import moment

from elasticsearch import helpers
from elasticsearch import Elasticsearch

import Geohash



es = Elasticsearch("localhost:9201")



def prettyPrint(doc):
	print json.dumps(doc, indent=4, sort_keys=True)

writeBatchSize = 5000
fromIndex = "bike-dc"
toIndex = 'bike-dc_predict'
fromType = "logs"
toType = "logs"

es.indices.delete(index=toIndex, ignore=[400, 404])

# .es(index=bike-dc, timefield=startDate, q="startStation:'Lincoln Memorial'").label(actual).bars().color(#ddddFF), .es(index=bike-dc_predict, metric="max:the_movingavg").label("simple moving average"),.es(index=bike-dc_predict, metric="max:the_holtwinters").label("holt winters prediction").color(black)

# .es(index=bike-dc, timefield=startDate).label(actual).bars().color(#ddddFF),  .es(index=bike-dc_predict, metric="max:the_movingavg").label("simple moving average"),.es(index=bike-dc_predict, metric="max:the_holtwinters").label("holt winters prediction").color(black)

day = 24


body = {
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "startDate": {
              "gte": "2014-04-01",
              "lte": "2014-07-30"
            }
          }
        }
      ]
    } 
  }, 
  "aggs": {
    "hist": {
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
        "holt1": {
          "moving_avg": {
            "buckets_path": "the_count",
            "window": day * 7 * 4,
            "model": "holt_winters",
            # "predict": 48,
            "minimize": True,
            "settings": {
              "type": "mult",
              "period": day * 7,
              # "alpha": 0.1,
              # "beta": 0.8,
              # "gamma": 0.8,
	          "pad": True
            }
          }
        },
        "holt2": {
          "moving_avg": {
            "buckets_path": "the_count",
            "window": day * 7 * 4,
            "model": "holt_winters",
            # "predict": 48,
            # "minimize": True,
            "settings": {
              "type": "mult",
              "period": day * 7,
              "alpha": 0.8,
              "beta": 0.1,
              "gamma": 0.8,
	          "pad": True
            }
          }
        },
        "holt3": {
          "moving_avg": {
            "buckets_path": "the_count",
            "window": day * 7 * 4,
            "model": "holt_winters",
            # "predict": 48,
            # "minimize": True,
            "settings": {
              "type": "mult",
              "period": day * 7,
              "alpha": 0.8,
              "beta": 0.8,
              "gamma": 0.1,
	          "pad": True
            }
          }
        }
      }
    }
  }
}




res = es.search(index=fromIndex, search_type="count",body=body)
buckets = res["aggregations"]["hist"]["buckets"]

# prettyPrint(buckets)

bulkActions = []
for bucket in buckets:
	m = moment.unix(bucket['key']).date ##.add(hours=4).date
	doc = {
		"@timestamp": bucket['key_as_string']
	}
	if("the_count" in bucket):
		doc["the_count"] = bucket["the_count"]["value"]
	if("holt1" in bucket):
		doc["holt1"] = bucket["holt1"]["value"]
	if("holt2" in bucket):
		doc["holt2"] = bucket["holt2"]["value"]
	if("holt3" in bucket):
		doc["holt3"] = bucket["holt3"]["value"]

	if( "the_count" in doc and "holt1" in doc and (doc["the_count"] > doc["holt1"] * 1.4)):
		doc["surprise1"] = doc["the_count"]
	if( "the_count" in doc and "holt2" in doc and (doc["the_count"] > doc["holt2"] * 1.4)):
		doc["surprise2"] = doc["the_count"]
	if( "the_count" in doc and "holt3" in doc and (doc["the_count"] > doc["holt3"] * 1.4)):
		doc["surprise3"] = doc["the_count"]
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
