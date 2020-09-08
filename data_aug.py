import tensorflow as tf
import random
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from skimage import exposure


def keras_pre(
        x_train,
        batch_size,
        zoom_range=0.2,
        shear_range=0.2,
        rotation_range=10,
        horizontal_flip=False,
        vertical_flip=False):

    def random_contrast_aug(im):
        im = exposure.rescale_intensity(im, out_range=(0, 1))
        amount = 2 ** ((random.random() - 0.5) * 4)  # 2** -2 to 2
        return exposure.adjust_gamma(im, amount)

    genargs = dict(
        # brightness_range=0.1,
        rotation_range=rotation_range,
        zoom_range=zoom_range,
        shear_range=shear_range,
        horizontal_flip=horizontal_flip,
        vertical_flip=vertical_flip,
        fill_mode='nearest',
        preprocessing_function=random_contrast_aug
    )

    xgen = ImageDataGenerator(**genargs)

    xgen.fit(x_train, augment=True, seed=0)
    xflow = xgen.flow(x_train, batch_size=batch_size, seed=0, shuffle=False)
    return xflow
