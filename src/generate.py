import vertexai
from vertexai.language_models import TextGenerationModel
import os
from openai import OpenAI

def generatePlan(prompt):
  vertexai.init(project="marathon-time-prediction", location="europe-west4")
  parameters = {
      "candidate_count": 1,
      "max_output_tokens": 2048,
      "temperature": 0.5,
      "top_p": 1
  }
  model = TextGenerationModel.from_pretrained("text-bison")

  response = model.predict(
      prompt,
      **parameters
  )
  return response.text

def generatePlanWithOpenAI(systemContent, userContent):
  client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
  )

  completion = client.chat.completions.create(
    model="gpt-4",
    temperature= "0.5",
    messages=[
      {"role": "system", "content": systemContent},
      {"role": "user", "content": userContent}
    ]
  )
  
  result = completion.choices[0].message.content
  
  return result