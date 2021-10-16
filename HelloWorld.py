from flask import Flask
app = Flask(__name__)

dictionary ={
    "SC": ["solar", "89%", "72%", "64%"],
    "CA": ["wind", "83%", "79%", "12%"]
}
      
# Data to be written 
# dictionary ={ 
#   "id": "04", 
#   "name": "sunil", 
#   "department": "HR"
# } 

# arr = [dictionary, dictionary]

from flask import jsonify
@app.route('/numbers/')
def print_list():
    return jsonify(dictionary)

app.run()