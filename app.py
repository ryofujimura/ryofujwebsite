from flask import Flask, render_template
import os

app = Flask(__name__)

# Define data
first_name = "RYO"
last_name = "FUJIMURA"
title = "SOFTWARE<br>ENGINEER"
description = "I am a data scientist with experience in data management, analysis, and visualization. I am passionate about using data to drive business decisions and solve complex problems."
featured_skills = ["swift", "database", "python"]


projects = [
    {
        "id": "honda",
        "company": "American Honda Motor Company, Inc.",
        "title": "Work",
        "term": "June 2024 - August 2024",
        "image": "honda.svg",
        "role": "Data Management<br>and Analysis",
        "description": "Assist in managing and analyzing large automotive data sets. Collaborating with team members to troubleshoot data issues. Perform data analysis to create reports that aid business decisions, and conduct research to gather information that bolsters data-driven strategies.",
    },
    {
        "id": "cusco",
        "company": "CUSCO USA Inc.",
        "title": "Work",
        "term": "October 2021 - Present",
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
        "role": "Developer<br>Project Management",
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
        "icon": "M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-4.466 19.59c-.405.078-.534-.171-.534-.384v-2.195c0-.747-.262-1.233-.55-1.481 1.782-.198 3.654-.875 3.654-3.947 0-.874-.312-1.588-.823-2.147.082-.202.356-1.016-.079-2.117 0 0-.671-.215-2.198.82-.64-.18-1.324-.267-2.004-.271-.68.003-1.364.091-2.003.269-1.528-1.035-2.2-.82-2.2-.82-.434 1.102-.16 1.915-.077 2.118-.512.56-.824 1.273-.824 2.147 0 3.064 1.867 3.751 3.645 3.954-.229.2-.436.552-.508 1.07-.457.204-1.614.557-2.328-.666 0 0-.423-.768-1.227-.825 0 0-.78-.01-.055.487 0 0 .525.246.889 1.17 0 0 .463 1.428 2.688.944v1.489c0 .211-.129.459-.528.385-3.18-1.057-5.472-4.056-5.472-7.59 0-4.419 3.582-8 8-8s8 3.581 8 8c0 3.533-2.289 6.531-5.466 7.59z",
    },
    {
        "title": "LinkedIn",
        "url": "https://www.linkedin.com/in/ryofujimura/",
        "icon": "M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z",
    },
    {
        "title": "Resume",
        "url": "https://drive.google.com/file/d/1TdtNaYYYiZngj8SL2CL7R8NwLqFlHUCD/view?usp=sharing",
        "icon": "M22 0h-20v24h14l6-6v-18zm-7 23h-12v-22h18v16h-6v6zm1-5h4.586l-4.586 4.586v-4.586zm-3 1h-8v1h8v-1zm0-3h-8v1h8v-1zm6-2v-1h-14v1h14zm0-4h-4v1h4v-1zm-6.006 1h-7.991l-.003-.789c-.003-.72-.006-1.615 1.314-1.92 1.483-.341 1.236-.418 1.158-.563-1.078-1.988-.71-3.173-.395-3.703.388-.651 1.089-1.025 1.923-1.025.827 0 1.523.368 1.91 1.011.545.904.409 2.222-.379 3.713-.105.196-.195.255 1.119.559 1.355.312 1.352 1.212 1.35 1.936l-.006.781zm-6.994-1h6c-.007-.547-.07-.626-.54-.734-.855-.198-1.629-.376-1.901-.972-.142-.311-.113-.66.087-1.039.61-1.151.758-2.146.407-2.729-.276-.458-.778-.526-1.053-.526-.48 0-.857.19-1.063.537-.352.59-.201 1.58.414 2.714.204.377.236.727.095 1.039-.269.598-1.036.774-1.847.962-.525.121-.593.202-.599.748zm13-2v-1h-4v1h4zm0-4h-4v1h4v-1z",
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
        description=description,
        projects=projects,
        links=links,
    )


if __name__ == "__main__":
    app.run(debug=True)
