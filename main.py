import pathlib
from keras.utils import image_dataset_from_directory

base_dir = pathlib.Path("data")

# Read in datasets and resize images to 180x180
train_dataset = image_dataset_from_directory(
 base_dir / "train",
 image_size=(180, 180),
 batch_size=32
)
validation_dataset = image_dataset_from_directory(
 base_dir / "validation",
 image_size=(180, 180),
 batch_size=32
)

from tensorflow import keras
from keras import layers

# VGG Image net convolution base used for feature extraction
conv_base = keras.applications.vgg16.VGG16(
 weights="imagenet",
 include_top=False,
 input_shape=(180, 180, 3)
)
# Freeze convolution layers
conv_base.trainable = False

# Basic data augmentation to resist overfitting
# and pad small dataset
data_augmentation = keras.Sequential(
 [
 layers.RandomFlip("horizontal"),
 layers.RandomRotation(0.1),
 layers.RandomZoom(0.2),
 ]
)

# Model definition, data augmentation, convolution base
# and new dense classifier
inputs = keras.Input(shape=(180, 180, 3))
x = data_augmentation(inputs)
x = keras.applications.vgg16.preprocess_input(x)
x = conv_base(x)
x = layers.Flatten()(x)
x = layers.Dense(128)(x)
outputs = layers.Dense(1, activation="sigmoid")(x)
model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(loss="binary_crossentropy",
 optimizer=keras.optimizers.RMSprop(0.002),
 metrics=["accuracy"]
)
print(model.summary())

callbacks = [
 keras.callbacks.ModelCheckpoint(
 filepath="tar_net.keras",
 save_best_only=True,
 monitor="val_loss")
]

history = model.fit(
 train_dataset,
 epochs=100,
 validation_data=validation_dataset,
 callbacks=callbacks
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

accuracy = history.history["accuracy"]
val_accuracy = history.history["val_accuracy"]
loss = history.history["loss"][2:]
val_loss = history.history["val_loss"][2:]
epochs = range(1, len(accuracy) + 1)

plt.plot(epochs, accuracy, "bo", label="Training accuracy")
plt.plot(epochs, val_accuracy, "b", label="Validation accuracy")
plt.title("Training and validation accuracy")
plt.legend()
plt.savefig('graph_0.png')
plt.clf()

plt.plot(epochs[2:], loss, "bo", label="Training loss")
plt.plot(epochs[2:], val_loss, "b", label="Validation loss")
plt.title("Training and validation loss")
plt.legend()
plt.savefig('graph.png')