# Isabelle-Simard
Project repository 

Is combining different metrics of rs-fMRI more predictive of age than using only FNC?

I originally wanted to use my thesis data to build this pipeline. However, a war with ethics is keeping me away from it at the moment. My original idea is to asses if using multiple metrics of rs-fMRI (i.e. FNC, power spectra and statistical maps) is more predictive of recidivism in offenders than using only data from one metric. Hence, in the absence of my data of interest, I am going to build on the machine learning exercise that we did in class to see if combining FNC, power spectra and statistical maps of rs-fMRI is more predictive of age than only using FNC.

Aims

1)	Script and perform a machine learning model to predict age using rs-fMRI FNC
2)	Script and perform a machine learning model to predict age using rs-fMRI power spectra
3)	Script and perform a machine learning model to predict age using rs-fMRI statistical maps
4)	Script and perform a machine learning model to predict age using rs-fMRI FNC, power spectra and statistical maps
5)	Compare models 1, 2, 3 and 4 to see which one is the most predictive of age

Dataset

MAIN Nilearn tutorial data
https://osf.io/5hju4/
Already pre-processed using fmriprep see details here https://osf.io/wjtyq/
155 participants watched a Disney movie passively (resting-state) while being in the scanner.
Taken from this publication:
https://www.ncbi.nlm.nih.gov/pubmed/29531321

Tools/Language used

Nilearn

Data processing and structuring

1)	Load data
2)	Data exploration and visualization
3)	Learn how to model power spectra and statistical maps in Nilearn

Machine learning model architecture

Current issues

Deliverables for Brainhack School 2019

Further scope

