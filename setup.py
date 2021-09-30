import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Snippets',
    version='0.0.1',
    author='null',
    author_email='null',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='null',
    project_urls = {
        "null"
    },
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)
