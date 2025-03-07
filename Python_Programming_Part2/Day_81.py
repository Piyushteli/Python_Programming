"""
Modules:
    Module is the python file that containing the functions ,classes and variables

Built in Modules in Python
1. math - Mathematical functions
2. string - String manipulation functions
3. fileio - File input/output functions (not a module, but a set of functions)
4. os - Operating System interfaces
5. sys - System-specific functions
6. re - Regular Expressions
7. time - Time-related functions
8. datetime - Date and Time classes
9. random - Random number generators
10. statistics - Statistical functions
11. collections - Container data types (e.g. lists, sets, dictionaries)
12. functools - Higher-order functions
13. itertools - Iteration tools
14. json - JSON encoding and decoding
15. csv - Comma-separated value file handling
16. xml - XML handling
17. urllib - URL handling
18. threading - Threads
19. multiprocessing - Process-based parallelism
20. logging - Logging
21. html - HTML handling
22. http - HTTP modules (e.g. http.client, http.server)
23. email - Email handling
24. sqlite3 - SQLite database
25. pickle - Object serialization
"""

#1)Math Module in python
"""
Function in Math Module
1)math.ceil()
2)math.floor()
3)math.fabs():Returns the absolute value
4)math.factorial()
5)math.fsum()
6)math.sqrt()
7)math.pow()
8)math.sin()
9)math.cos()
10)math.log()

for more function visit the link:
            https://docs.python.org/3.7/library/math.html

"""
import math
x=10.5
print(math.ceil(x))
print("--------------------------")
import math
x=10.5
print(math.floor(x))
print("--------------------------")
import math
x=-20
print(math.fabs(x))
print("--------------------------")
import math
x=5
print(math.factorial(x))
print("---------------------------")
import math
l=[10,20,30,40]
print(math.fsum(l))
print("----------------------------")
import math
print(math.sqrt(9))
print("-----------------------------")
import math
print(math.pow(2,3))
print("----------------------------")
print(math.sin(30))
print("--------------------------------")
print(math.cos(90))
print("--------------------------------")
print(math.log(2.74))
print("--------------------------------")
