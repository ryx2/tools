import ipdb
import numpy as np
import csv
import argparse

parser = argparse.ArgumentParser(
         description="auto image annotation given camera gps and target gps")
parser.add_argument(
         "data",
         help="csv of object to be edited.")
parser.add_argument(
         "remove",
         help="csv of invalid annos.")
parser.add_argument(
         "out",
         help="output annos.")
args = parser.parse_args()
data = np.array(list(csv.reader(open(
    args.data))))
remove = np.array(list(csv.reader(open(
    args.remove
    ))))

#import ipdb; ipdb.set_trace()
rd = {}
datar = []
for thing in remove:
    datar.append(thing)
    if type(thing) == type([]) or len(thing) > 1:
        thing = thing[0]
    thing = thing[thing.rfind('/')+1:-4]
    rd[thing] = True
for i in range(len(data)):
    name = data[i][0]
    if name[name.rfind('/') + 1:-4] not in rd:
        datar.append(data[i])
csv.writer(
    open(
        args.out,
        'w')).writerows(datar)
