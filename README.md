# Project repository

## Is combining different metrics of rs-fMRI more predictive of age than using only one metric?

### Project Summary

This project aims to compare the capacity to predict age of different metrics of resting-state activity as well as their combined predictive ability, with the use of machine learning. I adapted Jake Vogel's machine learning tutorial to create 4 machine learning models predicting age using respectively Functional Connectivity (FNC), timeseries, fractional Amplitude of Low-Frequency Fluctuation (fALFF) and their combination. 


### Project Definition

My goal in this project was to asses if using multiple metrics of rs-fMRI (i.e. FNC, timeseries and fALFF) is more predictive of age than using only data from one metric. The overall objectives of this project were for me to get familiar with programming machine learning models, how to model different metrics of resting-state activity and improve my Python coding skills. I also wanted to learn how to optimize the parameters of a training machine learning model. For this project, I used a Support Vector Regressor algorithm. Details about the conceptualization of this project can be found in this video:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=u7wtJ5R34xY" target="_blank"><img src="http://img.youtube.com/vi/Yu7wtJ5R34xY/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

#### Project Aims

1. Script and perform a machine learning model to predict age using rs-fMRI FNC
2. Script and perform a machine learning model to predict age using rs-fMRI fALFF
3. Script and perform a machine learning model to predict age using rs-fMRI timeseries
4. Script and perform a machine learning model to predict age using rs-fMRI FNC, fALFF and timeseries
5. Compare models 1, 2, 3 and 4 to see which one is the most predictive of age

### Learning Experience

#### Dataset

* [MAIN Nilearn tutorial data](https://osf.io/5hju4/)
* Taken from this [publication](https://www.ncbi.nlm.nih.gov/pubmed/29531321)
* Already pre-processed using fmriprep see details [here](https://osf.io/wjtyq/)
* 155 participants watched a Disney movie passively (resting-state) while being in the scanner
* Age of participants ranged from 3 to 39 years old



#### Tools/Language used

* Nilearn
* Python
* Jupyter notebook
* Git and Github
* Pandas
* Matplotlib
* Scikit-learn
* Plotly
* Scipy
* Numpy
* Seaborn

#### Learning Aims

1. Learn how to use Nilearn
2. Reproduce age prediction Nilearn machine tutorial using FNC as predictor
3. Learn how to script other metrics of resting-state fMRI (i.e. fALFF and spatial maps) in Python
4. Be able to use fALFF and spatial maps as machine learning predictors in Nilearn
5. Be able to script a machine learning algorithm that uses 3 different metrics of resting-state (i.e. FNC, fALFF and machine learning) as a predictor of a variable
6. Learn how to statistically compare the performance of multiple machine learning models

#### To-Do

- [X]  Read Nilearn documentation
- [X]  Data exploration and visualization
- [X]  Re-run script age prediction machine learning tutorial using FNC
- [X]  Read documentation on how to model spatial maps in Nilearn
- [X]  Read documentation on how to model power spectra in Python
- [X]  Select cross-validation method
- [X]  Select dimensionality reduction method
- [X]  Modify ML tutorial script to train model to predict age using timeseries
- [X]  Modify ML tutorial script to train model to predict age using fALFF
- [X]  Modify ML tutorial script to train model to predict age using a combination of FNC, timeseries and fALFF
- [X]  Run all models on test data
- [ ]  Read on techniques to statistically compare accuracy of machine learning algorithm
- [ ]  Write and run script of statistical comparison of models
- [ ]  Statistically compare the performance of the 4 models

### Results

#### Model Feature Sizes

* FNC = 155 x 2016
* Timeseries = 10 752
* fALFF = 155 x 2016
* Combined Metrics = 12 832

#### Model Optimization

For the machine learning models of the training set of the 3 metrics of interest I performed 5 different model optimization techniques on the Support Vector Regressor Algorithm:
1. 10-fold cross-validation (cv)
2. 10-fold cv with age log-transformed to normalize the distribution of age
3. 10-fold cv with Gridsearch to identify the optimal parameters (age log-transformed)
4. 10-fold cv with validation curve to see if using a more complex and non-linear model could improve prediction on the training set (age log-transformed)
5. 10-fold cv with PCA feature reduction (age log-transformed)

For the models using FNC and timeseries as predictors, the most predictive training models used the 10-fold cross-validation with age log-transformed, while this model was only slightly improve by the PCA when using fALFF as a predictor. Hence, I decided to use the 2nd model optimization approach.

#### Model performance on validation data

![Alt text](https://github.com/mtl-brainhack-school-2019/Isabelle-Simard_Multimodal_ML/blob/master/All_Metrics_Validate_Model_Log_Age.png "Logo Title Text 1")

![Alt text](https://github.com/mtl-brainhack-school-2019/Isabelle-Simard_Multimodal_ML/blob/master/Combined_Metrics_Validate_Model_Log_Age.png "Logo Title Text 2")


![Alt text](https://github.com/mtl-brainhack-school-2019/Isabelle-Simard_Multimodal_ML/blob/master/Model_Accuracy.png "Logo Title Text 2")







#### Deliverables

The results of the project can be found in the 5 deliverables that I created:

*   ML_Regression_Combined_Metrics.ipynb
*   ML_Regression_FNC.ipynb
*   ML_Regression_Neural activity.ipynb
*   ML_Regression_fALFF.ipynb
*   fALFF.py




### Current issues

* Let me know if you have any suggestions regarding how to statistically compare ML models. Currently looking to use this [Scikit script](https://machinelearningmastery.com/compare-machine-learning-algorithms-python-scikit-learn/).




![Alt Text](https://media.giphy.com/media/4TtTVTmBoXp8txRU0C/giphy.gif)