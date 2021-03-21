from setuptools import setup, find_packages

setup(
    name="binding-scanner",
    version="0.1.0",
    author="Krish Agarwal",
    author_email="akrish136@gmail.com",
    description="Lightweight, flexible Flask/Gunicorn-based \
                    Binding Scanner implementation",
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/krish8484/binding-scanner.git",
    packages=find_packages(),
    keywords=(
        "binding scanner biotechnology rest restful api app server openapi "
        "swagger mongodb python flask"
    ),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["connexion", "Flask-Cors", "Flask-PyMongo"],
)
