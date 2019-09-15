import click
import os
import requests

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