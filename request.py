import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'RHumidity':2, 'Temperature':9, 'Wind_speed':6, 'Solar_Irradiation':6})

print(r.json())
