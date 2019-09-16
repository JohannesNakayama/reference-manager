import click
import os
import requests
import json

@click.command()
@click.option('--doi', prompt='DOI to look up', help='DOI lookup utility')
def doi_lookup(doi):
    baseurl = 'http://api.crossref.org/works/'
    url = baseurl + doi
    try:
        r = requests.get(url)
        pub_meta = r.json()['message']
        for key in pub_meta.keys():
            print(key)
            print(pub_meta[key])
            print('----------')
    except LookupError:
        print('Something went wrong')

@click.command()
def listfiles():
    f = []
    for (dirpath, dirnames, filenames) in os.walk(os.path.join('unprocessed')):
        f.extend(filenames)
        break
    for i in range(len(f)):
        print(f[i])

@click.command()
def rename_by_doi():
    try:
        files = os.listdir('unprocessed')
    except DIRERROR:
        print('You seem to be in the wrong directory')
    for i in range(len(files)):
        os.rename('unprocessed\\' + files[i], 'unprocessed\\' + str(i) + '.pdf')
    print(os.listdir('unprocessed'))

@click.command()
@click.option('--file', prompt='File to process', help='Utility for reference management')
def process_file(file):
    file_path = 'unprocessed\\' + file
    try:
        os.startfile(file_path)
    except:
        print('Either the file does not exist or you are in the wrong directory.')
    pub_type = input('publication type [either "book", "article" or "other"]:')
    if pub_type == 'article':
        title = input('title:')
        year = input('year:')
        flag = True
        authors = []
        authors.append(input('first author [surname, given name initial(s)]:'))
        while flag:
            flag_val = input('another author? [y\\n]')
            if flag_val == 'n':
                flag = False
            elif flag_val == 'y':
                authors.append(input('author name [surname, given name initial(s)]:'))
            else:
                print('wrong input')
                print('aborted')
                flag = False
        tags = []
        tags.append(input('provide at least one tag:'))
        flag = True
        while flag:
            flag_val = input('another tag? [y\\n]')
            if flag_val == 'n':
                flag = False
            elif flag_val == 'y':
                authors.append(input('provide another tag:'))
            else:
                print('wrong input')
                print('aborted')
                flag = False
        print('publication type: ' + pub_type)
        print('title: ' + title)
        print('year: ' + year)
        print('authors: ' + str(authors))
        print('tags: ' + str(tags))

        # TO DO: save to json file

