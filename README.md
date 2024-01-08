UTA Data Bootcamp Module 3
==========================

Riley Taylor  
2024-Jan-08


If you are my grader, please let me know what it is you are looking for in a README. I can be more or less detailed and I can find a coding standard/readme structure of preference if you like. For the time being, I'm sort of just throwing sources and basic summaries of my approach into this. 


## PyBank 

*Setup and related info*

PyBank's main.py only runs properly if the working directory is the PyBank directory. I did not include commands to set the working directory, so please run the script from there. It has a fairly fragile method of referencing the data and output files by just referencing a literal, and there is no config/injected initiailization.

The main does not have any other defined functions because it is fairly simple, but it could definitely be cleaned up, particularly with how I managed to work around the changes (in C++ I'd create a struct for this, but in Python a list of size 2 works, just with some tricky initilization). I also tried playing with try and except clauses in python here, to try to exercise at least some best principles, but since the input data will not be changing, it really wasn't necessary. 

## PyPoll

*Setup and related info*

Similar to PyBank, PyPoll requires that you run the main script from the PyPoll directory, and it will write to the pypoll_analysis.txt file in the analysis directory under PyPoll. I had already figured out the writing to a file method in PyBank, so most of this was pretty routine. The workhorse of the algorithm is the candidateVoteDict dictionary, which houses candidates as keys and their vote counts as the correlating value. Everything else was pretty much string formatting. 

## Sources

### https://stackoverflow.com/questions/2414667/python-string-class-like-stringbuilder-in-c

This source was used to motivate my approach for writing the analysis to a file in the PyBank project. Having already been acquainted with StringBuiler from C# and stringstream in C++, I was looking for some equivalent in Python. I found that just using "&lt;string delimiter&gt;.join(&lt;valid list&gt;)" would probably suffice for my interests. 

### https://www.digitalocean.com/community/tutorials/python-join-list

This was another source that helped me with using the join() method.

### https://stackoverflow.com/questions/74557297/f-string-with-percent-and-fixed-decimals

This source was used to help with the PyPoll f string formatting to convert the numbers into percentages without hard coding it.

### https://docs.python.org/3/library/stdtypes.html#typesmapping
### https://docs.python.org/3/tutorial/datastructures.html#dictionaries
### https://docs.python.org/3/tutorial/inputoutput.html
### https://docs.python.org/3/library/io.html#io.TextIOBase.write

I don't believe I should need to reference these, but I used several sections in Python's official documentation/tutorials to answer some syntax/method questions on dictionaries/lists/io. 