from flask import Flask, render_template, request, redirect, url_for
from budget import Budget
from category import Category
from transaction import Transaction
from sinking_fund import SinkingFund
from debt import Debt

app = Flask(__name__, template_folder="templates")
app.secret_key = "super_secret_key"

budget = Budget()

@app.route("/")
def home():
    total_spent = budget.get_total_spent()
    remaining = budget.get_remaining_budget()
    debts = budget.get_debts()
    funds = budget.get_sinking_funds()
    income = budget.get_monthly_income()

    categories = []
    for cat in budget.get_categories():
        spent = cat.get_spent_amount(budget.get_transactions())
        limit = cat.get_budget_limit()
        categories.append({
            "name": cat.get_name(),
            "spent": spent,
            "limit": limit,
            "remaining": limit - spent
        })

    category_names = [c["name"] for c in categories]
    category_spent = [c["spent"] for c in categories]

    return render_template(
        "home.html",
        total_spent=total_spent,
        remaining=remaining,
        debts=debts,
        funds=funds,
        transactions=budget.get_transactions(),
        categories=categories,
        income=income,
        category_names=category_names,
        category_spent=category_spent
    )

@app.route("/add-transaction", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]
        budget.add_transaction(Transaction(amount, category, description, date))
        return redirect(url_for("home"))
    return render_template("add_transaction.html", categories=budget.get_categories())

@app.route("/set-income", methods=["GET", "POST"])
def set_income():
    if request.method == "POST":
        income = float(request.form["income"])
        budget.set_monthly_income(income)
        return redirect(url_for("home"))
    return render_template("set_income.html", current_income=budget.get_monthly_income())

