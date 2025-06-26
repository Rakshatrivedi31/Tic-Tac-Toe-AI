# main.py
from ai import get_best_move, is_winner
from colorama import Fore, Style, init
init(autoreset=True)

def print_board(board):
    emoji_board = []
    for i, val in enumerate(board):
        if val == "X":
            emoji_board.append(Fore.RED + "❌" + Style.RESET_ALL)
        elif val == "O":
            emoji_board.append(Fore.GREEN + "⭕" + Style.RESET_ALL)
        else:
            emoji_board.append(Fore.YELLOW + str(i) + Style.RESET_ALL)

    print()
    for i in range(3):
        print(" | ".join(emoji_board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def main():
    user_score = 0
    ai_score = 0

    while True:
        board = [" "] * 9
        current_player = "X"

        print("\n🎮 " + Fore.CYAN + "Welcome to Smart Tic-Tac-Toe! You are ❌ (X), AI is ⭕ (O)")

        while True:
            print_board(board)

            if current_player == "X":
                try:
                    move = int(input(Fore.YELLOW + "Your move (0-8): "))
                    if board[move] != " ":
                        print(Fore.RED + "Invalid move. Try again.")
                        continue
                except:
                    print(Fore.RED + "Invalid input. Try again.")
                    continue
            else:
                print(Fore.GREEN + "AI is thinking...")
                move = get_best_move(board)

            board[move] = current_player

            if is_winner(board, current_player):
                print_board(board)
                if current_player == "X":
                    print(Fore.GREEN + "🎉 You win!")
                    user_score += 1
                else:
                    print(Fore.RED + "💻 AI wins!")
                    ai_score += 1
                break
            elif " " not in board:
                print_board(board)
                print(Fore.BLUE + "🤝 It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        print(Fore.MAGENTA + f"\n🧮 Score: You {user_score} - {ai_score} AI")
        play_again = input(Fore.CYAN + "\nDo you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            print(Fore.YELLOW + "👋 Thanks for playing! Bye.")
            break

if __name__ == "__main__":
    main()
