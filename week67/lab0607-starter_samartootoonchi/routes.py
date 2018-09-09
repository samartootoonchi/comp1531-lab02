from server import app, valid_time
from flask import request, render_template
from Calculator import Calculator


@app.route('/', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        if not valid_time(int(request.form['time_interest'])):
            return render_template('interest_form.html', calc_total=True,message ='Error')
        else:
            result = Calculator(int(request.form['amount invested']), int(request.form['interest rate']))
            total = result.total_interest(int(request.form['time_interest']))
            return render_template('interest_form.html', total = total, calc_total = True)
    return render_template('interest_form.html', calc_total=True)


@app.route('/time', methods=['POST', 'GET'])
def time_interest():
    if request.method == 'POST':
        result = Calculator(int(request.form['amount invested']),  int(request.form['interest rate']))
        time = result.time_required (int(request.form['calc total']))
        return render_template('interest_form.html', time_interest = time, calc_total = False)
    return render_template('interest_form.html', calc_total=False)


@app.route('/credits', methods=['GET'])
def credits():
    
    return render_template('credits.html',name = 'Samar')
