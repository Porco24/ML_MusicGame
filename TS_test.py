import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


image_raw_data = tf.gfile.FastGFile('test.jpg', 'rb').read()

with tf.Session() as sess:
    img_data = tf.image.decode_jpeg(image_raw_data)
    img_data = tf.image.convert_image_dtype(img_data, dtype=tf.uint8)

    resized = tf.image.resize_images(img_data, [300, 100], method=0)
    print(resized)
    # TensorFlow的函数处理图片后存储的数据是float32格式的，需要转换成uint8才能正确打印图片。
    print("Digital type: ", resized.dtype)
    print("Digital shape: ", resized.get_shape())
    cat = np.asarray(resized.eval(), dtype='uint8')
    # tf.image.convert_image_dtype(rgb_image, tf.float32)
    plt.imshow(cat)
    plt.show()