from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "change_this_secret_key"

COURSES = [
    {"name": "Gen AI", "category": "AI / Machine Learning", "description": "Explore generative AI techniques and real-world applications."},
    {"name": "Snowflake with Cortex", "category": "Cloud / DevOps", "description": "Combine Snowflake analytics and Cortex automation for modern data workflows."},
    {"name": "Python", "category": "Data Engineering / Analytics", "description": "Master Python programming for data, automation, and analytics."},
    {"name": "Pyspark", "category": "Data Engineering / Analytics", "description": "Learn distributed data processing with PySpark and Spark SQL."},
    {"name": "Databricks", "category": "Data Engineering / Analytics", "description": "Build scalable analytics pipelines on the Databricks platform."},
    {"name": "ML", "category": "AI / Machine Learning", "description": "Gain practical machine learning skills with Python and real datasets."},
    {"name": "DL", "category": "AI / Machine Learning", "description": "Develop deep learning models for image, text, and data applications."},
    {"name": "AWS DevOps", "category": "Cloud / DevOps", "description": "Use AWS and DevOps practices to automate cloud infrastructure."},
    {"name": "Agentic AI", "category": "AI / Machine Learning", "description": "Build autonomous AI agents and intelligent automation workflows."},
    {"name": "Chat bots", "category": "AI / Machine Learning", "description": "Create conversational chat bot experiences for websites and apps."},
    {"name": "Chat Assistants", "category": "AI / Machine Learning", "description": "Design smart assistant systems that support users with context-aware responses."},
    {"name": "Prompt Engineering", "category": "AI / Machine Learning", "description": "Learn prompt design and optimization techniques for modern AI models."},
    {"name": "Datawarehouse", "category": "Data Engineering / Analytics", "description": "Understand data warehouse architecture and ETL best practices."},
]

USERS = {
    "student@example.com": "password123",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        if email in USERS and USERS[email] == password:
            session["user_email"] = email
            flash("Login successful. You can now enroll in courses.", "success")
            return redirect(url_for("trainings"))
        flash("Invalid email or password. Please try again.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user_email", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

@app.route("/trainings")
def trainings():
    categories = ["AI / Machine Learning", "Data Engineering / Analytics", "Cloud / DevOps"]
    grouped = {category: [course for course in COURSES if course["category"] == category] for category in categories}
    return render_template("trainings.html", grouped=grouped)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not email or not message:
            flash("Please fill in all fields before sending your inquiry.", "warning")
        else:
            flash("Thank you, your inquiry was sent successfully. We will contact you soon.", "success")
            return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/enroll", methods=["GET", "POST"])
def enroll():
    selected_course = request.args.get("course", "")
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        course = request.form.get("course", "").strip()
        if not name or not email or not phone or not course:
            flash("Please complete all enrollment fields.", "warning")
        else:
            flash(f"Thank you {name}! You are enrolled for {course}. Our team will reach out soon.", "success")
            return redirect(url_for("trainings"))
    return render_template("enroll.html", course=selected_course, courses=COURSES)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
