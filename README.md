README.md 

## **Overview**
This is an interactive dice game built in Python, where the player rolls three dice and tries to score points by fixing dice and rerolling the others. The game tracks each roll, the fixed dice, and the rerolls, storing this information in a game history. The final score is calculated based on the dice rolls unless all dice are the same (a "tuple out"), resulting in zero points.

The game also includes features like data visualization using Matplotlib and data analysis using Pandas, making it both functional and fun.

## **How to Play**
1. The game begins by rolling three dice.
2. If all three dice show the same value, you "tuple out" and score zero points.
3. Otherwise, the game allows you to:
   - Fix any matching dice.
   - Reroll the unfixed dice to improve your score.
4. You can continue rerolling until no dice are left to reroll or until you choose to stop.
5. The final score is calculated based on the sum of the dice values unless you tuple out.

## **Features**
- **Dice Rolling and Fixing**:
  - Automatically identifies and fixes dice with matching values.
  - Allows rerolling of unfixed dice for a better score.

- **Game History Tracking**:
  - Stores data about each roll, including:
    - The values of the dice.
    - The fixed dice.
    - The number of rerolls.
  - Saves the game history to a CSV file (`game_history.csv`).

- **Data Visualization**:
  - Visualizes the sum of dice rolls across turns using Matplotlib.
  - Saves the graph as `game_history_plot.png`.

- **Advanced Timing Features**:
  - Simulates realistic delays using `time.sleep()` for better gameplay experience.

- **Data Analysis with Pandas**:
  - Calculates the sum of dice rolls for analysis.
  - Tracks all gameplay data in a Pandas DataFrame.

---

## **How to Run the Game**
1. Ensure you have Python 3.x installed on your computer.
2. Install the required libraries by running:
   ```bash
   pip install pandas matplotlib
