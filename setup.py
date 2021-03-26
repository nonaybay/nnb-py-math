from setuptools import find_packages, setup


setup(
    name='nnbmath',
    packages=find_packages(),
    version='0.0.1',
    description='(WIP) Uma alternativa para o módulo "math" embutido no python.',
    author='N0N4YB4Y',
    author_email='rafaelvenancio@protonmail.com',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest>=0'],
    test_suite='tests',
)
