import tensorflow as tf

#Import wandb libraries
import wandb
from wandb.keras import WandbCallback


wandb.init(project="first-attempt",
  	config={
    "dropout": 0.2,
    "learn_rate": 0.01,
    "epochs": 5,
    "dense": 64,
    "activation":'relu'},
    sync_tensorboard=True)

config = wandb.config

mnist = tf.keras.datasets.mnist

epochs = config.epochs
learning_rate = config.learn_rate
activation = config.activation
dropout = config.dropout
dense = config.dense


(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# we can log the separate values in that way
# wandb.log({"examples from train set ": [wandb.Image(x_train[0,:, :], caption="Label")]})
# wandb.log({"predicted ": [wandb.Image(x_test[0,:, :], caption=y_test[0])]})

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(dense, activation=activation),
        tf.keras.layers.Dropout(dropout),
        tf.keras.layers.Dense(10, activation='softmax'),
    ]
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate), metrics=['accuracy'], loss='sparse_categorical_crossentropy',
)

# Add labels
labels =["0","1","2","3","4","5","6","7","8","9"]

# during the validation process it is possible to callback images and validation metrics
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=epochs, callbacks=[WandbCallback(data_type="image", labels=labels)])


