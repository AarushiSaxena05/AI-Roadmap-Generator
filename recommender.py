import json

with open("roadmap_data.json") as f:
    data = json.load(f)

def generate_roadmap(goal, skills):

    goal = goal.lower().replace(" ", "_")

    if goal not in data:
        return {"error": "Goal not found"}

    required_skills = data[goal]["skills"]
    resources = data[goal]["resources"]

    skills = [s.strip().lower() for s in skills]

    missing_skills = []

    for skill in required_skills:
        if skill.lower() not in skills:
            missing_skills.append(skill)

    return {
        "missing_skills": missing_skills,
        "resources": resources
    }