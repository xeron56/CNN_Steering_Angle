# CNN_Steering_Angle
Here's a video about this project

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/v3rUuBi16rw/0.jpg)](https://www.youtube.com/watch?v=v3rUuBi16rw)

## Requirements & Dependencies
- [Bash on ubuntu on windows](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
- Python 2.7
- [Numpy](http://www.numpy.org/)
- [SciPy](https://www.scipy.org/)
- [Tensorflow](https://www.tensorflow.org/get_started/os_setup)
- [Keras](https://keras.io/) 1.1.0
- [udacity-driving-reader](https://github.com/rwightman/udacity-driving-reader) from rwightman, used to extract images from ROS bag files



# Data

the dataset can be downloaded  from here: 

training: [link](https://github.com/udacity/self-driving-car/tree/master/datasets/CH2) CH2_002 
testing:[link](https://drive.google.com/drive/folders/0B5PcvDP2jMVSV3ZpTmFPdmdFUHc) : "scenario1" folder then go to "data" folder then finally video data set is on "car" folder, [scenario1 -> data -> car -> car1_camera1.mp4
 ]
 Directory structure for data:

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

To train different models, run:

```
python model.py
```

You can change these parameters in the `config.py` file:


To predict steering angles from test data, run:

```
python drive.py
```

* Visualizing predicted steering angles

To visualize model predictions on test data, run:

```
python renderview.py
```



