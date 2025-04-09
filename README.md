# Tic Tac Toe

Tic Tac Toe is a Python terminal game, which runs in the Code Institute mock termnal on Heroku.

User will try to beat the computer by making one of the winning combinations before the computer makes.

![Tic Tac Toe](tic-tac-toe.PNG)

## How to play

- Start the game and choose the difficulty
    - 1 = Easy (computer makes random moves)
    - 2 = Difficult (computer makes smart moves)

- You play as 'x', the computer plays as 'o'.

- Pick a cell by entering a number (1–9) based on this layout:

    ![Possible Moves](tic-tac-toe-possible-moves.PNG)

- The first to get three in a row wins.

- A full board with no winner is a draw.

- At the end of the game, you can play again or exit.

## Features

### Existing Features

- Single-player mode against the computer

- Two difficulty levels: Easy and Difficult

- Interactive CLI interface with a clear 3×3 board layout

- Replay option after each round

- Score tracking for user and computer

- Move validation to prevent invalid inputs

- Winning combination display after each round

### Future Feature

- Add impossible level (minimax algorithm)

## Testing

- Given invalid inputs for the level and moves and get a proper error message.

- Pased the code through a PEP8 checker and confirmed that there are no errors.

- Tested in local terminal and Heroku terminal.

## Bugs

- The first time I wrote the function "get_available_cells", I did a mistake and the the funciton returned always the first available cell.

## Code Validating

- PEP8
    - No errors

## Deployment

The project was deployed using GitHub and Code Institute's mock terminal for Heroku.
