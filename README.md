# Frameworks for Reproducible Machine Learning


Producing reproducible results is paramount in scientific research, but this can be a challenge in the field of machine learning. In this work we compare three frameworks which assist with the reproduction of results in machine learning: **Weights and Biases**, **Guild AI** and **MLflow**. We empirically compare their performance on a number of experiments and derive a decision tree which takes the required features for a machine learning problem as an input for the query and returns the framework which would be most suited to the task. We also look at their logging capabilities and their collaboration support. 

Moreover, we compare the definitions of reproducibility and replicability in the context of neural networks and consider the possibility of [*exactly* reproducing the results of our experiments with neural networks using the Docker framework](https://github.com/pandorica-opens/Reproducibility-Tools-in-Machine-Learning/tree/master/docker%20replication).

Based on our findings, we construct a [decision tree](https://github.com/pandorica-opens/Reproducibility-Tools-in-Machine-Learning/blob/master/Decision%20tree/frameworks-full-depth-tree.svg) to assist the user according to their preferences of certain criteria using our given scores. It enables a better visualisation of the probabilities as to which framework would be most suitable according to the required criteria. 

## Summary of Findings of Framework Comparison


From our conducted experiments and the respective scores assigned to each experiment, we summarise our findings of the framework comparison in [Table 11](https://github.com/pandorica-opens/Reproducibility-Tools-in-Machine-Learning/blob/master/imgs/Table11.png). This is the concise summary of the high-level concepts based upon our experiments. In this table we can see that all frameworks perform well with MLflow performing marginally better than W\&B. If reproducibility is the goal then MLflow and W\&B would be more suited to the task. Guild does not offer the same level of collaboration and automatic saving of model parameters as the other two frameworks, but if runtime and memory is a priority for the user, then Guild would be a good choice.

## Report text

The full text of the report can be found at [the repository's root](https://github.com/pandorica-opens/Reproducibility-Tools-in-Machine-Learning/blob/master/Frameworks%20for%20Reproducible%20Machine%20Learning.pdf).

## Decision tree with restriction 3 on depth based on Table 11
		
Shown is the decision tree built on each possibility of the criteria choice shown in Table 11, namely: *Auto-Logging*, *Runtime*, *No. of Lines*, *Collaboration*, *Memory*, *Deep Dive Keras* and *Deep Dive Sklearn* (scores for the other criteria are identical). The [current tree](https://github.com/pandorica-opens/Reproducibility-Tools-in-Machine-Learning/blob/master/Decision%20tree/frameworks-3-depth-tree.svg) has a restriction of 3 on the tree depth:
<img src="./Decision%20tree/frameworks-3-depth-tree.svg" width="800">
        
The decision tree fits Table 11 completely. Each feature has a value of 1 if it is important to the user, and 0 if this is not the case. The decision space ranges from (0,0,0,0,0,0,0) for the case that none of the criteria are important, to (1,1,1,1,1,1,1) where all of the criteria are important. For instance, if the values for *Deep Dive Keras* and *Auto-Logging* are 1 (they are important to the user), then MLflow would be selected.
		
## Decision tree with no restriction on depth based on Table 11

The full tree is available [here](https://github.com/pandorica-opens/Reproducibility-Tools-in-Machine-Learning/blob/master/Decision%20tree/frameworks-full-depth-tree.svg) and is shown below. We can observe that MLflow has a clear advantage, W\&B is chosen in a specific case, when, amongst other chosen parameters, *Memory* is important and *No. of Lines* is not important.
![Full decision tree](./Decision%20tree/frameworks-full-depth-tree.svg)

## Decision tree based on reproducibility parameters

This decision tree concentrates on the criteria that we find particularly useful in terms of reproducibility, namely *Auto-Logging*, *Collaboration*, *Deep Dive Keras* and *Deep Dive Sklearn*. The decision tree is built using the same algorithm as described above. The *all* case stands for the edge case of all parameters being not important or (0,0,0,0). We can see that MLflow has the highest chance to be chosen, with wandb being available as an alternative when auto-logging is not important to the user.

<img src="./Decision%20tree/frameworks-reproducibility-tree.svg" width="600">
