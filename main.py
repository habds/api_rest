from flask import Flask, jsonify
# from bdfalsa import productos
app = Flask(__name__)

@app.route('/')
def inicio():
    return 'hjola' #jsonify(productos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)