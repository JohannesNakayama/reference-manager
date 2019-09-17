import click
import os
import requests
import json

@click.command()
def rf_help():
    print('''
    Welcome to refman!
    refman is a simple reference management system that allows you to query your literature by self-defined tags.
    The following workflow is suggested for optimal performance:
    
    1) navigate to an empty (!) directory where your refman project should live
    2) rf_init: initialize project
    3) save your pdf file in the directory /files/0_unproc/
    4) rf_list_unproc: list unprocessed files
    5) rf_process: process your files
    6) in step 5, a template for a review is created in the /review folder
    ''')

@click.command()
def rf_init():
    cur_dir = os.listdir()
    if _is_rf():
        print('This seems to be a refman project already.')
    elif len(cur_dir) == 0:
        os.mkdir('0_inbox')
        os.mkdir('files')
        os.mkdir('reports')
        os.mkdir('reviews')
        os.mkdir('data')
        os.mkdir(os.path.join('files', '0_unrev'))
        os.mkdir(os.path.join('files', '1_rev'))
        print('--- initialization successful ---')
    else:
        print('There already are files/directories in your folder.')
        print('Please navigate to an empty directory')
        print('--- aborted ---')

@click.command()
def rf_list_unproc():
    if _is_rf():
        unproc = os.listdir('0_inbox')
        for file in unproc:
            print(file)
    else:
        print('This does not seem to be an refman project.')
        print('Use rf_init to create a refman project.')
        print('--- aborted ---')

@click.command()
@click.option('--file', prompt='File to process', help='Utility for reference management')
def rf_process(file):
    if _is_rf():
        file_path = os.path.join('0_inbox', file)
        ok = True
        try:
            os.startfile(file_path)
        except:
            print('Either the file does not exist or you are in the wrong directory.')
            ok = False
        if ok:
            pub_type = input('publication type [either "book", "article" or "other"]: ')
            if pub_type == 'article':
                data = _article()
                json_string = json.dumps(data, sort_keys=True)
                json_dest = os.path.join('data', 'TEST.json')
                with open(json_dest, 'w') as json_file:
                    json.dump(data, json_file)
                print('Your entry was successfully saved.')
        else:
            print('This file does not seem to exist')
            print('--- aborted ---')
    else:
        print('This does not seem to be an refman project.')
        print('Use rf_init to create a refman project.')
        print('--- aborted ---')

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
def rename_by_doi():
    try:
        files = os.listdir('unprocessed')
    except DIRERROR:
        print('You seem to be in the wrong directory')
    for i in range(len(files)):
        os.rename('unprocessed\\' + files[i], 'unprocessed\\' + str(i) + '.pdf')
    print(os.listdir('unprocessed'))

def _is_rf():
    cur_dir = os.listdir()
    a = '0_inbox' in cur_dir
    b = 'files' in cur_dir
    c = 'reports' in cur_dir
    d = 'reviews' in cur_dir
    e = 'data' in cur_dir
    if a and b and c and d and e:
        return True
    else:
        return False

def _article():
    title = input('title: ')
    year = input('year: ')
    flag = True
    authors = []
    authors.append(input('first author [surname, given name initial(s)]: '))
    while flag:
        flag_val = input('another author? [y/n] ')
        if flag_val == 'n':
            flag = False
        elif flag_val == 'y':
            authors.append(input('author name [surname, given name initial(s)]: '))
        else:
            print('wrong input')
            print('--- aborted ---')
            flag = False
    tags = []
    tags.append(input('provide at least one tag: '))
    flag = True
    while flag:
        flag_val = input('another tag? [y/n] ')
        if flag_val == 'n':
            flag = False
        elif flag_val == 'y':
            authors.append(input('provide another tag: '))
        else:
            print('wrong input')
            print('--- aborted ---')
            flag = False
    entry = {
        'title': title,
        'year': year,
        'authors': authors,
        'tags': tags
    }
    return entry