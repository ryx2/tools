import sys
import notebook_util
import os
lowest = notebook_util.pick_gpu_lowest_memory()
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"   # see issue #152
print('least used gpu is gpu ' + str(lowest) + ', utilizing this gpu...')
sys.stdout.flush()
os.environ["CUDA_VISIBLE_DEVICES"] = str(lowest)
