### Performance Evaluation of prediction models

*   Relationship Forum on Dcard
    * test set size: 200 rows for each class(1: male, 0: not male or unknown)
    * Confusion matrix for models:
        * Passive Aggressive Classifier
        
        |Predicted:arrow_down_small: True:arrow_forward:|1|0|
        |---|---|---|
        |1|106|56|
        |0|94|144|
    
            accuracy= 0.625
            precision= 0.654 
            recall= 0.53

        * XGBoost Classifier

        |Predicted:arrow_down_small: True:arrow_forward:|1|0|
        |---|---|---|
        |1|92|56|
        |0|108|144|
    
            accuracy= 0.59 
            precision= 0.622 
            recall= 0.46
    
        * albert_FT
        
        |Predicted:arrow_down_small: True:arrow_forward:|1|0|
        |---|---|---|
        |1|113|36|
        |0|87|164|
          
            accuracy= 0.693
            precision= 0.758 
            recall= 0.565
    
        * albert_FB
        
        |Predicted:arrow_down_small: True:arrow_forward:|1|0|
        |---|---|---|
        |1|180|145|
        |0|20|55|

            accuracy= 0.588
            precision= 0.554 
            recall= 0.9
          
        * bertSeqCls
    
        |Predicted:arrow_down_small: True:arrow_forward:|1|0|
        |---|---|---|
        |1|103|41|
        |0|97|159|

            accuracy= 0.655
            precision= 0.715 
            recall= 0.515
    
- - -

* General Evaluation: including 52 predictable forums on Dcard
    * test set size：randomly-chosen 5 rows from every forum
        * Confusion matrix 
            * Passive Aggressive Classifier
            
            |Predicted:arrow_down_small: True:arrow_forward:|1|0|
            |---|---|---|
            |1|11|96|
            |0|9|144|
        
                accuracy= 0.6
                precision= 0.1 
                recall= 0.55
    
            * XGBoost Classifier
    
            |Predicted:arrow_down_small: True:arrow_forward:|1|0|
            |---|---|---|
            |1|11|131|
            |0|9|109|
            
                accuracy= 0.46
                precision= 0.08 
                recall= 0.55
- - -   
