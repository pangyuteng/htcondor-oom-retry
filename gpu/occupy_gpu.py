import time
import tensorflow as tf

tf.debugging.set_log_device_placement(True)
mylist = []
for x in range(4):
    with tf.device(f'/GPU:{x}'):
        tmp = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
        mylist.append(tmp)

print(mylist)
time.sleep(50000)
"""
docker run -it -u $(id -u):$(id -g) -w /workdir -v $PWD:/workdir \
    tensorflow/tensorflow:2.8.0-gpu-jupyter bash


"""