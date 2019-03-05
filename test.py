import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display
import tensorflow as tf


def specgramChart(fs, data):
    plt.rcParams['savefig.dpi'] = 300  # 图片像素
    plt.rcParams['figure.dpi'] = 300  # 分辨率
    plt.subplot(211)
    plt.plot(data)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.subplot(212)
    plt.specgram(data, Fs=fs)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.xlim(0, 10)
    plt.tight_layout()
    plt.show()

def melSaleChart(data, sample):
    S = librosa.feature.melspectrogram(y=data, sr=sample)
    librosa.display.specshow(librosa.power_to_db(S),
                             x_axis='time', y_axis='mel')
    plt.legend()
    plt.tight_layout()
    plt.show()

data, sample = librosa.load('zenzenzense2.wav')
#   S[Hz,Time]
#   S中的Time = Real_Time * 解析率 / 512
#   S_Time = S.shape[1]
S = librosa.feature.melspectrogram(y=data, sr=sample)
print(S.shape[1]/sample*512)
print(S)
#melSaleChart(data,sample)

#image_raw_data = tf.gfile.FastGFile('test.jpg', 'rb').read()

# with tf.Session() as sess:
#     #img_data = tf.image.decode_jpeg(image_raw_data)
#     img_data = tf.image.convert_image_dtype(S, dtype=tf.uint8)
#
#     resized = tf.image.resize_images(img_data, [300, 100], method=0)
#     print(resized)
#     # TensorFlow的函数处理图片后存储的数据是float32格式的，需要转换成uint8才能正确打印图片。
#     print("Digital type: ", resized.dtype)
#     print("Digital shape: ", resized.get_shape())
#     cat = np.asarray(resized.eval(), dtype='uint8')
#     # tf.image.convert_image_dtype(rgb_image, tf.float32)
#     plt.imshow(cat)
#     plt.show()

