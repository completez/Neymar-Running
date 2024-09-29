# NEYMAR RUNNING - A Simple Game with Login Functionality

This project implements a simple game where the player controls a character (Neymar) running and jumping over obstacles while collecting coins. The game includes a login screen, requiring the user to enter a username and password before proceeding. The character image is customizable, and the choice of image is saved in a config file for future use.

## Prerequisites

1. **Python** 3.x
2. **Pygame** for creating the game environment

## Setup Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/completez/Neymar-Running.git
cd Neymar-Running
```
###Step 2: Install Dependencies
Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

###Step 3: Configure the `config.txt`
On the first run, after a successful login, the program will prompt you to input a character image filename (e.g., neymar.png). The selected image file is saved in config.txt and will be loaded automatically on subsequent runs.

###Step 4: Running the Game
To run the game, use the following command:

```bash
python main.py
```
Step 5: Game Instructions
Login: When you start the game, you'll be presented with a login screen. Enter the username and password.
  1.Default credentials:
  Username: `user`
  Password: `pass`
  Character Selection: 
  2.After a successful login, the program will prompt you to input the filename of your character image. For example, if you want to use Neymar's image, you can input `neymar.png` (ensure the       image file         exists    in the project directory).
  3.Gameplay:
  The game screen will display your selected character running across the screen.
  Press the spacebar to jump and avoid obstacles.
  Collect coins to increase your score.
  
###Project Structure
**config.txt**: Stores the selected character image filename.
**main.py**: Main entry point for the game.
**README.md**: Documentation for the project.

##Functionality Overview
**Login System**: Prompts the user for a username and password before starting the game. Correct credentials are required to proceed.
**Image Selection**: Allows users to select and load a custom image for the player character. The selected image is saved in config.txt for future runs.
**Obstacle and Coin Generation**: Randomly generates obstacles and coins on the screen. The player must jump to avoid obstacles and collect coins for points.
**Character Control**: The player can jump using the spacebar. The game includes a double jump functionality.

##Example
To play the game:

Start the game with:

```bash
python main.py
```
Input the following credentials at the login screen:

  Username: `user`
  Password: `pass`
  Enter the filename of the character image (e.g., `neymar.png`).


##Troubleshooting
  **Character image not found**: Ensure the image file exists in the project directory. If not found, the program will prompt you to input a valid image filename.
  **Login issues**: Verify that you're entering the correct default credentials:
  Username: `user`
  Password: `pass`

##Enjoy the game!
