def originally_main_func():
#---------------------------Phase 1--------------------------------
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

#originally_main_func()

#---------------------------Phase 2--------------------------------

pages = [   
    
    {
    'filename': 'content/index.html',
    'output': 'docs/index.html',
    'title': 'About Me',
    },
    {
    'filename': 'content/tech.html',
    'output': 'docs/tech.html',
    'title': 'Tech',
    },
    {
    'filename': 'content/pta.html',
    'output': 'docs/pta.html',
    'title': 'PTA/Healthcare',
    },
    {
    'filename': 'content/jiujitsu.html',
    'output': 'docs/jiujitsu.html',
    'title': 'JiuJitsu',   
    },   
]

#base.html contains 'top' and 'bottom' of html pages
template = open('templates/base.html').read()

def main():

#---------------------------Phase 4--------------------------------
    def readwrite():
        html_file = open(content['filename']).read()
#---------------------------Phase 3--------------------------------
        combined = template.replace('{{content}}', html_file)
        open(content['output'], 'w+').write(combined)

        # I can't get this to work.
        for content in pages:
            new_title = template.replace('{{title}}', content['title'])
            open(content['output'], 'w+').write(new_title)
        
            readwrite()

if __name__ == "__main__":
    main()   














