import tensorflow as tf

hello = tf.constant("Hallo, Tensorflow!")
tf.print(hello)
print(hello)
print("TensorFlow Version: {}".format(tf.__version__))

tf.debugging.set_log_device_placement(True)


def get_GPU_CPU_details():
    print("GPU vorhanden?", tf.test.is_gpu_available())
    print("Devices:", tf.config.experimental.list_physical_devices())
    print(tf.config.list_physical_devices('GPU'))


get_GPU_CPU_details()
