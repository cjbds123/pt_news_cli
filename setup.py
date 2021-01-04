from setuptools import setup
setup(
    name = 'ptnews',
    version = '0.1.0',
    packages = ['ptnews'],
    entry_points = {
        'console_scripts': [
            'ptnews = ptnews.__main__:main'
        ]
    })