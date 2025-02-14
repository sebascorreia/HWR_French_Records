from tensorflow.keras.preprocessing.image import ImageDataGenerator
def train(image_folder):
    datagen = ImageDataGenerator(rescale=1./255)