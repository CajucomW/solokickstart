top = open('templates/top.html').read()
bottom = open('templates/bottom.html').read()

content = open('content/index.html').read()
index_html = top + content + bottom
open('index_full.html', 'w+').write(index_html)

content = open('content/tech.html').read()
tech_html = top + content + bottom
open('tech_full.html', 'w+').write(tech_html)

content = open('content/pta.html').read()
pta_html = top + content + bottom
open('pta_full.html', 'w+').write(pta_html)

content = open('content/jiujitsu.html').read()
jiujitsu_html = top + content + bottom
open('jiujitsu_full.html', 'w+').write(jiujitsu_html)
