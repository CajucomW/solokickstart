top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

content = open('content/index.html').read()
index_html = top + content + bottom
open('docs/index.html', 'w+').write(index_html)

content = open('content/tech.html').read()
tech_html = top + content + bottom
open('docs/tech.html', 'w+').write(tech_html)

content = open('content/pta.html').read()
pta_html = top + content + bottom
open('docs/pta.html', 'w+').write(pta_html)

content = open('content/jiujitsu.html').read()
jiujitsu_html = top + content + bottom
open('docs/jiujitsu.html', 'w+').write(jiujitsu_html)
