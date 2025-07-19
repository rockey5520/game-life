import argparse
import random
import json
from individuals import Individual, Project

WORLD_FILE = "world.json"

# You are God
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

# Projects
projects = {
    "men": Project("Men"),
    "women": Project("Women"),
    "kids": Project("Kids")
}

def initialize_population():
    if projects["men"].size() == 0:
        projects["men"].add_individual(Individual("male", 30, "bold", "Sparta", "warrior", "mountain", "tan", "black", "brown"))
        projects["men"].add_individual(Individual("male", 25, "funny", "Nordic", "bard", "village", "fair", "blonde", "blue"))
    if projects["women"].size() == 0:
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

def list_project(args):
    proj = projects[args.project]
    for idx, ind in enumerate(proj.list_all()):
        print(f"[{idx}] {ind}")

def god_mate(args):
    target_group = projects[args.group]
    partner = target_group.get(args.index)

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
    print(f"👶 A child was born from God + {args.group[:-1].capitalize()}[{args.index}]: {baby}")

def reset_world(args):
    for k in ["men", "women", "kids"]:
        projects[k].individuals.clear()
    initialize_population()
    print("🌍 World has been reset to default state.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fictional God Simulation CLI")

    subparsers = parser.add_subparsers(dest="command")

    # List
    list_cmd = subparsers.add_parser("list")
    list_cmd.add_argument("project", choices=["men", "women", "kids"])
    list_cmd.set_defaults(func=list_project)

    # Mate
    mate = subparsers.add_parser("mate")
    mate.add_argument("group", choices=["men", "women"])
    mate.add_argument("index", type=int)
    mate.set_defaults(func=god_mate)

    # Reset
    reset = subparsers.add_parser("reset")
    reset.set_defaults(func=reset_world)

    # Run
    args = parser.parse_args()
    load_world()
    if hasattr(args, "func"):
        args.func(args)
        save_world()
    else:
        parser.print_help()
