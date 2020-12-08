import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
feature_names = [
    'bedrooms', 
    'bathrooms',
    'furnished',
    'hasHeating',
    'parking',
    'hasGarage',
    'hasPetsAllowed',
    'Dishwasher',
    'Dryer',
    'Washer',
    'Refrigerator',
    'Range / Oven',
    'Microwave'
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():

    def convert_to_int(x):
        return 1 if x == 'on' else 0

    #raw_feature_values = request.form.values()
    raw_features = request.form

    features = []
    for feature_name in feature_names:
        if feature_name in raw_features.keys():
            feature_value = convert_to_int(raw_features[feature_name])
            features.append(feature_value)
        else:
            features.append(0)

 
    features_array = [np.array(features)]
    prediction = model.predict(features_array)

    output = int(prediction[0])

    return render_template('index.html', prediction_text='Estimated rental price is ${}/month'.format(output))


@app.route('/results', methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)