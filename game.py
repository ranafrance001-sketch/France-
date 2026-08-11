import random

def play_game():
    high_score = float('inf')  # High score ko infinity se start kiya

    while True:
        print("\n--- 🎮 Guess the Number ---")
        print("Difficulty Select Karein:")
        print("1. Easy   (Range: 1-30,  Lives: 7)")
        print("2. Medium (Range: 1-100, Lives: 5)")
        print("3. Hard   (Range: 1-200, Lives: 5)")

        while True:
            choice = input("\nLevel chunein (1, 2, ya 3): ").strip()
            if choice in ['1', '2', '3']:
                if choice == '1': max_num, lives = 30, 7
                elif choice == '2': max_num, lives = 100, 5
                else: max_num, lives = 200, 5
                break
            print("❌ Sahi option chunein (1, 2, ya 3)!")

        secret_number = random.randint(1, max_num)
        attempts = 0
        current_lives = lives

        print(f"\nGame Shuru! 1 se {max_num} ke beech guess karein.")
        
        while current_lives > 0:
            try:
                guess = int(input(f"[{current_lives} ❤️ Left] Guess: "))
                attempts += 1

                if guess == secret_number:
                    print(f"\n🎉 WINNER! Aapne {attempts} attempts mein jeeta! 🏆")
                    
                    if attempts < high_score:
                        high_score = attempts
                        print(f"🌟 Naya High Score: {high_score} attempts!")
                    else:
                        print(f"High Score abhi bhi: {high_score} attempts hai.")
                    break
                elif guess < secret_number: print("📉 Chhota guess hai!")
                else: print("📈 Bada guess hai!")

                current_lives -= 1
            except ValueError:
                print("❌ Invalid input! Number dalein.")

        if current_lives == 0:
            print(f"\n💀 GAME OVER! Sahi number tha: {secret_number}")

        again = input("\nKya dobara khelna chahte hain? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break

play_game()
