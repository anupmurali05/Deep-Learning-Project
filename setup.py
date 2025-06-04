import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Deep-Learning-Project"
AUTHOR_USER_NAME = "anupmurali05"
SRC_REPO = "CNNClassifier"

setuptools.setup(
    name=SRC_REPO,      
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for CNN Classifier",
    long_description=long_description,  
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)