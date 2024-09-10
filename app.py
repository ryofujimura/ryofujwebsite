from flask import Flask, render_template
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
        "id": "honda",
        "company": "American Honda Motor Company, Inc.",
        "title": "Work",
        "term": "June 2024 - August 2024",
        "image": "honda.svg",
        "role": "Software Engineer",
        "description": "Conducted comprehensive research on on-device generative AI, with a focus on its potential applications within the automotive industry to enhance vehicle functionalities. Developed and demonstrated applications on an NVIDIA Jetson Orin Nano 8GB using Linux and CUDA, showcasing on-device generative AI capabilities with Meta's Llama 3 model to enhance vehicle autonomy and local AI performance..",
    },
    {
        "id": "cusco",
        "company": "CUSCO USA Inc.",
        "title": "Work",
        "term": "October 2021 - May 2024",
        "image": "cusco.svg",
        "role": "Data Engineer",
        "description": "Led a team to develop a Python application, extracting data from 11,560 archived PDF files to improve access to historical data. Utilized advanced methodologies and testing to enhance software quality, resulting in a 30% revenue increase.",
    },
    {
        "id": "matchatime",
        "company": "Moyai LLC",
        "title": "Project",
        "term": "March 2024 - April 2024",
        "image": "matchatime.svg",
        "role": "Developer Project Management",
        "description": "Creating a desktop macOS app so remote individual contributors can easily align timezones without interrupting the flow of their work",
    },
    {
        "id": "Shohei Home Ground",
        "company": "Ryo Fujimura",
        "title": "Project",
        "term": "March 2023 - November 2023",
        "image": "shoheihomeground.svg",
        "role": "Founder",
        "description": "Leveraged leadership and development skills to create and deploy an automated Instagram upload program using Python and the Instagram API, achieving 685 posts and an 11,000 follower increase in 8 months. Successfully transformed the initiative into a profitable venture by enhancing engagement and expanding the audience, effectively monetizing the platform reach.",
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


if __name__ == '__main__':
    app.run(debug=True)
