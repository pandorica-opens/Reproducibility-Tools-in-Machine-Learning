# Reproducibility challenge


One of the challenges in machine learning research is to ensure that published results are reliable and reproducible. For that reason, a number of frameworks (such as i.e. mlflow, wandb and others) is used for tracking the hyperparameters. By doing so, we expect the results to be reproducible in machiene learning workflows. 

The challenge also arises as some of the algorithms in tensorflow/keras are [reported](https://stackoverflow.com/questions/50659482/why-cant-i-get-reproducible-results-in-keras-even-though-i-set-the-random-seeds) to involve the randomness despite the established seed in the code. To investigate that matter, we empirically compare the named frameworks and highlight the usability points of each of them. 

Namely, for a number of algorithms we aim to find the answer “Which Framework is most suitable for this kind of task?” 

