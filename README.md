# Game
Game is a Python-written program. In this program several classes are written, which are interconnected and are then used in another program, which prescribes the details of the game, which are the objects of these classes.
## Сomponents of the program
The program consists of three functions. 
5 classes are written in this program.

The first class "Room" represents the rooms that are locations in the game. Objects of this class have only one attribute - the name. It also implements functions that can be used to create game details, return relevant information to the player, there is also a function that allows the player to move between rooms

The second class "Character" represents all the characters in the game. Objects in this class have two attributes, a name and a description. Also in this class there are functions with which the player can interact with the characters of the game.

The third class "Enemy" represents the enemies in the game. This class is a subclass of "Character". Objects have two attributes - name and description. Also in this class there is a function that takes the name of the artifact, with which the player can defeat this enemy.

The fourth grade "Friend" represents the friendly characters in the game. This class is a subclass of "Character". Objects have two attributes - name and description.

The fifth class "Item" presents artifacts that the player can collect in the room. Objects of this class have one argument - the name. Also in this class there are functions which receive the description of an artifact, return the description and the name of an artifact.

## The results of the program
The program displays relevant information to the player. The player has a certain set of teams. The course of the game depends on which team the player enters. The game ends when the player defeats 2 enemies or loses the battle
## An example of how this program works

![20220415_203729](https://user-images.githubusercontent.com/87234112/163603148-2fb25e81-dce7-4cc8-9240-6a59cdcd5523.png)
