from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='ai_assistantbot',  # Name of your package
    version='0.0.10',  # Version of the package
    packages=find_packages(),  # Automatically find the packages in your project
    install_requires=[],  # External dependencies (if any)
    description='AssistantBot is a python package which provides an question-answering system designed to process large datasets efficiently. It dynamically matches user queries with relevant data, offering accurate responses and easy training process.',  # A short description
    long_description=README,  # Include the README contents
    long_description_content_type='text/markdown',  # Content type for the description
    author='Wassim Khleifi',
    author_email='wassimkhleifi@gamil.com',
    url='https://github.com/wassim-khleifi/ai_assistantbot',  # Optional: link to your repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
