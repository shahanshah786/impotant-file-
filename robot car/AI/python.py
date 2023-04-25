# Artificial Intelligence" ke baare mein bataya hai. Is project mein hum AI ka use kar sakte hain jisse car accident se related information
# ko automatically process kar sake aur us information ko sahi jagah par forward kar sake.

# AI ke liye aap kisi bhi popular programming language jaise Python, Java, C++, MATLAB, R, etc. ka use kar sakte hain. Aap AI ke algorithms,
# tools aur techniques ka use karke apne application ko intelligent bana sakte hain.

# Kuch popular AI tools aur techniques hain:

# Machine Learning: Ye ek AI technique hai jisme computer systems ko data se sikhaya jaata hai aur phir wo data ko analyze karke
# decisions lete hain. Iske liye scikit-learn, TensorFlow, PyTorch, Keras jaise tools ka use kiya jaata hai.

# Natural Language Processing (NLP): Is technique ke use se computer ko human language ko samajhne aur interpret karne ki shakti milti hai.
# Iske liye NLTK, spaCy, Gensim jaise tools ka use kiya jaata hai.

# Computer Vision: Is technique se computer systems ko images aur videos ko analyze aur interpret karne ki shakti milti hai. Iske liye OpenCV, 
# TensorFlow, Keras jaise tools ka use kiya jaata hai.

# Deep Learning: Ye ek advanced form of Machine Learning hai jisme computer systems ko complex models ko sikhaya jaata hai. Iske liye TensorFlow,
# Keras, PyTorch jaise tools ka use kiya jaata hai.

# Is project mein, hum AI ka use karke car accident ke information ko analyze aur process karenge. Aap machine learning ka use kar sakte hain
# jisse system car accident ke information ko analyze kar sake aur us information ko police aur ambulance tak send kar sake.

# Ek example ke liye, hum Keras (Python library) ka use kar sakte hain. Keras mein hum image classification ke liye pre-trained models ka
# use kar sakte hain. Hum car accident ke images ko classify kar sakte hain aur phir us information ko forward kar sakte hain.

#python.py

from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the pre-trained model
model = load_model('car_accident_model.h5')

# Load the image and preprocess it
img = image.load_img('car_accident.jpg', target_size=(224, 224))
img = image.img_to_array(img)
img = np.expand_dims(img, axis=0)
img = preprocess_input(img)

# Predict the class of the image
pred = model.predict(img)

if pred[0][0] > 0.5:
    print("Car accident detected")
else:
    print("No car accident detected")

