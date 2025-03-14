# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.


## Team Members
- **Haoxuan Lin(Steve)**: [Echoudexigaigu](https://github.com/Echoudexigaigu)
- **Jiaxi Zhang**: [SuQichen777](https://github.com/SuQichen777)
- **Zhiheng Pan**: [pzhiheng](https://github.com/pzhiheng)


 
 ## Project Overview
 
 ## Pypl Project Link
 
 ## Steps Needed to Contribute
 - Clone the repo
 ```bash
 git clone https://github.com/software-students-spring2025/3-python-package-se_project3/blob/main/instructions.md
 cd 3-python-package-se_project3
 ```
 - Create a new branch
 ```bash
 git checkout -b <branch-name>
 ```
 - Install pipenv, build, and twine if you don't have them
 ```bash
 python3 -m pip install --user pipenv
 python3 -m pip install --upgrade build
 pip3 install twine
 ```
 - Create a virtual environment and install dependencies
 ```bash
 pipenv install pytest-cov --dev
 ```
 - Activate the virtual environment
 ```bash
 pipenv shell
 ```
 - Exit the virtual environment
 ```bash
 exit
 ```
 
 ## Steps to Run the Tests
 - Activate the virtual environment
 ```bash
 pipenv shell
 ```
 - Run the tests without success output
 ```bash
 pytest
 ```
 - Run the tests with success output
 ```bash
 pytest -s
 ```