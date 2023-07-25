#!/bin/env python3
import json
import re
import operator

with open('entries.json') as json_data:
    json_obj = json.load(json_data)

filename_for_url = {}

assets = json_obj['assets']
for item in assets:
    # url = item['url-4K-SDR']
    url = item['url-4K-HDR']
    filename = "%s" % (item['accessibilityLabel'])

    m = re.match('.*/(.+)',url)
    if m:
        base_filename = m.group(1)

    filename = filename + " " + base_filename
    filename_for_url[url] = filename

file = open('urls.txt', "w")
for x in sorted(filename_for_url.items(), key=operator.itemgetter(1)):
    out_str = "%s,%s" % (x[0],x[1])
    file.write(out_str + "\n")
file.close()

file = open('urls_aria.txt', "w")
for x in sorted(filename_for_url.items(), key=operator.itemgetter(1)):
    out_str = "%s\n out=%s" % (x[0],x[1])
    file.write(out_str + "\n")
file.close()

file = open('filenames.txt',"w")
for x in sorted(filename_for_url.items(), key=operator.itemgetter(1)):
    out_str = "%s" % (x[1])
    file.write(out_str + "\n")
file.close()
