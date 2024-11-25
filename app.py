from flask import Flask, render_template
import webbrowser

# Flask app
app = Flask(__name__)

# Resume data
resume_data = {
    "Name": "Pooja Lakkundi",
    "Contact": {
        "Email": "lakkundi.pooja15@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/pooja150201",
        "GitHub": "https://github.com/pooja-lakkundi"
    },
    "Skills": "Go | Python | Java | Shell Scripting | Git | GitHub | OOP | Cloud Computing | AWS | RDBMS | Blockchain | Firebase | Android Studio | Navigation",
    "Experience": {
        "Tata Consultancy Services      ----------------------------------------------------------------------------------------------------------------------------------------------------        New Delhi, India 08/2022 – 11/2024. \n"
        "Analyst-GIS": (
            "- Participated in training program designed to enhance technical skills, domain knowledge, and soft skills.\n"
            "- Compiled, managed and analyzed geographic data from various sources including satellite imagery, Drives, and surveys using GIS software tool.\n"
            "- Maintained GIS Databases.\n"
            "- Provided technical support training to the staff on GIS software, tools and methodologies.\n"
            "- Collaborated with other departments to integrate data with existing systems and applications.\n"
            "- Conducted quality assurance checks on the data to ensure accuracy, completeness, and consistency.\n"
            "- Assisted in preparing documentation, presentations and reports for the client meetings or project reviews.\n"
            "- Assisted project teams in executing tasks and deliverables according to the project plans and timelines."
        ),
        "Graduate Trainee": (
            "- Participated in training program designed to enhance technical skills, domain knowledge, and soft skills.\n"
            "- Completed assigned coursework and certifications in relevant technologies such as blockchain, DBMS, Python etc.\n"
            "- Engaged in on-the-job training and mentorship to understand TCS's methodologies, tools and practices."
        )
    },
    "Education": "BCA(Bachelor's in Computer Applications) at KLE Society's college of BCA, RLSI Belagavi.    ----------------------------------------------------------------   Karnataka, India | 2019 - 2022\n",
    "Projects": {
        "AWS Resource Tracker": (
            "- This project is a simple Bash script that tracks usage of various AWS resources such as S3 Buckets, EC2 Instances, Lambda Functions, and IAM Users and logs these details into a file at regular intervals using cron jobs. (10/2024)"
        ),
        "DigiArt": (
            "- Led a 7-member team for developing a decentralized web-based blockchain application that converts an image into an NFT that are built using react in frontend and Flask as backend. (11/2023)"
        ),
        "Abhogi": (
            "- This aim of this restaurant management application is to replace the traditional way of taking orders with computerized system and to prepare order summary reports quickly. Main goal of this application is to computerizing the work in a restaurant. (06/2022)"
        )
    }
}

# Home route
@app.route("/")
def home():
    return render_template("resume.html", resume=resume_data)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
