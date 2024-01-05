import vertexai
from vertexai.language_models import TextGenerationModel

def generatePlan(prompt):
  vertexai.init(project="marathon-time-prediction", location="europe-west4")
  parameters = {
      "candidate_count": 1,
      "max_output_tokens": 2048,
      "temperature": 0.9,
      "top_p": 1
  }
  model = TextGenerationModel.from_pretrained("text-bison")

  response = model.predict(
      prompt,
      **parameters
  )
  print(f"Response from Model: {response.text}")
  return response.text
  
  
