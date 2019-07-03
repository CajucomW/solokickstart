# # Challenge 3 of Jinja Control Flow looks to have the answer to nav links being selected when on that page.
# # -------Phase 1--------
import glob
import os

all_html_files = glob.glob("content/*.html")
output = glob.glob('docs/*.html')
template_html = open('templates/base.html').read()

# pages = []

# for html_path in all_html_files:
#     file_name = os.path.basename(html_path)
#     print(file_name)
#     name_only, extension = os.path.splitext(file_name)

#     pages.append({
#     "filename": html_path, 
#     "title": name_only,
#     "output": "docs/" + file_name,
# })

# for page in pages:
    
#     html_file = open(page['filename']).read()
#     combined = template.replace('{{content}}', html_file)
#     combined = combined.replace('{{title}}', page['title'])
#     open(page['output'], 'w+').write(combined)
# #
# # 
# #  -------Phase 2--------
from jinja2 import Template

output = glob.glob('docs/*.html')

for html_path in all_html_files:
    file_name = os.path.basename(html_path)
    name_only, extension = os.path.splitext(file_name)
    html_content = open(html_path).read()
    template = Template(template_html)
    result = template.render(
        title=name_only,
        content=html_content,
        )
    open("docs/" + file_name, 'w+').write(result)

# tech_html = open("content/tech.html").read()
# template = Template(template_html)

# result = template.render(
#     title="Tech",
#     content=tech_html,
#     )
# open('docs/tech.html', 'w+').write(result)

# pta_html = open("content/pta.html").read()
# template = Template(template_html)

# result = template.render(
#     title="PTA",
#     content=pta_html,
#     )
# open('docs/pta.html', 'w+').write(result)

# jiujitsu_html = open("content/jiujitsu.html").read()
# template = Template(template_html)

# result = template.render(
#     title="Jiujitsu",
#     content=jiujitsu_html,
#     )
# open('docs/jiujitsu.html', 'w+').write(result)
