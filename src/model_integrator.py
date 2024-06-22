from flask import Flask, request, jsonify

app = Flask(__name__)

# Загрузка обученной модели
model = tf.keras.models.load_model('path_to_saved_model')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction[0][0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
