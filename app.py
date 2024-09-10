from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define data
first_name = "RYO"
last_name = "FUJIMURA"
title = "SOFTWARE<br>ENGINEER"
welcomemessage = "welcome to my portfolio"
description = "I am a data scientist with experience in data management, analysis, and visualization. I am passionate about using data to drive business decisions and solve complex problems."
featured_skills = ["swift", "database", "python"]


projects = [
    {
        "id": "1",
        "company": "American Honda Motor Company, Inc.",
        "title": "Work",
        "term": "June 2024 - August 2024",
        "image": "honda.svg",
        "role": "Software Engineer - Intern",
        "description": "Conducted comprehensive research on on-device generative AI, focusing on its potential applications within the automotive industry to enhance vehicle functionalities. Developed and demonstrated applications on an NVIDIA Jetson Orin Nano 8GB using Linux and CUDA, showcasing on-device generative AI capabilities with Meta's Llama 3 model to enhance vehicle autonomy and local AI performance.",
    },
    {
        "id": "2",
        "company": "CUSCO USA Inc.",
        "title": "Work",
        "term": "October 2021 - May 2024",
        "image": "cusco.svg",
        "role": "Data Engineer - Freelance",
        "description": "Led a three-member team in developing a Python application that extracted data from 11,560 archived PDF files, utilizing advanced software development methodologies. Demonstrated proficiency in testing and development, including the creation of comprehensive test cases to ensure software quality and functionality. Enhanced user access to historical data dating back to 1977, resulting in a 30% increase in revenue by enabling precise retrieval of previously inaccessible information for new users.",
    },
    {
        "id": "3",
        "company": "CUSCO USA Inc.",
        "title": "Work",
        "term": "October 2021 - May 2024",
        "image": "cusco.svg",
        "role": "Full Stack Web Developer - Freelance",
        "description": "Collaborated with a team of 2 to develop a modern website utilizing Svelte with Svelte Kit, focusing on UI and information accessibility, resulting in a 50% reduction in exit rate. Implemented data management systems including Google Drive, Cloudinary, and Sanity for efficient content organization and delivery, leading to a 250% increase in revenue over the past three years.",
    },
    {
        "id": "4",
        "company": "FUJITSUBO GIKEN KOGYO CO., LTD",
        "title": "Work",
        "term": "September 2023 - November 2023",
        "image": "fujitsubo.svg",
        "role": "Data Engineer - Freelance",
        "description": "Engineered a Python-based software program employing web scraping techniques to meticulously extract crucial data from diverse websites. Automated generation workflows with Adobe InDesign, significantly boosting efficiency and achieving a 100% error-free rate by eliminating manual effort across various cases, ensuring software quality and functionality.",
    },
    {
        "id": "5",
        "company": "Matcha Time",
        "title": "Project",
        "term": "March 2024 - April 2024",
        "image": "matchatime.svg",
        "role": "Co-Project Manager and Developer",
        "description": "Developed and created application functions with Swift/SwiftUI, implemented multi-city synchronization, designed and tested features, fixed bugs, and deployed solutions. Planned and completed the project in 4 weeks, launched the application on the Mac App Store, and managed cross-functional team collaboration to ensure seamless integration and project success.",
    },
    {
        "id": "6",
        "company": "Poker Percentage",
        "title": "Project",
        "term": "January 2022 - April 2024",
        "image": "poker.png",
        "role": "Developer",
        "description": "Developed a poker percentage calculator application for watchOS using Swift and WatchKit, facilitating real-time calculation of odds and probabilities. Improved user decision-making by providing accurate insights into poker hands, resulting in a 15% increase in win rates among users.",
    },
    {
        "id": "7",
        "company": "Schedule Mastermind",
        "title": "Project",
        "term": "December 2023 - February 2024",
        "image": "schedule.jpg",
        "role": "Developer",
        "description": "Engineered a Python-based application with the Flask framework, streamlining scheduling operations for over 500 classes. Created a user-friendly interface for course selection, timetable generation, and conflict resolution, achieving a 100% reduction in scheduling errors and boosting overall productivity by 25% through automation.",
    },
    {
        "id": "8",
        "company": "Shohei Home Ground",
        "title": "Project",
        "term": "March 2023 - November 2023",
        "image": "shoheihomeground.svg",
        "role": "Developer and Project Leader",
        "description": "Engineered and deployed a streamlined content scheduling and posting process using Python and the Instagram API, achieving 685 posts and increasing followers by 11,000 in 8 months. Transformed the project from a non-revenue-generating initiative to a profitable venture by enhancing engagement and expanding the audience.",
    },
    {
        "id": "9",
        "company": "Amazon Web Services",
        "title": "Leadership",
        "term": "September 2023 - November 2023",
        "image": "aws.png",
        "role": "Trainer",
        "description": "Provided training sessions to professionals on Amazon Web Services, imparting knowledge on cloud infrastructure and services.",
    },
    # more projects...
]


links = [
    {
        "title": "Github",
        "url": "https://github.com/ryofujimura",
        "icon": "github.png",
    },
    {
        "title": "LinkedIn",
        "url": "https://www.linkedin.com/in/ryofujimura/",
        "icon": "linkedin.png",
    },
    {
        "title": "Resume",
        "url": "https://docs.google.com/document/d/1J32LsLRUETEwXttxBxeZHVihFNcm10fRAfiumhfVTTU/edit?usp=sharing",
        "icon": "resume.png",
    },
]


# Get available images with their extensions
img_asset_path = os.path.join(app.static_folder, "img-asset")
# for each file in the img_asset_path, add "img-asset/" in front



# print(available_images)
# Define routes
@app.route("/")
def index():
    return render_template(
        "index.html",
        first_name=first_name,
        last_name=last_name,
        title=title,
        welcomemessage=welcomemessage,
        description=description,
        projects=projects,
        links=links,
    )

@app.route('/experience')
def experience():
    project_id = request.args.get('project_id')
    # Find the project by ID
    selected_project = next((p for p in projects if str(p['id']) == project_id), None)
    return render_template('experience.html', project=selected_project)



if __name__ == '__main__':
    app.run(debug=True)
