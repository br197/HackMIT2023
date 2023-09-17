from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission here (e.g., store the user's name and email)
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # You can add code here to process the data as needed

    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
