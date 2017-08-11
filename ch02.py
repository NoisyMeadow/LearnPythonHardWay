#! C:\\Python\\bin
# -*- coding:utf-8 -*-

import json
from collections import defaultdict

def get_counts(sequence):
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts

def get_counts2(sequence):
	counts = defaultdict(int) # values will initialize to 0
	for x in sequence:
		counts[x] += 1
	return counts

path = '../pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
print records[0]
print records[0]['tz']

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print time_zones[:10]

counts = get_counts( time_zones )
print counts

counts = get_counts2( time_zones )
print counts