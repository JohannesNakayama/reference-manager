from setuptools import setup

setup(
    name='refman',
    version=0.1,
    install_requires=['Click',],
    py_modules=['refman'],
    entry_points='''
    [console_scripts]
    doi_lookup=refman:doi_lookup
    listfiles=refman:listfiles
    '''
)