from io import BytesIO
import numpy as np
import tensorflow as tf
from fastapi import FastAPI,File,UploadFile
import uvicorn
from PIL import Image

#Define Function
labels = ['fmd_gum', 'healthy_gum']

def process(file)-> Image.Image:
    image = image = Image.open(BytesIO(file))
    return image

def predict1(image: Image.Image):
    loaded_model = tf.keras.models.load_model('model_gum_v2.h5')
    image = tf.image.resize(np.array(image), (150,150))
    image = Image.fromarray(np.uint8(image.numpy()))
    image = image.convert("RGB")
    image = np.expand_dims(np.array(image)/255,0)

    classes = loaded_model.predict(image)
    percent = "{:.2f}".format(100 - classes[0][0]*100)
    if classes[0]>0.5:
        string = "Sapi Anda tidak mengalami gejala PMK berdasarkan pemindaian pada gusi."
    else:
        string = "Sapi Anda memiliki kemungkinan mengalami PMK berdasarkan gejala pada gusi sebesar " + percent + "%."
    return string

def predict2(image: Image.Image):
    loaded_model = tf.keras.models.load_model('inc_model_tongue.h5')
    image = tf.image.resize(np.array(image), (150,150))
    image = Image.fromarray(np.uint8(image.numpy()))
    image = image.convert("RGB")
    image = np.expand_dims(np.array(image)/255,0)

    classes = loaded_model.predict(image)
    percent = "{:.2f}".format(100 - classes[0][0]*100)
    if classes[0]>0.5:
        string = "Sapi Anda tidak mengalami gejala PMK berdasarkan pemindaian pada lidah."
    else:
        string = "Sapi Anda memiliki kemungkinan mengalami PMK berdasarkan gejala pada lidah sebesar " + percent + "%."
    return string

def predict3(image: Image.Image):
    loaded_model = tf.keras.models.load_model('inc_model_feet.h5')
    image = tf.image.resize(np.array(image), (150,150))
    image = Image.fromarray(np.uint8(image.numpy()))
    image = image.convert("RGB")
    image = np.expand_dims(np.array(image)/255,0)

    classes = loaded_model.predict(image)
    percent = "{:.2f}".format(100 - classes[0][0]*100)
    if classes[0]>0.5:
        string = "Sapi Anda tidak mengalami gejala PMK berdasarkan pemindaian pada kaki."
    else:
        string = "Sapi Anda memiliki kemungkinan mengalami PMK berdasarkan gejala pada kaki sebesar " + percent + "%."
    return string

def predict4(image: Image.Image):
    loaded_model = tf.keras.models.load_model('inc_model_saliva.h5')
    image = tf.image.resize(np.array(image), (150,150))
    image = Image.fromarray(np.uint8(image.numpy()))
    image = image.convert("RGB")
    image = np.expand_dims(np.array(image)/255,0)

    classes = loaded_model.predict(image)
    percent = "{:.2f}".format(100 - classes[0][0]*100)
    if classes[0]>0.5:
        string = "Sapi Anda tidak mengalami gejala PMK berdasarkan pemindaian pada air liur."
    else:
        string = "Sapi Anda memiliki kemungkinan mengalami PMK berdasarkan gejala pada air liur sebesar " + percent + "%."
    return string

app = FastAPI()

@app.post("/predict/gum")
async def predict_fastapi(file: UploadFile = File(...)):
    image = process(await file.read())
    prediction = predict1(image)
    return prediction

@app.post("/predict/tongue")
async def predict_fastapi(file: UploadFile = File(...)):
    image = process(await file.read())
    prediction = predict2(image)
    return prediction

@app.post("/predict/feet")
async def predict_fastapi(file: UploadFile = File(...)):
    image = process(await file.read())
    prediction = predict3(image)
    return prediction

@app.post("/predict/saliva")
async def predict_fastapi(file: UploadFile = File(...)):
    image = process(await file.read())
    prediction = predict4(image)
    return prediction


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3001)
