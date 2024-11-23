import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Home page route
@app.route("/", methods=["GET", "POST"])
def index():
    regex = ""
    test_string = ""
    matches = []
    highlighted = ""
    
    if request.method == "POST":
        regex = request.form["regex"]
        test_string = request.form["test_string"]

        try:
            # Perform regex matching
            pattern = re.compile(regex)
            matches = pattern.findall(test_string)
            
            # Highlight the matched substrings in the test string
            highlighted = highlight_matches(test_string, matches)
        except re.error:
            matches = []
            highlighted = "<p style='color: red;'>Invalid regex pattern.</p>"

    return render_template("index.html", regex=regex, test_string=test_string, matches=matches, highlighted=highlighted)


# New route for email validation
@app.route("/validate_email", methods=["GET", "POST"])
def validate_email():
    email = ""
    is_valid = None
    if request.method == "POST":
        email = request.form["email"]
        # Email validation regex pattern
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        is_valid = bool(re.match(email_pattern, email))  # Return True/False

    return render_template("validate_email.html", email=email, is_valid=is_valid)


# Function to highlight the matched strings in the test string
def highlight_matches(test_string, matches):
    highlighted = test_string
    for match in matches:
        highlighted = highlighted.replace(match, f"<span class='highlight'>{match}</span>")
    return highlighted


if __name__ == "__main__":
    app.run(debug=True)
