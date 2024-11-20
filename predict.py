import numpy as np
import tensorflow as tf
from PIL import Image
from PilLite import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

class Predict:

    def __init__(self):
        self.interpreter = tf.lite.Interpreter(model_path='model041824_3.tflite')
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.tsr = ImageDataGenerator(rescale=1./255)
        self.class_labels = {0: 'Cardboard', 1: 'Food Organics', 2: 'glass', 3: 'metal', 4: 'paper', 5: 'plastic', 6: 'Vegetation'}
#         self.class_labels = {0: "Non-Biodegradable", 1:"Biodegradable"}

    def inference(self, frame):
        if isinstance(frame, str):
            # If frame is a file path, load the image directly
            img = image.load_img(frame, target_size=(224, 224))
        elif isinstance(frame, np.ndarray):
            # If frame is a numpy array, convert it to bytes and load using PIL
            img = Image.fromarray(frame)
            img = img.resize((224, 224))
        else:
            raise ValueError("Unsupported input type for 'frame'")

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = self.tsr.flow(x, batch_size=1)
        print(x)
        
        # Set model input
        input_data = next(x)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        
        # Perform inference
        self.interpreter.invoke()
        out = self.interpreter.get_tensor(self.output_details[0]['index'])
        final = np.argmax(out)
        label_name = self.class_labels.get(final, 'Unknown')
        print("Predicted class label:", label_name)  # Print the predicted class label
        print("Predicted class index:", final)
        
        global bio
        bio=[]
        global nonBio
        nonBio=[]
        
        if (final == 1) or (final == 6):
            bio.append(1)
            # print('\nLabel: Biodegradable')
        else:
            nonBio.append(0)
            # print('\nLabel: Non-Biodegradable')
        
        print(bio,'\n',nonBio)
        
        if len(bio) > len(nonBio):
            print('\nLabel: Biodegradable')
        else:
            print('\nLabel: Non-Biodegradable')

    def get_most_frequent_outcome(self, frames):
        results = [self.inference(frame) for frame in frames]
        most_frequent = max(set(results), key=results.count)
        label_name = self.class_labels.get(most_frequent, 'Unknown')

        print("Most frequent predicted class index:", most_frequent)
        print("Most frequent predicted class label:", label_name)
        return most_frequent, label_name