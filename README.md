Snake Game with Data Structures 
This project is a simple implementation of the classic Snake game using Python and the Pygame 
library. The game incorporates fundamental data structures such as a deque for managing the snake's 
body and ensures smooth gameplay with intuitive controls and scoring. 
Features 
• Classic Gameplay: Navigate the snake to collect food and grow while avoiding collisions. 
• Smooth Movement: The snake's movement is controlled using the arrow keys. 
• Dynamic Scoring: Your score increases as the snake grows. 
• Restart Option: Press P to restart the game after losing or Q to quit. 
Requirements 
To run this game, you need: 
• Python 3.x 
• Pygame library 
You can install the Pygame library using pip: 
pip install pygame 
How to Play 
1. Run the Game: Execute the script by running the following command in your terminal:  
2. python snake_game.py 
3. Controls:  
o Use the arrow keys to control the snake's direction. 
o Avoid colliding with the walls or yourself. 
o Collect the red blocks (food) to grow the snake and increase your score. 
4. Game Over:  
o If the snake collides with the wall or itself, the game ends. 
o You can press P to restart or Q to quit. 
Code Structure 
Main Components 
• Screen Setup: Initializes the Pygame display and sets up screen dimensions and colors. 
• Snake Management: The snake's body is managed using a deque, which ensures efficient 
additions and removals of segments. 
• Food Generation: Randomly places food on the grid. 
• Collision Detection:  
o Checks if the snake collides with the walls or itself. 
o Detects when the snake eats food and grows. 
• Game Loop:  
o Handles events (keyboard input, quitting). 
o Updates the game state and redraws the screen. 
Functions 
• display_score(score): Displays the player's score in the top-left corner of the screen. 
• draw_snake(snake_body): Draws the snake on the screen. 
• message(msg, color): Displays a message at the center of the screen (e.g., "You lost!"). 
• main_game(): The core game loop, handling all game logic and rendering. 
Enhancements 
Here are some potential improvements you can make: 
1. Increase Difficulty: Gradually increase the snake's speed as the score grows. 
2. Obstacles: Add static or dynamic obstacles to make the game more challenging. 
3. High Scores: Save and display the highest score across sessions. 
4. Themes: Add options for different color schemes or snake/food designs. 
5. Multiplayer Mode: Introduce a second player with a separate snake. 
Example Output 
• Starting Screen: The snake appears in the center of the screen, and food is placed randomly. 
• Gameplay: The snake grows as it collects food, and the score updates dynamically. 
• Game Over: A message is displayed with the final score, and options to restart or quit. 
