from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
# from streamlit_cors import st_cors
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
# Use st_cors to enable CORS for your Streamlit app
# st_cors(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return render_template('index.html', filename=filename)

@app.route('/streamlit')
def streamlit():
    return render_template('streamlit_template.html')  # Use the template you created for Streamlit

if __name__ == '__main__':
    app.run(debug=True)
