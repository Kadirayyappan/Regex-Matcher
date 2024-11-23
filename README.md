# Regex Matcher and Email Validation Web App

## Project Objective

The objective of this project is to create a web application that allows users to input a test string and a regular expression (regex) to find matches. It also includes a feature to validate email addresses using regex. The application provides real-time feedback, displaying the matches found in the test string and validating email format as per a predefined regex pattern.

---

## Features

1. **Regex Matcher**: 
   - Input a regular expression and a test string.
   - The app will display all the matches found within the test string based on the regex pattern.

2. **Email Validation**:
   - Input an email address.
   - The app will validate if the email address matches a standard email format using regex.

---

## Technologies Used

- **Flask**: Python web framework for backend development.
- **HTML/CSS**: For frontend user interface.
- **Python re module**: For regex matching and email validation.

---

## Steps to Run the Application Locally

### 1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/regex-matcher-email-validation.git
   cd regex-matcher-email-validation
```


### 2. Set up a virtual environment:
   - **Windows**:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

### 3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
```

### 4. Run the application:
```
python app.py
```
Your application will be available at http://localhost:5000/.
### File Structure
```
regex-matcher-email-validation/
│
├── app.py                  # Main Flask app file
├── templates/              # Folder containing HTML templates
│   ├── index.html          # Home page template for Regex Matcher
│   ├── email_validation.html # Template for Email Validation page
├── static/                 # Folder containing static files like CSS
│   └── styles.css          # Stylesheet for the web app
├── requirements.txt        # List of Python dependencies
└── README.md               # This README file
```

## Contact Me

If you have any questions or need assistance, feel free to reach out to me:

- **Email**: [kadirayyappan@gmail.com](mailto:kadirayyappan@gmail.com)
- **LinkedIn**: [A. Kadir](https://www.linkedin.com/in/kadir-ayyappan2005)
- **GitHub**: [Kadirayyappan](https://github.com/Kadirayyappan)

---

⭐️ Show Your Support
If you like this project, please consider giving it a ⭐️! It helps me a lot and motivates me to continue building cool projects.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
