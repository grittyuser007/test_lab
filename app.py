from flask import Flask, request


app = Flask(__name__)
@app.route('/', methods=['POST'])
def home():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    return f"Hello, {name}! Your email is {email} and you are {age} years old."  
if __name__ == '__main__':
    app.run(debug=True)