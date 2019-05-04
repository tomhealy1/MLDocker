#Created on 4/5/2019






#import the package and request method
from flask import Flask, request
#app name =
app = Flask(__name__)

#the slash is the url
@app.route('/hello_world', methods=['GET', 'POST'])
def add():
    #a=request.form["a"]
    #b=request.form["b"]
    #c=request.form["c"]
    return "Hello World" #str( int(a) + int(b) + int(c))

#ef predict(house_size, house_beds):
 #   prediction =ml_model.predict(house_size, house_beds)
  #  return prediction

if __name__=='__main__':
    app.run(port=7000)

