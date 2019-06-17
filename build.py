top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

content = open('index.html').read()
index_html = top + content + bottom
open('index_full.html', 'w+').write(index_html)
