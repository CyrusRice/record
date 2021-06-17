from setuptools import setup
setup(name='record', 
    version='0.1',
    description='Record Creating Python Package', 
    author='@cyrus', 
    author_email='', 
    license='MIT', 
    packages=['record'],
    install_requires=
    [
        'PyMySQL'
    ],      
    zip_safe=False)
