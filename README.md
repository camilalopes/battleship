# Battleship

Game developed as an activity of the discipline Artificial Intelligence.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Things you need to run this project

* Python 3.7
* NumPy package 1.16.2

### Running

Clone or download this repository

```
$ git clone https://github.com/camilalopes/battleship.git
```

Install the requirements

```
$ pip install -r requirements.txt
```

Execute

```
$ python game/game.py
```

## Artificial Intelligence

This game has two different intelligence strategies to implement how the computer will play and interact.

### PC2 logic

* Sorting a number of random (x, y) positions to move
* Calculate the best playing position using Euclidean distance. In other words, the closer the position is to an already assertive position, that hit a ship earlier, the better its fit and consequently it have more chances of hitting a ship

* **IMPORTANT**
    -  When the computer hits a ship the position is saved in a control list (hit_positions), which will be used in the distance calculation.
    -  When the ship is completely sunk, its positions are removed from the control list, so that ship are disconsidered in the distance calculation.

## Statistics and Tests

A few tests were performed to verify the correctness of each intelligence strategy

### PC1 vs. PC2

A test considering 100 executions with PC1 and PC2 playing against each other was run, the result counted 53% of victory to PC2 and 47% of victory to PC1. Basically a technical tie.

### PC2 vs. Human

A test considering 10 executions with PC2 and a Human playing against each other was run, the result counted 40% of victory to PC2 and 60% of victory to Human. We intend to improve this test with more executions.

## Authors

* **Camila Lopes** - [camilalopes](https://github.com/camilalopes)
* **Giovani Moutinho** - [mgiovani](https://github.com/mgiovani)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
