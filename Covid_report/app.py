from flask import Flask, render_template, request
from analytic import *
import datetime as dt


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/covid_analytics", methods=["POST"])
def covid_analytics():

    s_date = request.form.get("start-date")
    e_date = request.form.get("end-date")
    death, cured, confirm = stats(e_date)

    return render_template("landing_page.html", S_date = s_date, E_date=e_date, Death=death, Cured=cured, Confirmed=confirm,
                           Table=table(e_date),Piechart=piechart(e_date), MaxCase=max_cases(e_date), LowestCase=lowest_cases(e_date),
                           HighImpactConfirmed=high_impact_confirmed(e_date), HighImpactCured=high_impact_cured(e_date),
                           HighImpactDeath=high_impact_death(e_date),
                           LineGraph=line_graph(e_date), LowestImpactConfirm = lowest_impact_confirmed(e_date))


app.config["DEBUG"] = True

if __name__ == '__main__':
    app.run(debug=True)
