# Challenge 3 of Jinja Control Flow looks to have the answer to nav links being
# selected when on that page.

# -------Phase 1--------
# Instead of using a fixed list, grab files from the content/ directory to
# build the site 

import glob
import os

all_html_files = glob.glob("content/*.html")
output = glob.glob('docs/*.html')

print(all_html_files)

for html_path in all_html_files:
    print(html_path)
    file_name = os.path.basename(html_path)
    print(file_name)

#    name_only, extension = os.path.splitext(file_name)
#    print(name_only)
#    print(extension)

    pages = []

    pages.append({
        "filename": html_path, 
#        "title": "Index",
        "output": "docs/" + file_name,
        })
    print(pages)

template = open('templates/base.html').read()

def build():
    for page in pages:
        html_file = open(page['filename']).read()
        combined = template.replace('{{content}}', html_file)
        open(page['output'], 'w+').write(combined)

build()
      
# if __name__ == "__main__":
#     main()   











