import sys
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
print('initializing tensorflow with CPU ONLY...')
sys.stdout.flush()
os.environ["CUDA_VISIBLE_DEVICES"] = ""
