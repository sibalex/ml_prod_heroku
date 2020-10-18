import requests

res = requests.post(
    url='http://localhost:5000/predict',
    json={
        'sepal_length': 5.0,
        'sepal_width': 3.2,
        'petal_length': 1.5,
        'petal_width': 0.3
    }
)

res

res.json()
