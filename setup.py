from setuptools import setup, find_packages
setup(
    name="mcgen",
    version ="0.1.0",
    author="Akshat Mishra",
    author_email="makshat146@gmail.com",
    install_requires=["ollama", "langchain", "streamlit","PyPDF2", "python-dotenv"],
    packages=find_packages(),
)