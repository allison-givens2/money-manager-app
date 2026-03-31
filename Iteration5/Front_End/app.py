from flask import Flask, render_template, request, redirect, url_for
from budget import Budget
import os
from datetime import datetime, timedelta

app = Flask(__name__, template_folder="templates")
app.secret_key = "super_secret_key"
ACTIVE_FILE = None
budget = None

# === Directory setup ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)


# === 1. Budget path helper ===
def get_budget_filename(year, month):
    return os.path.join(DATA_DIR, f"budget_{year}_{month:02}.json")


# === 2. Autoload and rollover ===
def autoload_budget():
    """
    Load current month if present.
    If missing, roll over last month into a new file; THEN reload from disk.
    If nothing exists, create fresh current month; THEN reload from disk.
    """
    global budget, ACTIVE_FILE

    now = datetime.now()
    current_name = get_budget_filename(now.year, now.month)

    # Case 1: current month exists
    if os.path.exists(current_name):
        budget = Budget.load_from_file(current_name)
        ACTIVE_FILE = current_name
        return

    # Case 2: try last month
    first_of_month = now.replace(day=1)
    last_month_end = first_of_month - timedelta(days=1)
    prev_name = get_budget_filename(last_month_end.year, last_month_end.month)

    if os.path.exists(prev_name):
        prev = Budget.load_from_file(prev_name)
        rolled = Budget.rollover(prev)
        rolled.save_to_file(current_name)
        budget = Budget.load_from_file(current_name)
        ACTIVE_FILE = current_name
        return

    # Case 3: nothing found — create fresh
    empty = Budget()
    empty.save_to_file(current_name)
    budget = Budget.load_from_file(current_name)
    ACTIVE_FILE = current_name

# 4
@app.route("/")
def home():
    global budget, ACTIVE_FILE
    if budget is None or ACTIVE_FILE is None:
        autoload_budget()
        if budget is None or ACTIVE_FILE is None:
            return redirect(url_for("startup"))

    total_spent = budget.get_total_spent()
    remaining = budget.get_remaining_budget()
    summary = budget.get_summary_by_category()
    debts = budget.get_debts()
    funds = budget.get_sinking_funds()
    income = budget.get_monthly_income()

    categories = []
    for cat in budget.get_categories():
        spent = cat.get_spent_amount(budget.get_transactions())
        limit = cat.get_budget_limit()
        cat_remaining = limit - spent
        categories.append({
            "name": cat.get_name(),
            "spent": spent,
            "limit": limit,
            "remaining": cat_remaining
        })

    category_names = [c["name"] for c in categories]
    category_spent = [c["spent"] for c in categories]

    return render_template(
        "home.html",
        total_spent=total_spent,
        remaining=remaining,
        summary=summary,
        debts=debts,
        funds=funds,
        transactions=budget.get_transactions(),
        categories=categories,
        current_file=ACTIVE_FILE,
        budget_loaded=True,
        income=income,
        category_names=category_names,
        category_spent=category_spent
    )


# 5
@app.route("/add-transaction", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]
        budget.add_transaction(amount, category, description, date)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("add_transaction.html", categories=budget.get_categories())

# 6
@app.route("/set-income", methods=["GET", "POST"])
def set_income():
    if request.method == "POST":
        income = float(request.form["income"])
        budget.set_monthly_income(income)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("set_income.html", current_income=budget.get_monthly_income())

