from setuptools import setup, find_packages

setup(
    name='pf-auth',
    version='0.0.1',
    url='https://github.com/problemfighter/pf-flask-react',
    license='Problem Fighter License',
    author='H.M.Touhid Mia',
    author_email='codegen@problemfighter.com',
    description='',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'bcrypt>=3.2.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
