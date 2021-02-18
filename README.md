# Frameworks for Reproducible Machine Learning

In this work we compare three frameworks, that assist in reproducing results in Machine Learning: **wandb**, **guild.ai** and **mlflow**. We empirically compare their performance on a number of experiments and conduct a *decision tree* that takes as an input the most important features for the query. Moreover, we address the definition of the *reproducibility* in the context of the Neural Networks and argue about the possibility of the *replicating* the results using Docker framework for Neural Networks. We conclude our work by compiling the decision tree and drawing the conclusions from our findings.

The full tree of the framework choice, depending on the most important input criteria is presented below:  

![decision tree](./Decision%20tree/frameworks-allleaves-tree.svg)

It is possible to manipulate the number of leaves in the notebook. For instance, the 8-leaf version is presented below:

![decision tree](./Decision%20tree/frameworks-8leaves-tree.svg)
