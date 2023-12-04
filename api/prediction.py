import keras
import numpy as np
import tensorflow 


def load_model(img):
    # global loaded_model
    # if loaded_model is None:
    with open("./prediction/model/model_architecture.json", "r") as f:
        model_architecture = f.read()
    loaded_model = keras.models.model_from_json(model_architecture)
    loaded_model.load_weights("./prediction/model/model_weights.h5")
    loaded_model = loaded_model
    print("done")
    IMG_HEIGHT = 96
    IMG_WIDTH = 96
    # Preprocess the image
    import io

    image_bytes = io.BytesIO()
    img.save(image_bytes, format='JPEG')
    image_bytes.seek(0)
    img = tensorflow.keras.preprocessing.image.load_img(image_bytes, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img = tensorflow.keras.preprocessing.image.img_to_array(img)
    print(img)
    img = img / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)

    prediction = loaded_model.predict(img)
    prediction = prediction.tolist()
    return{'prediction': prediction} 