@app.route("/add-category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        name = request.form["name"]
        limit = float(request.form["limit"])
        budget.add_category(name, limit)
        return redirect(url_for("home"))
    return render_template("add_category.html")

@app.route("/add-fund", methods=["GET", "POST"])
def add_fund():
    if request.method == "POST":
        name = request.form["name"]
        goal = float(request.form["goal"])
        amount = float(request.form["amount"])
        budget.add_sinking_fund(name, goal, amount)
        return redirect(url_for("home"))
    return render_template("add_sinking_fund.html")

@app.route("/add-debt", methods=["GET", "POST"])
def add_debt():
    if request.method == "POST":
        name = request.form["name"]
        total = float(request.form["total"])
        paid = float(request.form["paid"])
        budget.add_debt(name, total, paid)
        return redirect(url_for("home"))
    return render_template("add_debt.html")

@app.route("/category-summary", methods=["GET", "POST"])
def category_summary():
    if request.method == "POST":
        category = request.form["category"]
        summary = budget.get_category_summary(category)
        return render_template("category_summary.html", summary=summary)
    return render_template("category_form.html", categories=budget.get_categories())

@app.route("/delete-transaction", methods=["GET", "POST"])
def delete_transaction():
    if request.method == "POST":
        index = int(request.form["index"])
        budget.delete_transaction_by_index(index)
        return redirect(url_for("home"))
    return render_template("delete_transaction.html", choices=budget.get_transaction_choices())

@app.route("/edit-transaction", methods=["GET", "POST"])
def edit_transaction_select():
    if request.method == "POST":
        return redirect(url_for("edit_transaction_form", index=request.form["index"]))
    return render_template("edit_transaction_select.html", choices=budget.get_transaction_choices())

@app.route("/edit-transaction/<int:index>", methods=["GET", "POST"])
def edit_transaction_form(index):
    transaction = budget.get_transaction_by_index(index)
    if not transaction:
        return redirect(url_for("edit_transaction_select"))
    if request.method == "POST":
        transaction.set_amount(float(request.form["amount"]))
        transaction.set_category(request.form["category"])
        transaction.set_description(request.form["description"])
        transaction.set_date(request.form["date"])
        return redirect(url_for("home"))
    return render_template("edit_transaction_form.html", transaction=transaction, index=index, categories=budget.get_categories())

@app.route("/delete-debt", methods=["GET", "POST"])
def delete_debt():
    if request.method == "POST":
        index = int(request.form["index"])
        budget.delete_debt_by_index(index)
        return redirect(url_for("home"))
    return render_template("delete_debt.html", choices=budget.get_debt_choices())

@app.route("/edit-debt", methods=["GET", "POST"])
def edit_debt_select():
    if request.method == "POST":
        return redirect(url_for("edit_debt_form", index=request.form["index"]))
    return render_template("edit_debt_select.html", choices=budget.get_debt_choices())

@app.route("/edit-debt/<int:index>", methods=["GET", "POST"])
def edit_debt_form(index):
    debt = budget.get_debt_by_index(index)
    if not debt:
        return redirect(url_for("edit_debt_select"))
    if request.method == "POST":
        debt.set_total_amount(float(request.form["total"]))
        debt.set_amount_paid(float(request.form["paid"]))
        return redirect(url_for("home"))
    return render_template("edit_debt_form.html", debt=debt, index=index)

@app.route("/delete-fund", methods=["GET", "POST"])
def delete_fund():
    if request.method == "POST":
        index = int(request.form["index"])
        budget.delete_sinking_fund_by_index(index)
        return redirect(url_for("home"))
    return render_template("delete_fund.html", choices=budget.get_fund_choices())

@app.route("/edit-fund", methods=["GET", "POST"])
def edit_fund_select():
    if request.method == "POST":
        return redirect(url_for("edit_fund_form", index=request.form["index"]))
    return render_template("edit_fund_select.html", choices=budget.get_fund_choices())

@app.route("/edit-fund/<int:index>", methods=["GET", "POST"])
def edit_fund_form(index):
    fund = budget.get_sinking_fund_by_index(index)
    if not fund:
        return redirect(url_for("edit_fund_select"))
    if request.method == "POST":
        fund.set_goal_amount(float(request.form["goal"]))
        fund.set_current_amount(float(request.form["amount"]))
        return redirect(url_for("home"))
    return render_template("edit_fund_form.html", fund=fund, index=index)

@app.route("/edit-category", methods=["GET", "POST"])
def edit_category_select():
    if request.method == "POST":
        return redirect(url_for("edit_category_form", name=request.form["category"]))
    return render_template("edit_category_select.html", categories=budget.get_categories())

@app.route("/edit-category/<name>", methods=["GET", "POST"])
def edit_category_form(name):
    category = budget.get_category_by_name(name)
    if not category:
        return redirect(url_for("edit_category_select"))
    if request.method == "POST":
        category.set_budget_limit(float(request.form["limit"]))
        return redirect(url_for("home"))
    return render_template("edit_category_form.html", category=category)

@app.route("/transactions")
def view_transactions():
    return render_template("transactions.html", transactions=budget.get_transactions())

@app.route("/categories")
def view_categories():
    categories = []
    for cat in budget.get_categories():
        spent = cat.get_spent_amount(budget.get_transactions())
        limit = cat.get_budget_limit()
        categories.append({
            "name": cat.get_name(),
            "limit": limit,
            "spent": spent,
            "remaining": limit - spent
        })
    return render_template("categories.html", categories=categories)

@app.route("/debts")
def view_debts():
    debts = []
    for d in budget.get_debts():
        total = d.get_total_amount()
        paid = d.get_amount_paid()
        debts.append({
            "name": d.get_name(),
            "total": total,
            "paid": paid,
            "remaining": total - paid
        })
    return render_template("debts.html", debts=debts)

@app.route("/funds")
def view_funds():
    funds = []
    for f in budget.get_sinking_funds():
        funds.append({
            "name": f.get_name(),
            "goal": f.get_goal_amount(),
            "saved": f.get_current_amount(),
            "percent": f.get_percent_saved()
        })
    return render_template("funds.html", funds=funds)

if __name__ == "__main__":
    app.run(debug=True)