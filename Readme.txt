#Running a python script for rod cutting and wood board cutting algorithms through Visual Studio Code.

Here in problem 1 we used cut rod algorithm to find maximum Revenue and for problem2 we used Wood Board Cutting algorithm to determine the minimum total cost of cutting a wood board, which involves dividing the board into four pieces with each cut, creating four smaller sub-pieces. It does all permutations and combinations of the board-cutting with the given cuts or points and comes up with minimum cost and optimal order of the cuts. 

#prerequisites
Make sure these are installed on your system

Visual Studio Code : Download and Install VS code from [https://code.visualstudio.com/]
Python             : Download and Install Python from [https://www.python.org/downloads/]
System properties > Advanced > Environment Variables > add the path of python file
Python Extension   :  Install the python extension code by Microsoft(Eligible for vesions python >=3.7)

#Open the project in vs code
File > Open Folder > /path/to/yourproject

(Optional)
#To isolate dependencies create a Virtual Environment using the terminal
python -m venv venv
venv\Scripts\activate

On mac and linux to activate  source venv/bin/activate

Environment dependencies:

Python      : Version 3.8 and above
Interpreter : 3.8.10 64 bit(Microsoft) 
System Requirements: This can run on any operating system but it should follow the above steps mentioned.
random and timeit libraries are inbuilt in python 3.8 version, no need to install or upgrade it.
To install External dependencies use pip install in integrated terminal.

# To run the python script
Open the integrated terminal in the vs code  
view > terminal
python board_cut.py
python cut_rod.py