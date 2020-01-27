from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name='causeinfer',
    version='0.0.5',
    description='Machine learning based causal inference/uplift in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(),
    license='MIT',
    url="https://github.com/andrewtavis/causeinfer",
    author='Andrew Tavis McAllister',
    author_email='andrew.t.mcallister@gmail.com'
)

install_requires = [
    'os',
    'numpy',
    'pandas',
    'random',
    'scikit-learn',
    'seaborn',
    'requests',
    'urllib',
    'zipfile'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)