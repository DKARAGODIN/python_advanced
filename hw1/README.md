## Ручное тестирование приложения nl
Input:
python nl.py nl.py

Output:
     1  import sys
     2  
     3  ARGS: list = sys.argv[1:]
     4  counter: int = 1
     5  
     6  if len(ARGS) > 0:
     7      for file_name in ARGS:
     8          with open(file_name) as file:
     9              lines = file.readlines()
    10              for line in lines:
    11                  print("{:6d}  {}".format(counter, line), end="")
    12                  counter += 1
    13  
    14  else:
    15      for line in sys.stdin:
    16          print("{:6d}  {}".format(counter, line), end="")
    17          counter += 1

#####
Input:
python nl.py nl.py nl.py

Output:
     1  import sys
     2  
     3  ARGS: list = sys.argv[1:]
     4  counter: int = 1
     5  
     6  if len(ARGS) > 0:
     7      for file_name in ARGS:
     8          with open(file_name) as file:
     9              lines = file.readlines()
    10              for line in lines:
    11                  print("{:6d}  {}".format(counter, line), end="")
    12                  counter += 1
    13  
    14  else:
    15      for line in sys.stdin:
    16          print("{:6d}  {}".format(counter, line), end="")
    17          counter += 1
    18  import sys
    19  
    20  ARGS: list = sys.argv[1:]
    21  counter: int = 1
    22  
    23  if len(ARGS) > 0:
    24      for file_name in ARGS:
    25          with open(file_name) as file:
    26              lines = file.readlines()
    27              for line in lines:
    28                  print("{:6d}  {}".format(counter, line), end="")
    29                  counter += 1
    30  
    31  else:
    32      for line in sys.stdin:
    33          print("{:6d}  {}".format(counter, line), end="")
    34          counter += 1

####
Input:
python nl.py

Output:
asdf
     1  asdf
asdf
     2  asdf


## Ручное тестирование приложения tail
Input:
python tail.py tail.py nl.py

Output:
==> tail.py <==
        print()

elif len(ARGS) == 0:
    cache = []
    for line in sys.stdin:
        cache.append(line)
        if len(cache) > 10:
            del cache[0]
    for line in cache:
        print(line, end="")
==> nl.py <==
        with open(file_name) as file:
            lines = file.readlines()
            for line in lines:
                print("{:6d}  {}".format(counter, line), end="")
                counter += 1

else:
    for line in sys.stdin:
        print("{:6d}  {}".format(counter, line), end="")
        counter += 1


Input:
python tail.py tail.py

Output:
        print()

elif len(ARGS) == 0:
    cache = []
    for line in sys.stdin:
        cache.append(line)
        if len(cache) > 10:
            del cache[0]
    for line in cache:
        print(line, end="")

Input:
python tail.py 

Output:
1
2
3
4
5
6
7
8
9
10
11

2
3
4
5
6
7
8
9
10
11

## Ручное тестирование приложения wc
Input:
python wc.py
asdf
asdf
asdf asdf

Output:
       3        4       20

Input:
python wc.py wc.py
Output:
      47      138     1020 wc.py

Input:
python wc.py wc.py wc.py
Output:
      47      138     1020 wc.py
      47      138     1020 wc.py
      94      276     2040 total
