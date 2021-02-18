from setuptools import setup

setup(
    name='screenless',
    author='Damian',
    author_email='damiamcz@mailfence.com',
    packages=['screenless'],
    install_requires=['readchar'],
    version='0.1',
    license='MIT',
    description=(
        'Package for creating applications that don\'t require the user to'
        'look at the computer screen.'
    )
)
