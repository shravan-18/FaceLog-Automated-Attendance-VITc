import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices("GPU")
if len(gpus) > 0:
    print("GPUs Available:")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPU available!")
