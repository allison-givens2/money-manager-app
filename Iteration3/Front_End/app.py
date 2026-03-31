from flask import Flask, render_template, request, redirect, url_for
from budget import Budget
from transaction import Transaction
from sinking_fund import Sinking_Fund
from debt import Debt

app = Flask(__name__)
budget = Budget()

@app.route('/')
def home():
    return render_template(
        'home.html',
        categories=budget.get_categories(),
        transactions=budget.get_transactions(),
        sinking_funds=budget.get_sinking_funds(),
        debts=budget.get_debts()
    )

# Add a transaction
@app.route("/add-transaction", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]
        budget.add_transaction(amount, category, description, date)
        return redirect(url_for("home"))
    return render_template("add_transaction.html", categories=budget.get_categories())

# Set monthly income
@app.route("/set-income", methods=["GET", "POST"])
def set_income():
    if request.method == "POST":
        income = float(request.form["income"])
        budget.set_monthly_income(income)
        return redirect(url_for("home"))
    return render_template("set_income.html", current_income=budget.get_monthly_income())

# Add a category
@app.route("/add-category", methods=["GET", "POST"])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        limit = float(request.form['budget_limit'])
        budget.add_category(name, limit)
        return redirect(url_for('home'))
    return render_template('add_category.html')

# Add a sinking fund
@app.route('/add-sinking-fund', methods=['GET', 'POST'])
def add_sinking_fund():
    if request.method == 'POST':
        name = request.form['name']
        goal = float(request.form['goal'])
        budget.add_sinking_fund(name, goal, 0)
        return redirect(url_for('home'))
    return render_template('add_sinking_fund.html')

# Add a debt
@app.route('/add-debt', methods=['GET', 'POST'])
def add_debt():
    if request.method == 'POST':
        name = request.form['name']
        total = float(request.form['total'])
        budget.add_debt(name, total, 0)
        return redirect(url_for('home'))
    return render_template('add_debt.html')

if __name__ == '__main__':
    app.run(debug=True)