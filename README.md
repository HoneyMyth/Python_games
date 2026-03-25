# Star Duels

A 2D arcade-style space shooter built with Python and Pygame. Pilot your ship, dodge incoming meteors, and blast them out of the sky to rack up points!

## Features
* **Omnidirectional Movement:** Smooth 8-way player movement with normalized diagonal speeds.
* **Combat System:** Laser firing mechanics with built-in cooldowns.
* **Dynamic Enemies:** Meteors spawn at randomized intervals and travel at varying trajectories.
* **Collision Detection:** Accurate hitbox tracking for lasers, meteors, and the player.

## Prerequisites
* Python 3.13+
* Pygame 2.6.1

## Installation

1.  **Clone or download the project files.**
2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Directory Structure
For the game to successfully locate its image assets, your project folders must be arranged exactly like this. The script containing the game logic must be run from a directory that sits right next to the `space_shooter` folder:

```text
Your_Project_Folder/
│
├── Project_1/                 # The folder where you run the script
│   └── main.py                # Your game code goes here
│
└── space_shooter/             # Asset folder (must be one level up from the script)
    └── images/
        ├── player.png
        ├── star.png
        ├── laser.png
        └── meteor.png
