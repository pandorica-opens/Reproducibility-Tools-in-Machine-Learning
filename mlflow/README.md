# Weights & Biases 

1. Make sure you have mlflow installed.
```
pip install mlflow
```

2. Check that it has all the dependencies installed (i.e. tensorflow) and other libraries are added to the requirements.txt


3. Initialize our sample script.
```
pip install -r requirements.txt
```

4. The following import and function call are the only additions to code required to automatically log metrics and parameters to MLflow. To track a run add:

```python
import mlflow.keras
mlflow.keras.autolog()
```

6. Run the script from the command line.

```
python beginner.py
```

7. In order to see the interface for the run:

```
mlflow ui
```

Awesome! Now head over to http://localhost:5000/ to check the run!