import tensorflow as tf
from matplotlib.image import imread
import numpy as np

loaded_model = tf.keras.models.load_model('my_model.h5')

def test_model_interface():
    folder = 'test_photos/'
    filename = folder + 'cat.0.jpg'
    image = imread(filename)
    image.resize((200, 200, 3))
    q = loaded_model.predict( np.array( [image,] )  )
    assert q[0][0] == 1

    filename = folder + 'cat.1.jpg'
    image = imread(filename)
    image.resize((200, 200, 3))
    q = loaded_model.predict( np.array( [image,] )  )
    assert q[0][0] == 1

    filename = folder + 'cat.2.jpg'
    image = imread(filename)
    image.resize((200, 200, 3))
    q = loaded_model.predict( np.array( [image,] )  )
    assert q[0][0] == 1

    filename = folder + 'dog.0.jpg'
    image = imread(filename)
    image.resize((200, 200, 3))
    q = loaded_model.predict( np.array( [image,] )  )
    assert q[0][0] == 0

    filename = folder + 'dog.1.jpg'
    image = imread(filename)
    image.resize((200, 200, 3))
    q = loaded_model.predict( np.array( [image,] )  )
    assert q[0][0] == 0

    filename = folder + 'dog.2.jpg'
    image = imread(filename)
    image.resize((200, 200, 3))
    q = loaded_model.predict( np.array( [image,] )  )
    assert q[0][0] == 0
