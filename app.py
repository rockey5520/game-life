from flask import Flask, render_template, request, redirect, url_for, flash
import json
import random
from individuals import Individual, Project

app = Flask(__name__)
app.secret_key = "god-simulation-secret"

WORLD_FILE = "world.json"

GOD = Individual(
    gender="divine",
    age=9999,
    personality="wise",
    nationality="cosmic",
    identity="god",
    growth_environment="heaven",
    skin_color="radiant",
    hair_color="silver",
    eye_color="gold"
)

projects = {
    "men": Project("Men"),
    "women": Project("Women"),
    "kids": Project("Kids")
}

# Partner fertility tracking
partner_state = {
    "men": {},
    "women": {}
}

def initialize_population():
    projects["men"].add_individual(Individual("male", 30, "bold", "Sparta", "warrior", "mountain", "tan", "black", "brown"))
    projects["men"].add_individual(Individual("male", 25, "funny", "Nordic", "bard", "village", "fair", "blonde", "blue"))
    projects["women"].add_individual(Individual("female", 28, "gentle", "Elven", "healer", "forest", "pale", "silver", "green"))
    projects["women"].add_individual(Individual("female", 22, "clever", "Desertian", "alchemist", "desert", "bronze", "black", "amber"))

def load_world():
    try:
        with open(WORLD_FILE, "r") as f:
            data = json.load(f)
            projects["men"].load_from_list(data.get("men", []))
            projects["women"].load_from_list(data.get("women", []))
            projects["kids"].load_from_list(data.get("kids", []))
            if projects["men"].size() == 0 and projects["women"].size() == 0:
                initialize_population()
    except FileNotFoundError:
        initialize_population()

def save_world():
    with open(WORLD_FILE, "w") as f:
        json.dump({
            "men": projects["men"].to_dict(),
            "women": projects["women"].to_dict(),
            "kids": projects["kids"].to_dict()
        }, f, indent=2)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html",
        god=GOD,
        men=projects["men"].list_all(),
        women=projects["women"].list_all(),
        kids=projects["kids"].list_all()
    )

@app.route("/mate", methods=["POST"])
def mate():
    group = request.form["group"]
    index = int(request.form["index"])
    key = f"{group}:{index}"

    if key not in partner_state[group]:
        partner_state[group][key] = {
            "clicks": 0,
            "threshold": random.randint(1, 5)
        }

    state = partner_state[group][key]
    state["clicks"] += 1

    if state["clicks"] >= state["threshold"]:
        partner = projects[group].get(index)
        baby = Individual(
            gender=random.choice(["male", "female"]),
            age=0,
            personality=random.choice([GOD.personality, partner.personality]),
            nationality=random.choice([GOD.nationality, partner.nationality]),
            identity=random.choice([GOD.identity, partner.identity]),
            growth_environment=random.choice([GOD.growth_environment, partner.growth_environment]),
            skin_color=random.choice([GOD.skin_color, partner.skin_color]),
            hair_color=random.choice([GOD.hair_color, partner.hair_color]),
            eye_color=random.choice([GOD.eye_color, partner.eye_color]),
        )
        projects["kids"].add_individual(baby)
        flash(f"🎉 A child was born with {group[:-1].capitalize()} #{index}!")
        partner_state[group][key] = {
            "clicks": 0,
            "threshold": random.randint(1, 5)
        }
        save_world()
    else:
        flash(f"⏳ Not ready yet! Try again... ({state['clicks']}/{state['threshold']})")

    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset():
    for k in projects:
        projects[k].individuals.clear()
    initialize_population()
    save_world()
    flash("🌍 World has been reset.")
    return redirect("/")

if __name__ == "__main__":
    load_world()
    app.run(debug=True)
