# CS 331 Assignment #2: 4x4 Othello
Othello is a classic two-player, turn-based game in which players try to flip as many pieces over to their color as possible. If you are not familiar with the rules for Othello, please read the following Wikipedia page

In this assignment you will  be implementing the computer opponent for a simplified 4x4 version of Othello using the Alpha-beta search with a few different options.

## Requirements
You will calculate the next move for the computer player using the Alpha-beta and Minimax algorithms. Since we will be using ASCII art to display the board, we will use the symbols X (for the dark player who goes first) and O (for the light player who goes second). A legal move would outflank the enemies pieces in a straight line with your own pieces. The result would turn the outflanked enemy pieces into yours. If a player has no legal move, then the turn passes to the opponent, and if both players cannot move, then the game ends. The win is determined by who has more pieces when the game ends. 

The game starts with X's at (column 1, row 1) and (column 2, row 2) and O's at (column 1, row 2) and (column2, row 1).

The command line allows you to select whether a player is a human player or a computer player. Note that the 4x4 game of Othello is asymmetric; the player moving second has a serious advantage over the player moving first. If the search is exhaustive, the computer player, when going second, should always either win or tie.

The specific things you need to implement for this assignment are:
1. Evaluation functions: The 4x4 version of Othello is small enough that we can generate the entire game tree while doing the Minimax search. However, you will also experiment with shallower searches with an evaluation function. If a terminal state is reached, give an evaluation of 0 for a tie, float("inf") if you win, -float("inf") if you lose. Implement the following 3 evaluation functions:
    - H0, Piece Difference: Number of your pieces - number of opponent's pieces
    - H1, Mobility:  Number of your legal moves - number of opponent's legal moves
    - H2: Design your own function
2. Successor function: You will also need to create a successor function. This function takes the current state of the game and generates all the successors that can be reached within one move of the current state.
3. Alpha-beta/Minimax function: Implement the alpha-beta function in the adversarial search lecture. You will need to implement the Max-Value and Min-Value functions, successor function and different evaluation functions as defined below. Also, you will need to terminate the search once it hits a certain depth defined by the depth parameter.

In addition to the functionality described above, you may need to implement some other code to do things like bookkeeping. You also will need to create a report described below.

## Python Code
For the board, the 0th row starts from the top, and the 0th column starts from the left. The input parameter "prune" is 1 for alpha-beta and 0 for the regular minimax.

**Players.py** is the code that needs to be modified. The code has comments for the return values specified for the functions that need to be changed: alphabeta, eval_board, get_successors. For grading, our testing code will unit test these functions.

**OthelloBoard.py** contains the class definition for an Othello board object and inherits from Board.py. You will need to use functions in OthelloBoard.py.

**GameDriver.py** is the code to run a game of Othello. You don't need to edit this file, but can add your own plotting code if needed. We won't test your plotting functionality, so you can comment it out after you use it.

**run.sh** contains a shell script with some sample commands that start a game. You can choose to have a player be a human or AI. You can run the following:
```
chmod +x run.sh
sh run.sh
```
## Report
1. Search vs. depth: nodes expanded by each search method when you limit the depths  to 2,4,6,8,10 and 12 steps from the starting position. Plot line or bar graphs with the number of nodes vs. depth for pruning on/off and the 3 heuristics.
2. Heuristic quality: Play alpha-beta search with pruning with the 3 heuristics against each other from both sides (X and O) at depths of 2, 4, 6, and 8 (i.e., H1(X) vs H2(O), H2(X) vs. H1(O),  H1(X) vs H3(O), H3(X) vs. H1(O), H2(X) vs H3(O) and H3(X) vs. H2(O).  Report the win-loss results.
3. Write a brief report about how the different heuristics performed against each other in terms of winning rates and amount of search.
