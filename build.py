#def main():

#    top = open('templates/top.html').read()
#    bottom = open('templates/bottom.html').read()
#    
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

    

#def from_dict():
pages = [   #TURN THIS INTO SOMETHING THAT PUTS OUT FULL HTML FILES
    
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
# I need to write something here that goes through the list and makes
# new docs/ files for site links

#def output_directory(output='', combined=''):
#    open(output, 'w+').write(combined)


def main():

    template = open('templates/base.html').read()
    
    for content in pages:
        html_holder = open(content['filename']).read()
        combined = template.replace('{{content}}', html_holder)
        open(content['output'], 'w+').write(combined)

##        html_holder = open(content['filename']).read()
##        combined_holder = template.replace('{{content}}', html_holder)

##            

##        html_holder = open(content['filename']).read()
##        combined_holder = template.replace('{{content}}', html_holder)
##        open('docs/pta.html', 'w+').write(combined_holder)


##        html_holder = open(content['filename']).read()
##        combined_holder = template.replace('{{content}}', html_holder)
##        open('docs/jiujitsu.html', 'w+').write(combined_holder)  
#        
if __name__ == "__main__":
    main()    
    
    
    
    
    
    #TODO I need to be able to pick a specific item in the 
    # list to assign a newfolder/newfile name



#for html in pages:
#    build_site(position = 'docs/tech.html')
#        filename = open(html['filename']).read()
#        combined_page = template.replace('{{content}}', filename)
#        open('docs/index.html', 'w+').write(combined_page)
#        build_site()
        
#from_dict()
 

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















