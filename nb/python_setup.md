# Getting started with Python
This chapter will cover what Python is and how to get Python setup on your computer.

## What is Python?
Python is a programming language. There are many programming languages like C, C++, C#, Julia, Javascript, Matlab, R, etc. There are so many languages because many languages were developed for specific purposes. R is a statistical language, C is a low-level, and Python is general purpose language. Programming languages have different features. Languages can be interpreted or compiled, and statically or dynamically typed. Python is an interpreted language and dynamically typed. An interpreted language mean that there is another program that executes the program that you write. To run an interpreted language you need to install the interpreter. Dynamically vs statically typed is something that we will cover in a later chapter.

There are several benefits of using Python for scientific computing. The first is ease of use. Python has an easy to read syntax and can be run on many different platforms. Python does not have to be compiled which makes it much easier to quickly iterate and build analysis workflows and programs. Most of the code you will write, and that is included here, does not require a deep knowledge of programming principles. You can certainly improved your programs and analysis by learning more about programming but it is not needed. There is much more technical overhead writing in other languages. The second is there is a huge scientific computing ecosystem that had been built which includes in Numpy, Scipy, Statsmodels, ScikitLearn, Matplotlib, Tensorflow, PyTorch and many others. These libraries get around the worst parts of Python (mainly that it is slow) and abstract away some of the hardest parts of scientific programming. Third, Python does not require a license or subscription like Matlab which is one of the two other comparable languages for scientific computing (the other being Julia). Fourth, there are many resources available to learn Python. You will find a lot of repeated examples and shallow tutorials. This book is intended to get past that issue.

The Python interpreter comes with many packages and data stuctures that are useful for general programming. However, most of the power of Python comes from the third party package ecosystem.

## Setting up your Python environment
There are several ways and tools that you can use to help setup your Python environment. I will cover the most common tools you can use to run Python. First we will cover local tools or tools you can run directly on your computer. I will cover how to setup Python on Windows, Mac and Linux since there are differences between each. Then I will cover remote tools, such as Jupyter Notebook and Google Colab where you can run your data on an external resource.

### Local Python
When running Python locally, whatever tool you use you will have to become familiar with using the command-line/terminal. While daunting at first, most of what you will need to know is fairly simple. To run Python locally you will typically need an IDE (intergrated development environment) and I highly recommend some way to manage Python versions. IDEs that people use are VSCode, PyCharm, Spyder and the newer LLM based IDEs. I prefer VSCode because it can make using virtual environments easier and allows you to run Jupyter Notebooks locally. Spyder is probably most like RStudio. Python version control and package managment tools inlcude Anaconda, PyInstaller (Windows only), Pyenv (Mac and Linux), Poetry and Uv.

The biggest thing to note, is that you should get used to using virtual environments with Python. Sometimes Python packages can conflict and cause problems if you install them under the main interpreter. Virtual environments essentially copies the interpreter and creates an isolated environment. I will cover the basics of setting up setting up Python but it is quite hard to cover everything in writing. This is not meant to be comprehensive.

#### Anaconda
The easiest way for many people getting started with Python is to use [Anaconda](https://www.anaconda.com/). Anaconda is a prepackaged Python version and package manager. It comes preinstalled with most of the commonly used scientific Python packages. To get started with Anaconda you can download the full Anaconda or MiniConda. I prefer MiniConda but for those of you who are more comfortable with UIs the full Anaconda might be a better choice to start. Below is some basic instructions to get started with MiniConda.
1. Download and install Miniconda.
2. Open Anaconda prompt/terminal.
3. Create a new virtual environment ```conda create -n getting_started```. You can replace getting started with any name you want.
4. Activate the new virtual environment ```conda activate getting_started```
5. Install some basic python packages ```conda install numpy scipy pandas matplotlib```.
6. Now you are all set. If you are using VSCode you can connect to this environment. Or you can install Jupyter Lab and run Jupyter Notebooks from the virtual environment. It is important to note that you will need to activate your virtual environment each time you want to use it. VSCode will do this automatically.

#### Py Installer (Windows only)
The Py installer is the default installer for Python on Windows which you get [here](https://www.python.org/). Python has installers for Linux and Mac but not the Py installer. The Py installer makes it easy to manage Python versions and create virtual environments. For Windows I also recommed installing Powershell 7. It is easier to use than the commdand prompt or the old powershell. I generally also create a folder somewhere on my compture where I store all the virtual environments that I create.
1. Download and install Python version 3.12.x. 
2. Open Powershell or command prompt.
3. Create a virtual environment ```py -3.12 -m venv getting_started```. This will create a virtual environment in your user folder. The 3.12 is the version number, -m specifies you want to run a python module, venv is the module you want to run and getting_started is the virtual environment name.
4. To activate the virtual environment you will need to go the virtual environment folder you created, open the bin folder and there should be a file name activate.ps. Just drag and drop this file into the powershell or command prompt and hit enter. If you get an error put quotes around the file name before hitting enter.

#### Pyenv (Linux or Mac)
[Pyenv](https://github.com/pyenv/pyenv) is trickier to setup and can be hard if you are not comfortable using the terminal/shell on Linux or Mac.
1. Follow the instructions here: https://github.com/pyenv/pyenv to install and setup up Pyenv.
2. Install Python 3.12: ```pyenv install 3.12```.
3. Set the Python version: ```pyenv global 3.12```
4. Create a virtual environment ```python -m venv getting_started```. This will create a virtual environment in your user folder. The -m specifies you want to run a python module, venv is the module you want to run and getting_started is the virtual environment name.
5. To activate the virtual environment you will need to go the virtual environment folder you created, open the bin folder and there should be a file name activate.ps. Just drag and drop this file into the powershell or command prompt and hit enter. If you get an error put quotes around the file name before hitting enter.

#### Other managers
For other managers such as Poetry and Uv I suggest following their documentation.

### Remote Python
Python can be run remotely on Google Colab or any service that hosts a Jupyter serve. Most universities provide a Jupyter server. For each of these I recommed following the documentation that is available.