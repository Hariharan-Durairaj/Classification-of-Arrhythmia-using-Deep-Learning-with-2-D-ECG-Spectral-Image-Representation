# Classification of Arrhythmia using Deep Learning with 2-D ECG Spectral Image Representation

## Introduction
The Classification of Arrhythmia using Deep Learning with 2-D ECG Spectral Image Representation project is aimed at building a deep learning model that can classify different types of arrhythmia from 2D ECG spectral image representation.

## Dataset
The dataset used in this project is available in the Dataset folder. The dataset consists of two folders, train and test. The train folder contains 8670 ECG images in 6 classes and the test folder contains 2286 ECG images in the same 6 classes.

## Requirements
Python 3.x
Keras 2.7
Tensorflow 2.x
Watson Machine Learning Client
IBM Watson Machine Learning API Key
IBM Cloud Object Storage credentials
Flash

## Installation
To run the project, you can clone the repository to your local machine using the following command:

bash
Copy code
```
https://github.com/Hariharan-Durairaj/Classification-of-Arrhythmia-using-Deep-Learning-with-2-D-ECG-Spectral-Image-Representation.git
```

Then, install the required dependencies using the following command:

Copy code
```
pip install -r requirements.txt
```

## Usage

app.py: Run the code to launch the website
To run the run.py use the below code in terminal
```
python -m flask run
```

To install flask, run the below code
```
python -m pip install flask
```

ECG_classification.ipynb: This is the main Jupyter notebook that contains the code for building and training the deep learning model.

ECG.h5: This is the trained model that was saved after training.

classification-model.tgz: This is a compressed file that contains the trained model that can be deployed on IBM Watson Machine Learning.

README.md: This file.

requirements.txt: This file contains all the required dependencies for the project.

