import ipdb
import numpy as np
import csv
import argparse

parser = argparse.ArgumentParser(
    description="auto image annotation given camera gps and target gps")
parser.add_argument("data", help="csv of object to be edited.")
parser.add_argument("remove", help="csv of invalid annos.")
parser.add_argument("out", help="output annos.")
args = parser.parse_args()
# data = np.array(list(csv.reader(open(
#     args.data))))
data = np.genfromtxt(args.data, dtype='unicode', delimiter=",")
# remove = np.array(list(csv.reader(open(
#     args.remove
#     ))))
remove = np.genfromtxt(args.remove, dtype='unicode', delimiter=",")
# import ipdb; ipdb.set_trace()
if len(remove.shape) > 1:
    remove = remove[:, 0]
rd = {}
for thing in remove:
    thing = thing[thing.rfind('/') + 1:-4]
    rd[thing] = True
keepers = np.ones_like((data[:, 0])).astype(np.int) == 1
for i in range(len(data)):
    name = data[i, 0]
    if name[name.rfind('/') + 1:-4] in rd:
        keepers[i] = 0
datar = data[keepers]
csv.writer(open(args.out, 'w')).writerows(datar)
