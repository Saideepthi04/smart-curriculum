from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------------------
# PAGES
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generator")
def generator():
    return render_template("generator.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------------------
# API (UPDATED: includes internships + certifications)
# ---------------------------
@app.route("/api/generate-curriculum", methods=["POST"])
def generate_curriculum():
    try:
        data = request.json

        skill = (data.get("skill") or "").strip()
        level = (data.get("level") or "").strip()
        semesters = int(data.get("semesters"))
        weekly_hours = (data.get("weekly_hours") or "").strip()
        industry_focus = (data.get("industry_focus") or "").strip()

        skill_lower = skill.lower()

        internships = []
        certifications = []

        # ---------- Skill based suggestions ----------
        if "machine learning" in skill_lower or skill_lower == "ml":
            internships = [
                "Machine Learning Intern",
                "Data Science Intern",
                "AI Research Intern",
                "Computer Vision Intern",
                "NLP Intern"
            ]
            certifications = [
                "DeepLearning.AI Machine Learning Specialization (Coursera)",
                "Google Advanced Data Analytics (Coursera)",
                "IBM Machine Learning Professional Certificate (Coursera)",
                "Microsoft Azure AI Fundamentals (AI-900)",
                "Kaggle Micro-Courses: Machine Learning"
            ]

        elif "data science" in skill_lower or "datascience" in skill_lower:
            internships = [
                "Data Science Intern",
                "Business Analyst Intern",
                "Data Analyst Intern",
                "BI Intern",
                "Product Analyst Intern"
            ]
            certifications = [
                "Google Data Analytics Professional Certificate (Coursera)",
                "IBM Data Science Professional Certificate (Coursera)",
                "Microsoft Power BI Data Analyst (PL-300)",
                "Kaggle Micro-Courses: Pandas + Data Visualization",
                "SQL for Data Science (Coursera)"
            ]

        elif "web" in skill_lower or "frontend" in skill_lower or "full stack" in skill_lower:
            internships = [
                "Frontend Developer Intern",
                "Full Stack Developer Intern",
                "Web Developer Intern",
                "UI Developer Intern",
                "React Developer Intern"
            ]
            certifications = [
                "Meta Front-End Developer Professional Certificate (Coursera)",
                "Meta Back-End Developer Professional Certificate (Coursera)",
                "freeCodeCamp Responsive Web Design",
                "The Odin Project (Full Stack Path)",
                "Google UX Design Professional Certificate (Coursera)"
            ]

        elif "android" in skill_lower or "mobile" in skill_lower:
            internships = [
                "Android Developer Intern",
                "Mobile App Developer Intern",
                "Flutter Developer Intern",
                "React Native Intern"
            ]
            certifications = [
                "Google Associate Android Developer (learning path)",
                "Meta Android Developer Professional Certificate",
                "Flutter & Dart - The Complete Guide (Udemy)",
                "Kotlin for Android (Coursera)"
            ]

        elif "cloud" in skill_lower or "aws" in skill_lower or "azure" in skill_lower:
            internships = [
                "Cloud Intern",
                "DevOps Intern",
                "Site Reliability Intern",
                "Cloud Support Intern"
            ]
            certifications = [
                "AWS Cloud Practitioner (CLF-C02)",
                "Microsoft Azure Fundamentals (AZ-900)",
                "Google Cloud Digital Leader",
                "Docker + Kubernetes (Udemy/Coursera)"
            ]

        elif "cyber" in skill_lower or "security" in skill_lower:
            internships = [
                "Cybersecurity Intern",
                "SOC Analyst Intern",
                "Security Analyst Intern",
                "Network Security Intern",
                "Penetration Testing Intern"
            ]
            certifications = [
                "Google Cybersecurity Professional Certificate (Coursera)",
                "CompTIA Security+ (Recommended)",
                "CEH (Certified Ethical Hacker)",
                "Cisco CCNA (Networking)"
            ]

        elif "java" in skill_lower:
            internships = [
                "Java Developer Intern",
                "Backend Developer Intern",
                "Software Engineer Intern",
                "Spring Boot Intern"
            ]
            certifications = [
                "Oracle Java SE Certification (OCA/OCP)",
                "Spring Boot + Microservices (Udemy)",
                "DSA in Java (Coding Ninjas / Coursera)"
            ]

        elif "python" in skill_lower:
            internships = [
                "Python Developer Intern",
                "Backend Intern",
                "Automation Intern",
                "Data Analyst Intern"
            ]
            certifications = [
                "Python for Everybody (Coursera)",
                "Google IT Automation with Python (Coursera)",
                "HackerRank Python Certification",
                "Kaggle Python Micro-Course"
            ]

        elif "ui" in skill_lower or "ux" in skill_lower or "design" in skill_lower:
            internships = [
                "UI/UX Intern",
                "Product Design Intern",
                "UX Research Intern",
                "Graphic Design Intern"
            ]
            certifications = [
                "Google UX Design Professional Certificate (Coursera)",
                "Figma UI UX Design Essentials (Udemy)",
                "Interaction Design Foundation (IDF) Courses"
            ]

        else:
            internships = [
                f"{skill} Intern",
                "Software Engineering Intern",
                "Technical Intern",
                "Research Intern"
            ]
            certifications = [
                f"Coursera specialization in {skill}",
                f"Udemy course in {skill}",
                f"edX certification in {skill}"
            ]

        # ---------- Curriculum generation ----------
        curriculum = {
            "program_title": f"{level} in {skill}",
            "summary": f"{semesters}-semester program focused on {skill} with industry focus on {industry_focus}. Weekly hours: {weekly_hours}.",
            "internships": internships,
            "certifications": certifications,
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