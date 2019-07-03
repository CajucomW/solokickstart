# Challenge 3 of Jinja Control Flow looks to have the answer to nav links being selected when on that page.
# -------Phase 1--------
import glob
import os


all_html_files = glob.glob("content/*.html")
output = glob.glob('docs/*.html')
template = open('templates/base.html').read()

pages = []

for html_path in all_html_files:
    file_name = os.path.basename(html_path)
    name_only, extension = os.path.splitext(file_name)

    pages.append({
    "filename": html_path, 
    "title": name_only,
    "output": "docs/" + file_name,
})

for page in pages:
    
    html_file = open(page['filename']).read()
    combined = template.replace('{{content}}', html_file)
    combined = combined.replace('{{title}}', page['title'])
    open(page['output'], 'w+').write(combined)
#
# 
#  -------Phase 2--------
from jinja2 import Template
#index_html = open("content/index.html").read()
#template_html = open("templates/base.html").read()
#template = Template(template_html)
#print(template)
#result = template.render(
#    title="Homepage",
#    content=index_html,
#    )
#print(result)























