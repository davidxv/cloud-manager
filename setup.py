from distutils.core import setup

setup(
    name='cloudmanager',
    version='0.2.0',
    author='Hugo Peixoto',
    author_email='hugo.peixoto@gmail.com',
    packages=['cloudmanager'],
    scripts=[],
    url='https://github.com/super3/cloud-manager',
    license='LICENSE.txt',
    description='Manages a pool of files uploaded to "the cloud"',
    long_description=open('README.md').read(),
    install_requires=[
        'plowshare >= 0.2.0',
        'sqlite3',
    ],
)