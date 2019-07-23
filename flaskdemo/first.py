from flask import Flask, render_template,request
app = Flask(__name__)


@app.route('/insertion/',methods=['POST'])
def insert():
   print("running")
   result = request.form
   print result
   return render_template('next.html')

@app.route('/nextpage/')
def nextpg():
   return render_template('next.html')

@app.route('/details/<string:data>')
def details(data):
   print(data)
   return data

@app.route('/')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)
