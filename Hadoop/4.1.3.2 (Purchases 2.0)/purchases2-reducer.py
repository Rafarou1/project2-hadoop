#!/usr/bin/python2
import sys

oldKey = None
sales_total = 0.0

for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) != 2:
    continue

  thisKey, thisSale = data

  if oldKey and oldKey != thisKey:
    print '{0}\t{1}'.format(oldKey, sales_total)
    # Reset the total for the new key
    sales_total = 0.0

  oldKey = thisKey
  try:
    sales_total += float(thisSale)
  except ValueError:
    continue

if oldKey is not None:
  print '{0}\t{1}'.format(oldKey, sales_total)
EOF