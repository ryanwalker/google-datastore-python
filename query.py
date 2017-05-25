print 'Lets look at some data'
from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Card')
it = query.fetch()

query = client.query(kind='Card'
# query.add_filter('appName',  '=', 'mobpay1')

query.fetch(1)

for card in query.fetch(limit=1):
  print card['actualWaitTimeMinutes']
  print card


print query.project
