
# HNSCPred :- A Tool for Identification of HNSCC from Single Cell Genome using Deep Learning

A computational approach tool to predict Head and Neck Cancer affected patients from their single cell RNA seq data.


## Introduction

Head and neck cancer, which encompasses a range of malignancies affecting the respiratory tract and upper digestive tract and also the seventh most common cancer in the world. 

This tool aims to use Artifical Neural Network (Deep Learning) model to classify Normal Control(NC) patients and Head and Neck Cancer (HNSCC) patients from
their single cell RNA seq data. The tool takes 10x single cell genomics data as input and predicts whether the patient is diseased or healthy with the help of highly trained model.

An excellent feature selection method called mRMR (Minimum Redundancy Maximum Relevance) was used to find out top 100 features which act as promising biomarkers
in classification and prediction of Normal and Diseased patients. Also further classified diseased patients into HPV+ and HPV-.

## Installation

Install my-project with pip

```bash
  pip install HNSCPred
```
    
You if previously installed please update the python package to the latest version using the command below

```bash
  pip3 install --upgrade HNSCPred
```
## Usage/Examples

After installation of the HNSCPred package in your python enviornment. Import the library using the below code.


```python
import HNSCPred
```
The HNSCPred comes with 1 inbuilt module. 

- Predict
Please import only 1 module in your python enviornment using the code below.

```python
from HNSCPred import Validation
```

After importing all the important pre requisites. You can follow the demo below for your case.


```python
import pandas as pd
df = pd.read_csv("Your file path here")

Validation.predict(df)

```




## Authors


- Akanksha Jarwal. 
- Aman Srivastava.
- Anjali Dhall.
- Sumeet Patiyal.  
- [Prof. G.P.S. Raghava](https://webs.iiitd.edu.in/raghava/)

