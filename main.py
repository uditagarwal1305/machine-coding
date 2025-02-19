from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data based on the provided table in the PDF
plans = [
    {
        "category": "Athleticism",
        "activity": "Advanced Mobility exercises",
        "frequency": "Maximize",
        "time": "Max.",
        "suggested_days": ["D14", "D15", "D16", "D17", "D18", "D19", "D20"]
    },
    {
        "category": "Boosters",
        "activity": "Knowledge Boosters (Follow daily plans)",
        "frequency": "2x/Day",
        "time": "30 sec",
        "suggested_days": ["D14", "D15", "D16", "D17", "D18", "D19", "D20"]
    },
    {
        "category": "Music",
        "activity": "Visual Soflege",
        "frequency": "1x/Day",
        "time": "30 sec",
        "suggested_days": ["D14", "D15", "D16", "D17", "D18", "D19", "D20"]
    },
    {
        "category": "Memory",
        "activity": "Auditory Memory 2",
        "frequency": "1x/Day",
        "time": "30 sec",
        "suggested_days": ["D14", "D15", "D16", "D17", "D18", "D19", "D20"]
    },
    {
        "category": "Creativity",
        "activity": "Auditory Magic",
        "frequency": "2 sounds/day",
        "time": "60 sec",
        "suggested_days": ["D14", "D15", "D16", "D17", "D18", "D19", "D20"]
    },
    {
        "category": "Languages",
        "activity": "Talk, To Listen",
        "frequency": "1x/Day",
        "time": "60 sec",
        "suggested_days": ["D14", "D15", "D16", "D17", "D18", "D19", "D20"]
    },
    {
        "category": "Athleticism",
        "activity": "Finger Skills",
        "frequency": "3x/Week",
        "time": "60 sec",
        "suggested_days": ["D14", "D17", "D20"]
    },
    {
        "category": "Creativity",
        "activity": "Stimulus Explosion",
        "frequency": "2x/Week",
        "time": "60 sec",
        "suggested_days": ["D14", "D19"]
    },
    {
        "category": "Logic",
        "activity": "Foundations of Logic (Quantity)",
        "frequency": "2x/Week",
        "time": "60 sec",
        "suggested_days": ["D15", "D18"]
    }
]

@app.route('/api/plans', methods=['GET'])
def get_plans():
    return jsonify({
        "week": "14-21",
        "plans": plans
    })

if __name__ == '__main__':
    app.run(debug=True)
