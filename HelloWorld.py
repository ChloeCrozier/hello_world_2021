from flask import Flask
import os
app = Flask(__name__)

dictionary ={
    "SC": ["solar", "89%", "72%", "64%"],
    "CA": ["wind", "83%", "79%", "12%"]
}


from flask import jsonify
@app.route('/numbers/')
def print_list():
    return jsonify(dictionary)

#port = os.environ.get('PORT')

app.run()