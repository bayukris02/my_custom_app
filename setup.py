from setuptools import setup, find_packages

setup(
    name='my_custom_app',
    version='0.0.1',
    description='Custom app for ERPNext',
    author='Bayu Krisna',
    packages=find_packages(),
    install_requires=['frappe'],
)
