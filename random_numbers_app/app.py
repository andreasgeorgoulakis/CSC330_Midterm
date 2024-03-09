from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_numbers():
    try:
        n = int(request.form['number_of_numbers'])
        numbers = random.sample(range(1, 1000), n)  # Generate n random numbers between 1 and 100
        return render_template('results.html', numbers=numbers)
    except ValueError:
        return "Please enter a valid integer."

if __name__ == "__main__":
    app.run(debug=True)
