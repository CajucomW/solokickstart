pages = []

template = open('templates/base.html').read()

def main():
    for content in pages:
        html_file = open(content['filename']).read()
        combined = template.replace('{{content}}', html_file)
        open(content['output'], 'w+').write(combined)

        # I can't get this to work.

#            new_title = template.replace('{{title}}', content['title'])
#            open(content['output'], 'w+').write(new_title)

if __name__ == "__main__":
    main()   














