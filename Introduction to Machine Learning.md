## Steps of Binary Classification in Machine Learning 

### 1. Define problem
Determine whether the author is male or not (True:1; unknown or False:0) based on his/her articles published on the forum.

### 2. Choose evaluation method
Evaluation allows us to see how the model might perform against data that it has not yet seen. <br>
**Confusion matrix** is a technique for summarizing the performance of a classification algorithm.

|Predicted:arrow_down:/True class:arrow_right:|  Positive | Negative |
|---|---|---|
| Positive |**TP(True Positive)**|**FP(False Positive)**<br>Type 1 Error|
| Negative |**FN(False Negative)**<br>Type 2 Error|**TN(True Negative)**|

### 3. Gather and explore raw data
Gathering data is a crucial step, since the quality and quantity of data will directly determine how good the predictive model can be. 
Next, do data visualizations to see descriptive statistics(for numeric data) and relations between variables.

### 4. Preprocessing raw data
Sometimes the data we collect need further adjusting and manipulation. e.g. remove digits, punctuations, stopwords, normalizing...etc.
As for Chinese text classification, we might need to remove English alphabets, digits, punctuations.

### 5. Label data manually
Why labeling? <br>
Labels resemble the ***correct answer to prediction*** and are needed in supervised learning.

<p>
After finishing labeling manually, check if there is any data imbalance. Imbalanced data will cause model to be biased toward guessing everything it sees is the majority class.

>How to deal with imbalanced data?
>   1. When the quantity of data is sufficient :arrow_right: **Under-sampling** : Reduce the size of the abundant class by keeping all samples in the rare class and randomly selecting an equal number of samples in abundant class.
>   2. When the quantity of data is insufficient :arrow_right: **Over-sampling** : Increase the size of rare samples by using SMOTE(Synthetic Minority Over-Sampling Technique).<br>

### 6. Select features: 
*i.e. Select a subset of **independent** features from the dataset.* <br>
In order to improve the performance of model, feature selection is the necessary process.
It's desirable to quantify the strength of the relationship between the predictors and the outcome and reduce computational cost.<p>

### 7. Split into training, dev, test set
>Randomize the ordering in advance to avoid the order of data affecting what model learns.
- **training set**: normally 80% of dataset, but the fraction would be higher if data is huge.<br>
A dataset used during learning process and is used to fit the parameters. 
   <p> e.g. Training set assembles student(model)'s textbook. Model learns from training set.
  
- **development set (validation set)**: normally 10% of dataset, but the fraction would be lower if data is huge.<br>
A dataset used to tune the hyper-parameters. *Must be independent of the training set.* 
   <p> e.g. Validation set resembles assignments written by student(model).

- **test set**: normally 10% of dataset, but the fraction would be lower if data is huge.<br>
A dataset used to assess the performance of model. Only used once a model is completely trained. *Must be independent of the training set.*
   <p> e.g. Test set resembles exams went through by student(model). Student(model) could assess itself with exam performance.

### 8. Start training with a baseline model
*baseline model: simple to set up and low cost to implement* <p>
Choose a model that is suited for text-based data and equipped to classify.

    Fundamental and widely-used classification algorithms
    - Logistic Regression
    - Decision Tree
    - Random Forest 
    - Naive Bayes
    - Supported Vector Machines(SVM)

### 9. Evaluate classification result
      Frequently used metrics.
      - Precision = TP / (TP + FP)
      - Recall = TP / (TP + FN)
      - F1-score = 2 * (Precision * Recall) / (Precision + Recall)

### 10. Review 
 - Features

    The **feature importance scores** can highlight **which features may be most relevant to the target**, 
**which features are the most important and least important to the model when making a prediction**,
and delete those features with lower scores or keep those features with higher scores.
Below are 3 methods to remove irrelevant variables in supervised learning. <br>
    
        1.Filter methods
        2.Wrapper methods
        3.Embedded methods
- Hyper-parameters

    - What should be the *maximum depth* allowed for my decision tree? 
    - *How many trees* should I include in my random forest?
    - What should I set my *learning rate* to for gradient descent?