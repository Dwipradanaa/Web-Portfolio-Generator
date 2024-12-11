from jinja2 import Environment, FileSystemLoader
import os

# Template loading
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index_template.html')

# Data untuk portfolio (bisa dikembangkan lebih lanjut)
portfolio_data = {
    "name": "John Doe",
    "profession": "Software Developer",
    "about": "A passionate software developer with experience in building web applications.",
    "skills": ["Python", "JavaScript", "HTML/CSS", "Django", "React"],
    "projects": [
        {"name": "Portfolio Website", "description": "A personal portfolio website created using Python and Bootstrap."},
        {"name": "Task Manager App", "description": "A web app to manage daily tasks built with Django."}
    ],
    "email": "johndoe@example.com"
}

# Render template dengan data
output_html = template.render(portfolio_data)

# Simpan ke file output
os.makedirs('output', exist_ok=True)
with open('output/index.html', 'w') as f:
    f.write(output_html)

print("Portfolio generated successfully!")
