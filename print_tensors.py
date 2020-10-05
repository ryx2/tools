import tensorflow as tf

import sys


def printTensorsPb(pb_file):
    # read pb into graph_def
    with tf.gfile.GFile(pb_file, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # import graph_def
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def)

    # print operations
    for op in graph.get_operations():
        print(op.name)
        sys.stdout.flush()


def printTensorsCkpt(ckpt_file):
    from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
    print_tensors_in_checkpoint_file(ckpt_file,
                                     all_tensors=True,
                                     tensor_name='')


if sys.argv[1][-3:] == '.pb':
    printTensorsPb(sys.argv[1])
elif sys.argv[1][-5:] == '.ckpt':
    printTensorsCkpt(sys.argv[1])
else:
    print('needs to be a .pb or .ckpt file')
