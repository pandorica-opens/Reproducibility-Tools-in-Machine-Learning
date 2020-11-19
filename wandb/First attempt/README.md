# Weights & Biases 

1. Make sure you have W&B installed.
```
pip install wandb
```

2. Put the libraries to install in the requirements.txt


3. Initialize our sample script.
```
pip install -r requirements.txt
wandb init
```

4. After `wandb` enter a name for your new project: First Attempt
This directory is configured!  Next, to track a run add:

```python
import wandb
from wandb.keras import WandbCallback

# Initialize wandb and save hyperparameters
wandb.init(
  project="first-attempt",
  config={
    "dropout": 0.2,
    "learn_rate": 0.01,
    "epochs": 5,
    "dense": 64,
    "activation":'relu'
     }
)
config = wandb.config
```

5. Add Keras WandbCallback, metrics

```python 
model.fit(x_train, y_train, epochs=epochs, callbacks=[WandbCallback(data_type="image", labels=labels)])
loss, accuracy = model.evaluate(x_test, y_test)
```


6. Run the CNN script from the command line.

```
python beginner.py
```

Awesome! Now head over to [Weights & Biases](https://app.wandb.ai) to visualize your model training or to the report page to view the [comparison](https://wandb.ai/s6hakond/first-attempt/reports/wandb--VmlldzozMjM0NTk?accessToken=ghmyav5gvswz6pnr3g9xfib633gdygzvgw8u1pr8x50ac7k46f041vnpare6u2m2).