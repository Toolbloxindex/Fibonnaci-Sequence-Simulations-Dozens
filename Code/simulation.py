import random

def spin_roulette():
    """Simulate a spin of a European roulette wheel."""
    return random.choice(range(37))  # 37 slots (0 to 36)

def fibonacci_bet(starting_bet, max_bet, spins, dozen_choice=1):
    """Simulate the Fibonacci betting system applied to dozens on European Roulette."""
    fib_sequence = [starting_bet, starting_bet * 2]  # Initialize Fibonacci sequence
    balance = 0
    fib_index = 0
    history = []

    for spin in range(spins):
        # Cap the bet at 75.40
        bet = min(fib_sequence[fib_index], 75.40)  

        result = spin_roulette()
        win = result in range((dozen_choice - 1) * 12 + 1, dozen_choice * 12 + 1)

        if win:
            balance += bet * 2
            fib_index = 0  # Reset to the start of the Fibonacci sequence
        else:
            balance -= bet
            fib_index += 1

            # Reset to a new game at starting bet (0.20) if the bet reaches 75.40 and it's a loss
            if bet == 75.40:
                fib_sequence = [starting_bet, starting_bet * 2]
                fib_index = 0
            else:
                # Otherwise, extend the Fibonacci sequence
                if len(fib_sequence) <= fib_index:
                    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

        history.append((spin + 1, bet, result, win, balance))

    return history, balance

def run_simulation(num_simulations=1, spins=1000):
    """Run simulation for specified number of spins."""
    starting_bet = 0.20
    max_bet = 108
    dozen_choice = 1  # Betting on the 1st dozen (1-12)

    final_balances = []

    for sim_num in range(num_simulations):
        print(f"\nSimulation {sim_num + 1}:")
        history, final_balance = fibonacci_bet(starting_bet, max_bet, spins, dozen_choice)
        final_balances.append(final_balance)

        for spin, bet, result, win, balance in history:
            print(f"Spin {spin}: Bet = €{bet:.2f}, Result = {result}, Win = {win}, Balance = €{balance:.2f}")

        print(f"Final balance for Simulation {sim_num + 1}: €{final_balance:.2f}")

    # Analysis only if more than one simulation
    if num_simulations > 1:
        average_balance = sum(final_balances) / num_simulations
        min_balance = min(final_balances)
        max_balance = max(final_balances)
        print(f"\nAfter {num_simulations} simulation(s):")
        print(f"Average final balance: €{average_balance:.2f}")
        print(f"Minimum final balance: €{min_balance:.2f}")
        print(f"Maximum final balance: €{max_balance:.2f}")

    return final_balances

# Run 1 simulation for 1000 spins
final_balances = run_simulation(num_simulations=100, spins=1000)
