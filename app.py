from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# API endpoint (matches your JS EXACTLY)
@app.route("/api/generate-curriculum", methods=["POST"])
def generate_curriculum():
    try:
        data = request.json

        skill = data.get("skill")
        level = data.get("level")
        semesters = int(data.get("semesters"))
        weekly_hours = data.get("weekly_hours")
        industry_focus = data.get("industry_focus")

        curriculum = {
            "program_title": f"{level} in {skill}",
            "summary": f"{semesters}-semester program focused on {skill} with industry focus on {industry_focus}. Weekly hours: {weekly_hours}.",
            "semesters": []
        }

        for i in range(1, semesters + 1):
            semester = {
                "semester": i,
                "courses": [
                    {
                        "course_name": f"{skill} Fundamentals {i}",
                        "credits": 4,
                        "topics": [
                            f"Core concepts of {skill}",
                            f"{skill} applications",
                            f"Industry use-cases in {industry_focus}",
                            "Hands-on labs"
                        ]
                    },
                    {
                        "course_name": f"Advanced {skill} {i}",
                        "credits": 3,
                        "topics": [
                            f"Advanced {skill} techniques",
                            "Mini projects",
                            "Case studies",
                            "Practical assessments"
                        ]
                    }
                ]
            }

            curriculum["semesters"].append(semester)

        return jsonify(curriculum)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
