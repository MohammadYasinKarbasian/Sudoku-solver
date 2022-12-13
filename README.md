# Introduction
Sudoku is a logic-based, combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.
[(More about sudoko)](https://en.wikipedia.org/wiki/Sudoku)
<br>
 In this project, our purpose is to solve classic 9 × 9 sudoku using a Genetic algorithm.
 # Features
* Random restart
* Initialization
* Fitness fuction
* Parent selection
* Cross over
* Mutation

## Random restart
If after a number of generations, it didn't converge to a solution, it will restart automatically and start from another random initial state.
## Initialization
We fill the sudoku randomly with two conditions: 1. we have some cells that have constant numbers so we do not change them. 2. in every 3 × 3 cell we mustn't have any replicated number.
## Fitness function
Counts all the threats of every column and every row and subtracts them from 108(108 is the worst case of cells arrangement for our fitness function).
## Parent selection
For every child, we need two parents. We want to have half as many children as the current population, so we choose randomly N pairs of parents (N is the population number), and each parent is chosen randomly with the weight of the fitness function of that parent.
## Cross over
We have two parents, each one has 9 3 × 3 cells. we choose 1 to 8 of 3 × 3 cells from the father (we choose this number randomly) and choose others from the mom.
## Mutation 
We want to don't have any duplicate numbers in every 3 × 3 cell, randomly choose a 3 × 3 cell then swap two non-constant members of it(these two members are chosen randomly).
## Test
Run on easy sample:
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Sudoku-solver$ python3 sudoku.py                                                                 
In generation 1 MAX was 87
In generation 2 MAX was 87
In generation 3 MAX was 88
In generation 4 MAX was 88
In generation 5 MAX was 88
In generation 6 MAX was 91
......
In generation 30 MAX was 106
In generation 31 MAX was 106
In generation 32 MAX was 106
In generation 33 MAX was 108
Wow we find solution:

[[5 7 3 2 8 4 1 9 6]
 [9 4 6 1 5 7 8 3 2]
 [1 2 8 3 9 6 7 4 5]
 [3 5 1 6 7 2 9 8 4]
 [2 8 7 5 4 9 6 1 3]
 [4 6 9 8 3 1 2 5 7]
 [7 3 4 9 2 8 5 6 1]
 [6 9 2 4 1 5 3 7 8]
 [8 1 5 7 6 3 4 2 9]]

```
Run on medium sample:
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Sudoku-solver$ python3 sudoku.py
In generation 1 MAX was 85
In generation 2 MAX was 85
In generation 3 MAX was 87
In generation 4 MAX was 87
In generation 5 MAX was 87
......
In generation 254 MAX was 106
In generation 255 MAX was 106
In generation 256 MAX was 106
In generation 257 MAX was 108
Wow we find solution:

[[7 1 4 9 2 5 8 3 6]
 [6 9 5 8 1 3 2 4 7]
 [2 8 3 4 6 7 5 1 9] 
 [8 7 6 3 5 1 4 9 2] 
 [5 2 1 7 9 4 6 8 3] 
 [3 4 9 2 8 6 1 7 5] 
 [9 6 7 1 4 2 3 5 8] 
 [4 3 2 5 7 8 9 6 1] 
 [1 5 8 6 3 9 7 2 4]]
```
Run on hard sample:
```
yasin@Hunter ~/Documents/Code/iut/ai/github/Sudoku-solver$ python3 sudoku.py                                                            
In generation 1 MAX was 77
In generation 2 MAX was 77
In generation 3 MAX was 77
In generation 4 MAX was 81
In generation 5 MAX was 81
In generation 6 MAX was 81
In generation 7 MAX was 82
In generation 8 MAX was 85
In generation 9 MAX was 85
......
In generation 1803 MAX was 106
In generation 1804 MAX was 106
In generation 1805 MAX was 106
In generation 1806 MAX was 108
Wow we find solution:

[[8 1 3 6 5 4 7 2 9] 
 [4 5 7 2 9 1 3 8 6]
 [6 2 9 3 7 8 1 5 4]
 [7 8 5 4 6 2 9 1 3]
 [2 6 1 7 3 9 8 4 5]
 [9 3 4 1 8 5 6 7 2]
 [3 4 6 8 2 7 5 9 1]
 [5 7 2 9 1 6 4 3 8]
 [1 9 8 5 4 3 2 6 7]]
```
