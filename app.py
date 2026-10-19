
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-key-change-before-deployment")

SERVICES = [
    ("01", "Residential Construction",
     "Build a comfortable home planned around your needs."),
    ("02", "Commercial Buildings",
     "Practical spaces for offices, shops, and businesses."),
    ("03", "Interior Design",
     "Beautiful and functional interiors for everyday living."),
    ("04", "Exterior Design",
     "Modern facades and attractive outdoor spaces."),
    ("05", "Renovation",
     "Improve existing spaces with thoughtful upgrades."),
    ("06", "Consultation",
     "Discuss your plans, materials, budget, and next steps.")
]

PROJECTS = [
    {
        "title": "Modern Family Home",
        "type": "Residential",
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1000&q=80"
    },
    {
        "title": "Elegant Living Space",
        "type": "Interior Design",
        "image": "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?auto=format&fit=crop&w=1000&q=80"
    },
    {
        "title": "Contemporary Office",
        "type": "Commercial",
        "image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1000&q=80"
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        services=SERVICES,
        projects=PROJECTS
    )


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please complete all required fields.", "error")
        return redirect(url_for("home") + "#contact")

    # Demo only: prints the enquiry in the server terminal.
    # Connect email or a database to receive enquiries in production.
    print("NEW ENQUIRY")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    flash(
        "Thank you! Your demo enquiry was accepted. "
        "Email delivery is not configured yet.",
        "success"
    )
    return redirect(url_for("home") + "#contact")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
