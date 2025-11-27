from flask import Flask, request


app = Flask(__name__)
@app.route('/', methods=['POST'])
def home():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Hello, {name}! Your email is {email}."  
if __name__ == '__main__':
    app.run(debug=True)