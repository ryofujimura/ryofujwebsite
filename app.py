from flask import Flask, render_template
from urllib.parse import quote as url_quote

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {'title': 'Honda', 'image': 'honda.svg', 'description': 'Data management and analysis'},
        {'title': 'Project 2', 'image': 'image2.png', 'description': 'Description of Project 2'},
        # Add as many projects as you like
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
