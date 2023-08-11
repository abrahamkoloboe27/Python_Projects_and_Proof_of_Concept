# This notebook is a POC to show ML skills.

# Titanic survived prediction
The sinking of the Titanic is one of the most infamous shipwrecks in history.

On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding with an iceberg. Unfortunately, there weren’t enough lifeboats for everyone onboard, resulting in the death of 1502 out of 2224 passengers and crew.

Would you have survived the sinking of the titanic ? 

This notebook is using Machine Learning library **sklearn** to make a model to predict whether you would have survived or not. 

Let's get fun :)


# Plan

## Data Import
* We have used the dataset titanic whic can found at the adress : https://www.kaggle.com/competitions/titanic/data
* To import he file we use function **read_csv** of the library **Pandas**
* The Data is import as **Pandas Data Frame**

## Exploratory analysis
* Here we get a look of our data 
* We looked at the missing values ​​and the types of the different variables in our dataset
* We looked at the different statistical information of the dataset such as the mean, the standard deviation, the mode, the quantiles, min, max values etc.
* We get a look of histogram of all dataset's variables (numeric variables and categorical).
* We get a look of a **pair plot** and a **heatmap** of the dataset with the library **seaborn**.
## Pre-processing
* Here we identify our target variable.
* We first eliminate the variables that will not be used for learning **name** and **ticket**.
* We then create two variables **X** and **y** which respectively contain the explanatory variables and the target variable, the variable **survived** here.
* Then thanks to the **train_test_split** function of sklearn we create a training set which represents **70%** and a test set which represents **30%**. We specify the **stratify** argument in this function so that the training and test data have the same class imbalance as the original dataset.
## Modeling
* Here we use models which are at the same time pipelines and which allow pre-processing operations such as the management of missing values, the encoding of categorical variables, the transformation of columns and the normalization of data.
## Model evaluation 
* To evaluate our model, several metrics are used here: F1 score, Accuracy, AUC.
* It is on these metrics that we will base ourselves to select the best model.
* Training each model generates  a **classification report**, a **confusion matrix** and the scores of **Accuracy** and **AUC** on the train and train sets. test.
* The different models we trained here are: **LogisticRegression**, **BaggingClassifier**, **RandomForestClassifier**, **KNeighborsClassifier**
## Model selection
* The selection of the best model is made on the basis of the model's **AUC** score on the test game. This metric is the most suitable for the evaluation of models because of the problem of class imbalance.
* Thus, the best model is the one with the best AUC score on the test set.
## Model save 
* To save the best model we use the **joblib** library