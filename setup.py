from setuptools import setup, find_packages                          # type: ignore

setup(
    name='emotion_detection',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ibm-watson',
        'flask'
    ],
)

