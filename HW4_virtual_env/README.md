## HW4 - Virtual environment requirements 

The programmer Mike was interested in virtual environments and decided to research it. 
After many years of research he published a paper, the code is available (https://github.com/krglkvrmn/Virtual_environment_research). 
However, this code is not easy to use for others...

**The file requirements.txt contains a list of all Python libraries, necessary to launch the file pain.py**


The script was tested on macOS Big Sur 11.6, Python 3.10.0.

#### Instructions:
- download the files pain.py and requirements.txt
- install the library for creating virtual environments (in case tou do not have it)
```
python3 -m pip install virtualenv
```
- create the virtual environment in your current directory
```
python3 -m virtualenv any_name_that_you_like
```
- activate the virtual environment
```
source any_name_that_you_like/bin/activate
```
- install necessary packages listed in requirements.txt
```
python3 -m pip install -r requirements.txt
```
- launch pain.py
```
python3 pain.py
```
