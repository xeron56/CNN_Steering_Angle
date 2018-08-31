# CNN_Steering_Angle


## Requirements & Dependencies
- [Bash on ubuntu on windows](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
- Python 2.7
- [Numpy](http://www.numpy.org/)
- [SciPy](https://www.scipy.org/)
- [Tensorflow](https://www.tensorflow.org/get_started/os_setup)
- [Keras](https://keras.io/) 1.1.0
- [udacity-driving-reader](https://github.com/rwightman/udacity-driving-reader) from rwightman, used to extract images from ROS bag files



# Data

 the dataset can be downloaded in the ROSBAG format from here: https://github.com/udacity/self-driving-car/tree/master/datasets/CH2 (both CH2_001 and CH2_002)

We used rwightman's [Udacity Reader docker tool](https://github.com/rwightman/udacity-driving-reader) 
to convert the images into JPGs.



The code assumes the following directory structure for data:

```
- data
-- models
-- test
--- center
---- 1477431483393873340.jpg
-- train
--- center
---- 1477431802438024821.jpg 
```

Change `data_path` value in `config.py` to point to this data directory.

# Pre-processing


To pre-process training data, run:

```
python train_data.py
```

To pre-process test data, run:

```
python test_data.py
```

These pre-processing scripts convert image sets to numpy arrays.

# Model

The main architecture for this model was inspired by the [NVIDIA's self-driving car paper](https://arxiv.org/abs/1604.07316)
The code includes 3 different models. To choose one of the models, change the model_name in config.py to either "nvidia1", "nvidia2", or "nvidia3".

To train different models, run:

```
python model.py
```

You can change these parameters in the `config.py` file:




Once you have trained your models, you can choose the one with the best performance, copy it into the submissions folder and rename it to "final_model.hdf5". 

To predict steering angles from test data, run:

```
python drive.py
```

* Visualizing predicted steering angles

To visualize model predictions on test data, run:

```
python renderview.py
```



