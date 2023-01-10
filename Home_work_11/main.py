from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def get_list_of_candidates():
    candidates = utils.load_candidates()

    return render_template('list.html', candidates=candidates)


@app.route('/candidates/<int:id>')
def get_candidates(id):
    candidate = utils.get_candidates_by_id(id)

    return render_template("card.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def get_candidates_by_name(name):
    candidate = utils.get_candidates_by_name(name)

    return render_template("search.html", candidate=candidate, count_candidates=len(candidate))

@app.route('/skill/<skill_name>')
def get_candidates_by_skill(skill):
    candidate = utils.get_candidates_by_skill(skill.lower())

    return render_template("skill.html", candidate=candidate, count_candidates=len(candidate))

app.run(debug=True)
