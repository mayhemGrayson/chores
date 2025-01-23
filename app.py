from flask import Flask, render_template
import web3

# you can run app.py to make sure you have web3
print(f"web3 version is: {web3.__version__}")

#standard flask instance
app = Flask(__name__)

# define route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)