# 👼 God Simulation Web App

This is a fictional simulation game where you — as **God** — can create children by mating with individuals from the **Men** or **Women** population. Each child inherits a mix of traits from God and the chosen partner.

The web app gives you a visual interface to explore, click, mate, and watch your divine offspring grow.

---

## 🌟 Features

- 👨‍🦱 View all Men and Women with detailed traits
- 👶 View all Kids born from divine unions
- 🧬 Traits are randomly inherited from God and partner
- 🎲 Fertility randomness: each partner requires 1–5 attempts before producing a child
- 🔔 Notifications:
  - “Try again...” when not yet fertile
  - “A child was born!” when successful
- 🗑️ Reset world anytime to start fresh

---

## 🔧 Tech Stack

- **Python 3.10+**
- **Flask** (backend web server)
- **Jinja2** (HTML templating)
- **Bootstrap 5** (UI styling)
- **JSON** (`world.json` for persistence)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/god-simulation-webapp.git
cd god-simulation-webapp
2. Install dependencies
bash
Copy
Edit
pip install flask
3. Run the app
bash
Copy
Edit
python app.py
4. Visit in browser
Open your browser and go to:

arduino
Copy
Edit
http://localhost:5000
📁 Project Structure
bash
Copy
Edit
god-simulation-webapp/
├── app.py               # Main Flask server
├── individuals.py       # Models for Individual and Project
├── world.json           # Stores simulation data (auto-generated)
└── templates/
    └── index.html       # UI template
📸 Demo Screenshot (optional)
Add a screenshot here if needed (use fakeimg.pl or local preview)

🧪 How to Play
Open the app and browse the list of men and women.

Click “Mate with God” under any individual.

Watch the notification:

⏳ “Not ready yet!” if the partner needs more attempts

🎉 “A child was born!” when the threshold is met

View new children in the Kids column.

Click “Reset World” to start over.