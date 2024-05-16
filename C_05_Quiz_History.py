    # Round ends here

    # if user has entered exit code, end game!!
    if end_game == "yes":
        break

    rounds_played += 1

    # Add round result to game history
    history_feedback = f"Round {rounds_played}: {feedback}"
    game_history.append(history_feedback)

    # add guesses to score list
    all_scores.append(guesses_used)

    # increase rounds if user is in infinite mode
    if mode == "Infinite":
        num_rounds += 1

# Game loop ends here

# check users have played at least one round before calculating statistics
if rounds_played > 0:
    # Game History / Statistics area

    # Calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n📊📊 Game Statistics 📊📊")
    print(f"Best: {best_score} | Worst: {worst_score} | Average: {average_score:.2f} ")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history?: ")
    if see_history == "yes":
        print()
        print("🎮🎮 Game History 🎮🎮")
        for item in game_history:
            print(item)

# End program if user hasn't played a round
else:
    print("😲😲 Oops - You chickened out! 😲😲")