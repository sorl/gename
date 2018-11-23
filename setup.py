from setuptools import setup


setup(
    name='gename',
    version='0.0.1',
    description='Guess gender from first name.',
    long_description=open('README.md').read(),
    author='Mikko Hellsing',
    author_email='mikko@sumsum.se',
    url='http://github.com/sorl/gename',
    packages=['gename'],
    package_data={'gename': ['names.db']},
    include_package_data=True,
    zip_safe=False,
    license='ICS',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ]
)