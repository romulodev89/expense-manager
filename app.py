from flask import Flask, render_template, request

app = Flask(__name__)

expenses = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        amount = float(request.form['amount'])  # Convertendo para float
        category = request.form['category']
        date = request.form['date']
        time = request.form['time']
        expense = {'description': description, 'amount': amount, 'category': category, 'date': date, 'time': time}
        expenses.append(expense)

    # Calculando o total das despesas
    total_expenses = sum(expense['amount'] for expense in expenses)

    return render_template('index.html', expenses=expenses, total_expenses=total_expenses)

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    del expenses[index]
    return render_template('index.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True)
