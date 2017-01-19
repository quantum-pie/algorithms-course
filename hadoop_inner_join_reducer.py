# Hadoop streaming inner join reducer
from sys import stdin

tokens = input().strip().split('\t')
last_user_id = tokens[0]
source, query = tokens[1].split(':')
h_array = dict()
h_array.update({source: [query]})

for line in stdin:
    tokens = line.strip().split('\t')
    user_id = tokens[0]
    source, query = tokens[1].split(':')

    if user_id == last_user_id:
        if source in h_array.keys():
            h_array[source].append(query)
        else:
            h_array.update({source: [query]})
    else:
        if len(h_array.keys()) == 2:
            for q1 in h_array['query']:
                for q2 in h_array['url']:
                    print('{:s}\t{:s}\t{:s}'.format(last_user_id, q1, q2))
        h_array = dict()
        h_array.update({source: [query]})
        last_user_id = user_id

if len(h_array.keys()) == 2:
    for q1 in h_array['query']:
        for q2 in h_array['url']:
            print('{:s}\t{:s}\t{:s}'.format(user_id, q1, q2))
