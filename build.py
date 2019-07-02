# Challenge 3 of Jinja Control Flow looks to have the answer to nav links being selected when on that page.
# -------Phase 1--------
# Instead of using a fixed list, grab files from the content/ directory tobuild the site 

import glob
import os

all_html_files = glob.glob("content/*.html")
output = glob.glob('docs/*.html')
template = open('templates/base.html').read()

for html_path in all_html_files:
    file_name = os.path.basename(html_path)
    name_only, extension = os.path.splitext(file_name)

pages = []
for page in pages:
    
    pages.append({
        "filename": html_path, 
        "title": name_only,
        "output": "docs/" + file_name,
    })

    html_file = open(page['filename']).read()
    combined = template.replace('{{content}}', html_file)
    open(page['output'], 'w+').write(combined)


# if __name__ == "__main__":
#   main()   











