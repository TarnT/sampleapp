from flask import Flask,render_template,request
from square import square
from word_break import reverse
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    errors = ""
    result = ""
    number = None
    if request.method == "POST":
        if request.form['number'] is not None:
            try:
                number = float(request.form["number"])
            except:
                    errors += f'Please Enter a Number'
            else:
                result = f'Square of {number} is {square(number)}'
    return render_template("calculate.html",solution=result, error_msg=errors)

@app.route('/reverse',methods=['GET','POST'])
def reversed():
    word_input,result  = None,None
    if request.method == 'POST': 
        word_input = request.form.get('word_input')
        result = f'Input: {word_input} Reverse: {reverse(word_input)}'
    return render_template('reverse.html',solution=result)




if __name__ == "__main__":
    app.run(debug=True)

