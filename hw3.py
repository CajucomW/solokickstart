#def main():

#    top = open('templates/top.html').read()
#    bottom = open('templates/bottom.html').read()

#    content = open('content/index.html').read()
#    index_html = top + content + bottom
#    open('docs/index.html', 'w+').write(index_html)

#    content = open('content/tech.html').read()
#    tech_html = top + content + bottom
#    open('docs/tech.html', 'w+').write(tech_html)

#    content = open('content/pta.html').read()
#    pta_html = top + content + bottom
#    open('docs/pta.html', 'w+').write(pta_html)

#    content = open('content/jiujitsu.html').read()
#    jiujitsu_html = top + content + bottom
#    open('docs/jiujitsu.html', 'w+').write(jiujitsu_html)

#if __name__ == "__main__":
#    main()
    
pages = [   #TURN THIS INTO SOMETHING THAT PUTS OUT FULL HTML FILES
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
    {
        'filename': 'content/index.html',
        'output': 'docs/index.html',
        'title': 'About Me',
    },
    
]
template = open('templates/base.html').read()

for html in pages:
    filename = open(html['filename']).read()
    combined_page = template.replace('{{content}}', filename)
    open('docs/index.html', 'w+').write(combined_page)



# So far this works.
#topfile = pages[0]
#indexfile = pages[1]
#bottomfile = pages[2]
#topcontent = open(topfile['filename']).read()
#indexcontent = open(indexfile['filename']).read()
#bottomcontent = open(bottomfile['filename']).read()
#finalcontent = topcontent + indexcontent + bottomcontent
#open('docs/index.html', 'w+').write(finalcontent)
#{
#        'filename': 'templates/top.html',
#        'output': 'docs/index.html',
#        'title': 'Top Document',
#    },
#{
#        'filename': 'templates/bottom.html',
#        'output': 'docs/index.html',
#        'title': 'Bottom Document',
#    },
    

# This code only writes the last entry in the list
#    contents = open(html['filename']).read()
#    open('test.html', 'w+').write(contents)
    

#    print('----')
#    print(html['filename'])
#    print(html['output'])
#    print('----')


# THIS ONE WORKS
#template = open('templates/base.html').read()
#index_content = open('content/index.html').read()
#finished_index_page = template.replace('{{content}}', index_content)
#open('docs/index.html', 'w+').write(finished_index_page)















