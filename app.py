from flask import Flask, send_from_directory, render_template

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/img/<path:filename>')
def index2(filename):
    return send_from_directory('static/img', filename)

@app.route('/css/<string:stylesheet>')
def rout_css(stylesheet):
    return send_from_directory('static/css', stylesheet)

if __name__ == "__main__":
    app.run(debug=True)