# 7
@app.route("/add-category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        name = request.form["name"]
        limit = float(request.form["limit"])
        budget.add_category(name, limit)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("add_category.html")

# 8
@app.route("/add-fund", methods=["GET", "POST"])
def add_fund():
    if request.method == "POST":
        name = request.form["name"]
        goal = float(request.form["goal"])
        amount = float(request.form["amount"])
        budget.add_sinking_fund(name, goal, amount)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("add_sinking_fund.html")

# 9
@app.route("/add-debt", methods=["GET", "POST"])
def add_debt():
    if request.method == "POST":
        name = request.form["name"]
        total = float(request.form["total"])
        paid = float(request.form["paid"])
        budget.add_debt(name, total, paid)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("add_debt.html")

# 10
@app.route("/category-summary", methods=["GET", "POST"])
def category_summary():
    if request.method == "POST":
        category = request.form["category"]
        summary = budget.get_category_summary(category)
        budget.save_to_file(ACTIVE_FILE)
        return render_template("category_summary.html", summary=summary)
    return render_template("category_form.html", categories=budget.get_categories())

# 11
@app.route("/delete-transaction", methods=["GET", "POST"])
def delete_transaction():
    if request.method == "POST":
        index = int(request.form["index"])
        budget.delete_transaction_by_index(index)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    choices = budget.get_transaction_choices()
    return render_template("delete_transaction.html", choices=choices)

# 12
@app.route("/edit-transaction", methods=["GET", "POST"])
def edit_transaction_select():
    if request.method == "POST":
        return redirect(url_for("edit_transaction_form", index=request.form["index"]))
    choices = budget.get_transaction_choices()
    return render_template("edit_transaction_select.html", choices=choices)

# 13
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
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    categories = budget.get_categories()
    return render_template("edit_transaction_form.html",
                           transaction=transaction, index=index, categories=categories)

# 14
@app.route("/delete-debt", methods=["GET", "POST"])
def delete_debt():
    if request.method == "POST":
        index = int(request.form["index"])
        budget.delete_debt_by_index(index)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    choices = budget.get_debt_choices()
    return render_template("delete_debt.html", choices=choices)

# 15
@app.route("/edit-debt", methods=["GET", "POST"])
def edit_debt_select():
    if request.method == "POST":
        return redirect(url_for("edit_debt_form", index=request.form["index"]))
    choices = budget.get_debt_choices()
    return render_template("edit_debt_select.html", choices=choices)

# 16
@app.route("/edit-debt/<int:index>", methods=["GET", "POST"])
def edit_debt_form(index):
    debt = budget.get_debt_by_index(index)
    if not debt:
        return redirect(url_for("edit_debt_select"))
    if request.method == "POST":
        debt.set_total_amount(float(request.form["total"]))
        debt.set_amount_paid(float(request.form["paid"]))
        budget.save_to_file(ACTIVE_FILE)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("edit_debt_form.html", debt=debt, index=index)

# 17
@app.route("/delete-fund", methods=["GET", "POST"])
def delete_fund():
    if request.method == "POST":
        index = int(request.form["index"])
        budget.delete_sinking_fund_by_index(index)
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    choices = budget.get_fund_choices()
    return render_template("delete_fund.html", choices=choices)

# 18
@app.route("/edit-fund", methods=["GET", "POST"])
def edit_fund_select():
    if request.method == "POST":
        return redirect(url_for("edit_fund_form", index=request.form["index"]))
    choices = budget.get_fund_choices()
    return render_template("edit_fund_select.html", choices=choices)

# 19
@app.route("/edit-fund/<int:index>", methods=["GET", "POST"])
def edit_fund_form(index):
    fund = budget.get_sinking_fund_by_index(index)
    if not fund:
        return redirect(url_for("edit_fund_select"))
    if request.method == "POST":
        fund.set_goal_amount(float(request.form["goal"]))
        fund.set_current_amount(float(request.form["amount"]))
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))
    return render_template("edit_fund_form.html", fund=fund, index=index)

# 20
@app.route("/edit-category", methods=["GET", "POST"])
def edit_category_select():
    if request.method == "POST":
        return redirect(url_for("edit_category_form", name=request.form["category"]))
    categories = budget.get_categories()
    return render_template("edit_category_select.html", categories=categories)

# 21
@app.route("/edit-category/<name>", methods=["GET", "POST"])
def edit_category_form(name):
    category = budget.get_category_by_name(name)
    if not category:
        return redirect(url_for("edit_category_select"))
    if request.method == "POST":
        budget.save_to_file(ACTIVE_FILE)
        category.set_budget_limit(float(request.form["limit"]))
        return redirect(url_for("home"))
    return render_template("edit_category_form.html", category=category)

# 25
@app.route("/transactions")
def view_transactions():
    return render_template("transactions.html", transactions=budget.get_transactions())

# 26
@app.route("/categories")
def view_categories():
    categories = []
    for cat in budget.get_categories():
        spent = cat.get_spent_amount(budget.get_transactions())
        limit = cat.get_budget_limit()
        remaining = limit - spent
        categories.append({
            "name": cat.get_name(),
            "limit": limit,
            "spent": spent,
            "remaining": remaining
        })
    return render_template("categories.html", categories=categories)

# 27
@app.route("/debts")
def view_debts():
    debts = []
    for d in budget.get_debts():
        total = d.get_total_amount()
        paid = d.get_amount_paid()
        remaining = total - paid
        debts.append({
            "name": d.get_name(),
            "total": total,
            "paid": paid,
            "remaining": remaining
        })
    return render_template("debts.html", debts=debts)

# 28
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

# 29
@app.route("/pay_debt/<int:index>", methods=["GET", "POST"])
def pay_debt(index):
    debts = budget.get_debts()

    # invalid index -> just go home
    if index < 0 or index >= len(debts):
        return redirect(url_for("home"))

    debt = debts[index]

    if request.method == "POST":
        # get amount
        try:
            amount = float(request.form.get("amount", 0))
        except ValueError:
            return redirect(request.url)

        # must be positive
        if amount <= 0:
            return redirect(request.url)

        remaining = debt.get_total_amount() - debt.get_amount_paid()

        # don't allow overpaying
        if amount > remaining:
            return redirect(request.url)

        # apply payment
        debt.set_amount_paid(debt.get_amount_paid() + amount)

        # just go back home
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))

    return render_template("pay_debt.html", debt=debt, index=index)

#30
@app.route("/contribute-fund/<int:index>", methods=["GET", "POST"])
def contribute_fund(index):
    funds = budget.get_sinking_funds()

    if index < 0 or index >= len(funds):
        return redirect(url_for("home"))

    fund = funds[index]

    if request.method == "POST":
        # parse amount
        try:
            amount = float(request.form.get("amount", 0))
        except ValueError:
            return redirect(request.url)

        # must be positive
        if amount <= 0:
            return redirect(request.url)

        # apply contribution
        fund.add_contribution(amount)

        # return home
        budget.save_to_file(ACTIVE_FILE)
        return redirect(url_for("home"))

    return render_template("contribute_fund.html", fund=fund, index=index)
