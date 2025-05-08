from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load('music_recommender.joblib')

class UserInput(BaseModel):
    age: int
    gender: int

@app.post('/predict')
def predict(user_input: UserInput):
    prediction = model.predict([[user_input.age, user_input.gender]])
    return {'genre': prediction[0]}