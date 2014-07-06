from setuptools import setup

description  = ''.join([
    'Django mini-framework for RESTful web services inspired by ',
    'the book "RESTful Webservices Cookbook" by O\'Reilly.'
])

try:
    with open('README.md') as f:
        long_description = f.read()
except IOError:
    long_description = description

setup(
    name = 'django-restful',
    version='0.2-alpha',
    description = description,
    author = 'Antonio Ognio',
    author_email = 'antonio@ognio.com',
    url = 'https://github.com/gnrfan/django-restful',
    long_description = long_description,
    packages = ['django_restful'],
    install_requires = ['django >= 1.6'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',                            
        'Framework :: Django',                                       
        'Intended Audience :: Developers',                           
        'License :: OSI Approved :: BSD License',                    
        'Operating System :: OS Independent',                        
        'Programming Language :: Python',                            
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Topic :: Utilities'                                       
    ]
)
