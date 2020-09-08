import numpy as np
import sys
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(
         description="terminal view a numpy file or image as np array")
parser.add_argument(
         "data",
         help=".npy file to be viewed or im.")
parser.add_argument(
         "--img", action='store_true',
         help="if an image.")
args = parser.parse_args()

if args.img:
    import imageio
    data = imageio.imread(args.data)
else:
    try:
        data = np.load(args.data)
    except Exception as e:
        print(e)
        print('trying genfromtxt instead')
        data = np.genfromtxt(args.data)
import ipdb; ipdb.set_trace()
