# US-States-Game

Name as many states in the US as you can in this educational geography game.

## Description

This is an interactive learning game built with Python and Turtle graphics where players test their knowledge of US geography. Players need to name all 50 US states by typing them in. The game:
- Shows a blank map of the United States
- Allows players to input state names
- Marks correct guesses on the map
- Tracks progress with a score counter
- Creates a CSV file of missed states for future learning

## Requirements

- Python 3.x
- pandas
- turtle (comes with Python standard library)

## Usage

1. Run the game:
```sh
python main.py
```

2. Type in US state names when prompted
3. To exit the game, type 'Exit'
4. Check 'states_to_learn.csv' for states you missed

## Game Features

- Real-time feedback on correct guesses
- Progress tracking (X/50 states)
- Automatically saves missed states for review
- Clean and intuitive interface

## Data Sources

The game uses a CSV file containing coordinates for all 50 US states, allowing precise placement of state names on the map.

## License

This project is open source and available under the MIT License.
