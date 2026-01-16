import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# Initialize variables
dice_roll = str(random.choices(range(1, 7), k=3))  # Assigned as a string
fixed_dice = []  # Assigned as a list
fixed_dice_str = str(fixed_dice)  # Assigned as a string

# Helper function for logging
def log_game_data(dice_roll, fixed_dice, rerolls):
    data = {"Rolls": [dice_roll], "Fixed Dice": [fixed_dice], "Rerolls": [rerolls]}
    return pd.DataFrame(data)

# Check if player tupled out
if len(set(eval(dice_roll))) == 1:
    print(f"All dice are the same ({dice_roll}), you got 0 points.")
    time.sleep(1)
else:
    # Fix any matching dice
    dice_roll_list = eval(dice_roll)  # Convert string back to list
    for i in range(len(dice_roll_list)):
        for j in range(i + 1, len(dice_roll_list)):
            if dice_roll_list[i] == dice_roll_list[j] and dice_roll_list[i] not in fixed_dice:
                fixed_dice.append(dice_roll_list[i])
    fixed_dice_str = str(fixed_dice)  # Update string version of fixed dice
    print(f"You rolled {dice_roll}. Fixed dice: {fixed_dice if fixed_dice else 'None'}")

# Initialize DataFrame for game history
game_history = log_game_data(dice_roll, fixed_dice_str, 0)

# Add Roll Sum column
game_history["Roll Sum"] = game_history["Rolls"].apply(lambda rolls: sum(eval(rolls)))

# Reroll logic
reroll_count = 0
while True:
    dice_roll_list = eval(dice_roll)  # Convert back to list for operations
    rerollable_dice = [die for die in dice_roll_list if die not in fixed_dice]

    if not rerollable_dice:
        print("No dice left to reroll.")
        break

    print(f"Rerollable dice: {rerollable_dice}")
    choice = input("Do you want to reroll? (yes/no): ").lower()

    if choice == "yes":
        time.sleep(1)
        reroll_count += 1
        new_roll = random.choices(range(1, 7), k=len(rerollable_dice))
        print(f"You rerolled: {new_roll}")

        # Update rerollable dice in the main roll
        rerollable_index = 0
        for i in range(len(dice_roll_list)):
            if dice_roll_list[i] not in fixed_dice:
                dice_roll_list[i] = new_roll[rerollable_index]
                rerollable_index += 1

        # Check if player tupled out
        if len(set(dice_roll_list)) == 1:
            dice_roll = str(dice_roll_list)  # Update the string version
            print(f"All dice are the same ({dice_roll}), you got 0 points.")
            break

        # Update fixed dice
        for i in range(len(dice_roll_list)):
            for j in range(i + 1, len(dice_roll_list)):
                if dice_roll_list[i] == dice_roll_list[j] and dice_roll_list[i] not in fixed_dice:
                    fixed_dice.append(dice_roll_list[i])

        fixed_dice_str = str(fixed_dice)  # Update the string version of fixed dice
        dice_roll = str(dice_roll_list)  # Update the string version of dice roll
        print(f"The following dice are now fixed: {fixed_dice if fixed_dice else 'None'}")
        
        game_history = pd.concat([game_history, log_game_data(dice_roll, fixed_dice_str, reroll_count)], ignore_index=True)
        game_history["Roll Sum"] = game_history["Rolls"].apply(lambda rolls: sum(eval(rolls)))  # Recalculate Roll Sum
    else:
        break

# Final score calculation
if len(fixed_dice) < 3:
    total_points = sum(eval(dice_roll))  # Convert back to list for calculation
    print(f"Your final dice are: {dice_roll}. You scored {total_points} points!")
else:
    print(f"You rolled {dice_roll} and got 0 points due to tuple out.")

# Save game history to a CSV
game_history.to_csv("game_history.csv", index=False)
print("Game history saved to game_history.csv")

# Data visualization
print("Visualizing your game history...")
time.sleep(1)
plt.figure(figsize=(8, 6))
game_history["Roll Sum"].plot(kind="bar", title="Dice Rolls Over Turns", ylabel="Roll Sum", xlabel="Turn")
plt.savefig("game_history_plot.png")
plt.show()

print("Thank you for playing!")
