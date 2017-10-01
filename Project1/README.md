# INTRO TO ARTIF INTEL PROJECT1
    maze game
## Algorithm
### DFS
Include two Python file, DFS.py and DFS_optimal.
DFS.py is an implement of Breadth-first search. Only find the first path from start node to the end node.
DFS_optimal.py is an implement of Breadth-first search. Will keep running until find the shortest route.
### BFS
BFS.py is an implement of Depth-first search. Always finds the shortest path when it finish.
### A*
A* is a modification of UFCS Algorithm that is optimized for a single destination.
UFCS Algorithm can find paths to all locations; A* finds paths to one location.
It prioritizes paths that seem to be leading closer to the goal.
ASTAR_EUC.py is an implement of A* using Euclidean Distance.
ASTAR_MHT.py is an implement of A* using Manhattan Distance.
### Genetic Algorithm

## Statistics Script
### Question 1

### Question 2
Question2 file include visualization by HTML and Python Script.
Question2.py is a data generate Script.
First it generate a random solvable maze with requested size.
Then, run all 4 algorithm on this maze.
At last, print the solutions and save it to data.js file.
Visualization is built by HTML5UP frame.
See Visualization chapter for more visualization detail.
### Question 3
Question3.py run DFS algorithm to determine if this map has a solution.
This Script will run from p = 0.0 to p = 1.0.
However, there usually no solvable maze when maze is randomly generated with p above 0.4.
So this Script will coming to a stop when p is over 0.43.
And run 100 times to see how many percentage mazes are solvable.
### Question 4
Question4.py run BFS algorithm to find the average length of the shortest path.
Also run DFS on this to show what other path distance is.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
### Question 5
Question5.py run A* Manhattan Distance algorithm to find the average length of path.
Also run DFS on this to compare with it.
This Script will run from p = 0.0 to p = 0.4.
And run 32 times to  get the average.
### Question 6
Question6.py run A* Manhattan Distance and A* using Euclidean Distance algorithm to find the average number of nodes expanded in total for a random map.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
### Question 7 BFS/DFS
Question7_BFS.py run BFS algorithm to determine if this map has a solution.
If it is solvable, find the average number of nodes expanded in total for a random map.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
Question7_DFS.py using DFS algorithm to determine if this map has a solution.
If it is solvable, find the average number of nodes expanded in total for a random map.
This Script will run from p = 0.0 to p = 0.4.
And run 100 times to  get the average.
## Visualization
### index.html
index.html is a HTML with JavaScript.
JavaScript will read the data.js file and show the result in web page.
Please double click the index.html and check out the web page~
### data.js
Contain data in JSON form. Import to HTML file as a "*.js" file.
Data include the original map and the solution provided by all 4 algorithm.
