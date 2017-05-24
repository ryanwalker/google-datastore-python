print 'Lets look at some data'
from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Card')
it = query.fetch()

count = 0

# Loop over every Card entity, stopping at last number divisible by 100
for card in it:
    print(card['appName'])
    count += 1
    if count == 10:
        break

# # Any remaining entities more than a number divisible by 100
# # (e.g. the last 26 of 926 total)
# if len(entitiesToSave) > 0:
#     # client.put_multi(entitiesToSave)
#     print('Saved the final cards: ')
#     print(len(entitiesToSave))
#
# print("Saved total: " + str(count))
