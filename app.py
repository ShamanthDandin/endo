from flask import Flask, request, jsonify, render_template
import os
from classify import classify_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No image selected.'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No image selected.'}), 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        result = classify_image(file_path)
        return jsonify(result)
    return jsonify({'message': 'Error uploading image.'}), 500

if __name__ == '__main__':
    app.run(debug=True)


# list output 
# ask gpt how to return ourput from model 
#