from setuptools import setup, find_packages

setup(
    name='pre-commit-hooks',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'check-import-order=check_import_order:main',
        ],
    },
)
