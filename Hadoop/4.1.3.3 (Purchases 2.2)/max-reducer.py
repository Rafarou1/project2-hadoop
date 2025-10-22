#!/usr/bin/python2
import sys

oldKey = None
max_sale = 0.0

for line in sys.stdin:
  data = line.strip().split("\t")
  if len(data) != 2:
    continue

  thisKey, thisSale = data
  try:
    thisSale = float(thisSale)
  except ValueError:
    continue

  if oldKey and oldKey != thisKey:
    print '{0}\t{1}'.format(oldKey, max_sale)
    max_sale = thisSale
  else:
    if thisSale > max_sale:
      max_sale = thisSale

  if not oldKey:
      max_sale = thisSale
  
  oldKey = thisKey

if oldKey is not None:
  print '{0}\t{1}'.format(oldKey, max_sale)
EOF