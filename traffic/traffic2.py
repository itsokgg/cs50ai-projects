# created by chatgpt based on traffic.py
import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

EPOCHS = 30
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4
BATCH_SIZE = 32


def main():
    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Load image arrays and labels
    images, labels = load_data(sys.argv[1])

    # Normalize image data and convert to float32
    images = np.array(images).astype("float32") / 255.0
    labels = tf.keras.utils.to_categorical(labels)

    # Split into train and test
    x_train, x_test, y_train, y_test = train_test_split(
        images, labels, test_size=TEST_SIZE
    )

    # Define model
    model = get_model()

    # Define data augmentation
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        shear_range=0.1,
        fill_mode='nearest'
    )
    datagen.fit(x_train)

    # Callbacks: early stopping and learning rate adjustment
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=5, monitor='val_loss', restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, verbose=1)
    ]

    # Train model
    model.fit(
        datagen.flow(x_train, y_train, batch_size=BATCH_SIZE),
        steps_per_epoch=len(x_train) // BATCH_SIZE,
        epochs=EPOCHS,
        validation_data=(x_test, y_test),
        callbacks=callbacks
    )

    # Evaluate model
    model.evaluate(x_test, y_test, verbose=2)

    # Save model if requested
    if len(sys.argv) == 3:
        model.save(sys.argv[2])
        print(f"Model saved to {sys.argv[2]}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.
    """
    images = []
    labels = []
    for category in range(NUM_CATEGORIES):
        category_dir = os.path.join(data_dir, str(category))
        if not os.path.isdir(category_dir):
            continue
        for filename in os.listdir(category_dir):
            filepath = os.path.join(category_dir, filename)
            img = cv2.imread(filepath)
            if img is None:
                continue

            # Sharpening kernel (optional)
            kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
            img = cv2.filter2D(src=img, ddepth=cv2.CV_64F, kernel=kernel)

            # Resize and append
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            images.append(img)
            labels.append(category)

    return (images, labels)


def get_model():
    """
    Returns a compiled CNN model.
    """
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.5),

        tf.keras.layers.Dense(NUM_CATEGORIES, activation='softmax')
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    main()
