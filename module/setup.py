from setuptools import setup

setup(
    name='refman',
    version=0.1,
    install_requires=['Click',],
    py_modules=['refman'],
    entry_points='''
    [console_scripts]
    rf_help=refman:rf_help
    rf_init=refman:rf_init
    rf_list_unproc=refman:rf_list_unproc
    rf_process=refman:rf_process
    '''
)