from flask import Flask, render_template
import os
import re

app = Flask(__name__)

# Function to convert tab name to URL-friendly slug
def slugify(name):
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', name.strip().lower()))

# Tab display name -> template filename
tabs = {
    "Title Page": "c1.html",
    "Project Index: Climate Change Modeling": "c2.html",
    "Climate Modelling Flowchart": "c3.html",
    "Climate Modelling Report": "c4.html",
    "Flowchart Introduction": "c5.html",
    "Fundamentals of Climate Science": "c6.html",
    "Flowchart-Fundamentals of Climate Science": "c7.html",
    "Overview of Mathematical Modelling in Climate Science": "c8.html",
    "Climate Modelling Flowchart": "c9.html",
    "Systems Theory and Climate Dynamics": "c10.html",
    "Flowchart-Systems Theory and Climate Dynamics ": "c11.html",
    " Mathematical Formulation of Climate Models": "c12.html",
    "Climate Models Flowchart":"c13.html",
    "Model Calibration and Validation ": "c14.html",
    "Flowchart-Model Calibration and Validation ": "c15.html",
    "Simulation and Analysis ": "c16.html",
    "Flowchart-Simulation and Analysis":"c17.html",
    "Applications and Policy Implications ": "c18.html",
    "Flowchart-Applications and Policy Implications ": "c19.html",
    "Challenges and Limitations": "c20.html",
    "Flowchart-Challenges and Limitations": "c21.html",
    "Future Directions in Climate Modelling": "c22.html",
    "Flowchart-Future Directions in Climate Modelling": "c23.html",
    "Bibliography": "c24.html",
    "Energy Balance Models(EBMs)": "c25.html",
    "Radioactive convective Models (RCMs)": "c26.html",
    "General Circulation Models(GCMs)": "c27.html",
    " Differential Equation in Climate Modelling":"c28.html",
    " Flowchart-Differential Equation in Climate Modelling":"c29.html",
    "Heat and Mass Transfer Equation": "c30.html",
    "Carbon Cycle Modelling":"c31.html",
    "Ocean-Atmosphere Interaction Models":"c32.html",
    "Coupled Subsystems and Integrated Models":"c33.html",
    "Machine-Learning Model Overview":"c34.html",
    "Mathematical Formulation -Hybrid System + ML Climate Model":"c35.html",
    "ML Surrogate for Climate-Change Dynamics":"c36.html",
    "Climate Change Dynamics Simulator":"c37.html"
}

# Slug -> HTML file name
slug_to_file = {slugify(name): filename for name, filename in tabs.items()}

# Slug -> Original tab name (used for display)
slug_to_title = {slugify(name): name for name in tabs.keys()}

@app.route('/')
def index():
    return render_template('index3.html', tabs=slug_to_title)

@app.route('/load/<slug>')
def show_page(slug):
    filename = slug_to_file.get(slug)
    if filename:
        return render_template(filename)
    return "<h2 style='color:red;'>❌ Page not found.</h2>", 404

if __name__ == '__main__':
    app.run(debug=True)
