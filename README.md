# Marathon prediction app

This is a project to predict marathon time based on your age and gender.

App live demo here [link](https://martahon-prediction-app-uu77f463wa-ez.a.run.app/) application that renders a simple webpage.

## Get marathon time predictions
It used trained model based on Berlin marathon data for the last 49 years.
To get predictions you need provide your age and gender as query params:

[link](https://martahon-prediction-app-uu77f463wa-ez.a.run.app/predict?age=30&gender=male)

## Get marathon training plan
To get tranning plan within Google Vertex AI API, you need provide age, gender, amount of months  and assistant as a query params:

[link](https://martahon-prediction-app-uu77f463wa-ez.a.run.app/plan?age=30&gender=male&mounts=6&assistant=open-ai)