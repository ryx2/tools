import os
import scipy.misc
import tensorflow as tf
import argparse

def save_images_from_event(fn, output_dir):
    assert(os.path.isdir(output_dir))

    image_str = tf.placeholder(tf.string)
    im_tf = tf.image.decode_image(image_str)

    sess = tf.InteractiveSession()
    with sess.as_default():
        num_events=0
        for e in tf.train.summary_iterator(fn):
            for v in e.summary.value:
                if v.HasField('image'):
                    num_events+=1
        count = 0
        event_num = 0
        for e in tf.train.summary_iterator(fn):
            for v in e.summary.value:
                if v.HasField('image'):
                    import ipdb; ipdb.set_trace()
                    if event_num >= num_events - 100:
                        im = im_tf.eval({image_str: v.image.encoded_image_string})
                        output_fn = os.path.realpath('{}/image_{:05d}.png'.format(output_dir, count))
                        print("Saving '{}'".format(output_fn))
                        scipy.misc.imsave(output_fn, im)
                        count += 1
                    else:
                        event_num +=1
                        continue
def main():
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("event", help="path to event")
    parser.add_argument("save_loc", help="save directory")
    args = parser.parse_args()
    save_images_from_event(args.event, args.save_loc)

if __name__ == '__main__':
    main()
