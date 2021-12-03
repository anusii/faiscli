from setuptools import setup, find_packages

REQUIREMENTS = ['Click']

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Admin',
    'License :: OSI Approved :: GPLv3 License',
    "Operating System :: OS Independent",
    'Programming Language :: Python :: 3',
    ]

setup(
    name="fais",
    version='0.0.0',
    description="Access FAIS functionality from the command line",
    author='Graham Williams',
    author_email='graham.williams@anu.edu.au',
    license='GPLv3',
    packages=find_packages(),
    entry_points={'console_scripts': ['fais = fais:cli']},
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
)
