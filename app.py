from flask import Flask, render_template, url_for, send_from_directory

# Changed template_folder back to 'index'
app = Flask(__name__, template_folder='index')

@app.route('/profile_img.jpeg')
def serve_profile_image():
    return send_from_directory('.', 'profile_img.jpeg', mimetype='image/jpeg')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)