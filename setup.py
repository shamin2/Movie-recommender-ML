from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Movie Recommender System Using-Machine Learning"
AUTHOR_NAME = "Shamin Yasar"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author = "Shamin Yasar",
    description="A Movie Recommender System where it will recommend you similar movies based on ur search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="shaminyasar2001@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.9.13",
    install_requires=LIST_OF_REQUIREMENTS
)