import numpy as np
import matplotlib.pyplot as plt
import keras
import cv2

model = keras.models.load_model('trained_models/modelTest.h5')

def get_letter(pred):
    if pred < 9:
        return chr(65 + pred)
    else :
        return chr(66 + pred)

def reshape_real_image(file_path):
    # Charger l'image
    image = cv2.imread(file_path)
    # Redimensionner l'image
    image = cv2.resize(image, (28, 28))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Normaliser l'image
    image = image / 255
    image = image.reshape(-1, 28, 28, 1)
    return image

# Luminosité 
labels = ["Normal","High Luminosity", "Low Luminosity", "Zoom", "Left rotation", "Right rotation","White bg","Dark bg"]

fig, axes = plt.subplots(nrows=1, ncols=8, figsize=(12, 7))
for i, ax in enumerate(axes):
    image = reshape_real_image("data/limites/R" + str(i+1) + ".jpg")
    pred = model.predict(image)
    pred = np.argmax(pred,axis = 1)
    ax.imshow(image.reshape(28,28), cmap=plt.get_cmap('gray'))
    ax.set_title(get_letter(pred[0]))
    ax.set_axis_off()
    print("Classification: ", get_letter(pred[0]))
    ax.text(14,32,labels[i],horizontalalignment='center',verticalalignment='center')
plt.show()
