import os
import glob
from jinja2 import Template


all_html_files = glob.glob("content/*.html")
output = glob.glob('docs/*.html')

pages = []

for html_path in all_html_files:                            # html_path is content/*.html
    file_name = os.path.basename(html_path)                 # file_name is *.html
    name_only, extension = os.path.splitext(file_name)      # name_only is *
    html_content = open(html_path).read()
    doc_dir = "docs/" + file_name

    pages.append({
        "title": name_only,
        "output": doc_dir,
        "filename": file_name,
        "content": html_content,
    })

template_html = open('templates/base.html').read()

for page in pages:
    title = page['title']
    output = page['output']
    filename = page['filename']                             # filename is content/*html from list
    content = page['content']
    template = Template(template_html)
    result = template.render(
        title=title, 
        output=output,
        filename=filename,
        content=content,
        pages=pages,       #### <<< links break when this line isn't inlcuded. Not sure why. ####
        )
    open(page['output'], 'w+').write(result)
