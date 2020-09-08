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
parser.add_argument(
         "--all", action='store_true',
         help="take annos from all when matched.")
args = parser.parse_args()

data = np.array(list(csv.reader(open(
    args.data))))
remove = np.array(list(csv.reader(open(
    args.remove
    ))))

#import ipdb; ipdb.set_trace()
# if len(remove.shape) > 1:
#     remove = remove[:, 0]
rd = {}
datar = []
for thing in remove:
    full= np.copy(thing)
    if type(thing) == type([]) or len(thing) > 1:
        thing = thing[0]
    thing = thing[thing.rfind('/')+1:-4]
    if thing not in rd:
        rd[thing] = [False, [full]] #bool for if its been added yet, list of annos on the same im
    else:
        rd[thing][1].append(full)

for i in range(len(data)):
    name = data[i][0]
    if name[name.rfind('/') + 1:-4] in rd:
        datar.append(data[i])
        value = rd[name[name.rfind('/') + 1:-4]]
        if not value[0]:
            for anno in value[1]:
                datar.append(anno)
        rd[name[name.rfind('/') + 1:-4]][0] = True
csv.writer(
    open(
        args.out,
        'w')).writerows(datar)
