from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='jfcli',
    version='0.0.2',
    description='CLI for JFrog Artifactory',
    long_description=readme,
    author='David',
    author_email='davidp@jfrog.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)