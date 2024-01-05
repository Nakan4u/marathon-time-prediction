import pandas as pd
from google.cloud import aiplatform
from pickle import load
from src.helpers import time_in_HHMMSS

# model = deployed, pretrained model
model = aiplatform.Endpoint(
    endpoint_name="projects/158192746313/locations/europe-west4/endpoints/6479153741646790656")

# Load the scaler from the bucket
sc = load(open('model/scaler.pkl', 'rb'))

def predictMarathonTime (age = 18, gender = 'male') :
  year = 2024

  if (age < 18) :
    print('You are too young to run')
    return
  elif (age > 80) :
    print('You are too old to run')
    return

  isMale = 1 if gender == 'male' else 0
  isFemale = 1 if gender == 'female' else 0

  # Створіть DataFrame для ваших нових даних
  new_data = pd.DataFrame({
      'year': [year],
      'age': [age],
      'gender_female': [isFemale],
      'gender_male': [isMale]
  })

  new_data_normalized = sc.transform(new_data)

  # this example to get predictions fron the deployed endpoint
  # convert to float32 list
  instances = new_data_normalized.tolist()
  predictions = model.predict(instances=instances).predictions[0][0]

  # Виведіть передбачення
  result = time_in_HHMMSS(predictions)
  print(result)
  
  return result