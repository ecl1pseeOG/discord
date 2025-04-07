from flask import Flask, render_template

app = Flask(__name__)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/tos')
def tos():
    return render_template('tos.html')

@app.route('/dashboard')
def dashboard():
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)
