Sudoku v0.3 Terminal Edition

This is a simple command-line program to solve, generate, or check the uniqueness of the sudoku grid.
The program has been written in Python and converted to a standalone exe version by py2exe. 

I wanted to make a playable version in pygame, but I realized that it wouldn't be finished before the end of the year, so it has to be a terminal edition for now.

Usage:
  py sudoku_v03_terminal.py [import] [filename.txt]
   - import sudoku board from file and solve it.
  py sudoku_v03_terminal.py [check] [filename.txt]    
   - import sudoku board from file and check if it is valid (has one, unique solution).
  py sudoku_v03_terminal.py [generate] [number_of_empty_spots] [*optional_filename.txt]
   - generate a sudoku board with a given number of empty spots (from 1 to 81) and export it into a file.
  py sudoku_v03_terminal.py [new] [*optional_filename.txt]
   - write a new sudoku board, line by line, and export it to file.