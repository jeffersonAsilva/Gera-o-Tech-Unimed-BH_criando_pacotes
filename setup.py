from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_linear_regression",
    version="0.0.2",
    author="jefferson",



    long_description_content_type="text/markdown",
    url="https://github.com/jeffersonAsilva/Gera-o-Tech-Unimed-BH_criando_pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3',
)
