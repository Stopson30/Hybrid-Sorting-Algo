import random
import numpy as np

# Define the card values for the Hi-Lo count
card_values = {'2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 0, '8': 0, '9': 0, '10': -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}

# Define the rules of the game
num_decks = 6
dealer_hits_soft_17 = False
surrender_allowed = False

# Define the lifetime performance parameters
num_players = 3
hands_per_hour_per_player = 100
hours_per_day = 8
days_per_year = 200

# Define the simulation parameters
num_simulations = 10000
num_hands_per_simulation = num_players * hands_per_hour_per_player * hours_per_day * days_per_year

# Simulate the blackjack hands and calculate the team's lifetime performance for each simulation
lifetimes = []
for i in range(num_simulations):
    deck = list(card_values.keys()) * 4 * num_decks
    random.shuffle(deck)
    running_count = 0
    num_hands_won = 0
    num_hands_lost = 0
    num_hands_pushed = 0
    for j in range(num_hands_per_simulation):
        if running_count >= 2:
            bet = 2
        elif running_count == 1:
            bet = 1
        else:
            bet = 0
        player_hands = []
        for k in range(num_players):
            player_hand = [deck.pop(), deck.pop()]
            player_hands.append(player_hand)
        dealer_hand = [deck.pop(), deck.pop()]
        dealer_upcard = dealer_hand[0]
        for player_hand in player_hands:
            hand_value = sum([card_values[card] for card in player_hand])
            if hand_value == -2:
                hand_value = 12
            while hand_value <= 11:
                player_hand.append(deck.pop())
                hand_value = sum([card_values[card] for card in player_hand])
            while hand_value >= 12 and hand_value <= 16 and dealer_upcard in ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                player_hand.append(deck.pop())
                hand_value = sum([card_values[card] for card in player_hand])
            if hand_value > 21:
                num_hands_lost += 1
            else:
                while True:
                    dealer_value = sum([card_values[card] for card in dealer_hand])
                    if dealer_hits_soft_17 and dealer_value == 17 and 'A' in dealer_hand:
                        dealer_value -= 10
                    if dealer_value >= 17:
                        break
                    dealer_hand.append(deck.pop())
                if dealer_value > 21:
                    num_hands_won += 1
                elif dealer_value < hand_value:
                    num_hands_won += 1
                elif dealer_value > hand_value:
                    num_hands_lost += 1
                else:
                    num_hands_pushed += 1
        running_count += sum([card_values[card] for card in dealer_hand])
        running_count += sum([card_values[card] for hand in player_hands for card in hand])
    lifetime = num_hands_won - num_hands_lost
    lifetimes.append(lifetime)

# Calculate the mean and
# Calculate the mean and standard deviation of the team's lifetime performance
mean_lifetime = np.mean(lifetimes)
std_lifetime = np.std(lifetimes)

# Calculate the probability of the team having a positive lifetime performance
p_positive_lifetime = sum([1 for lifetime in lifetimes if lifetime > 0]) / num_simulations

# Calculate the probability of the team having a lifetime performance greater than a certain threshold
threshold = 5000
p_lifetime_above_threshold = sum([1 for lifetime in lifetimes if lifetime > threshold]) / num_simulations

# Print the results
print(f"Mean lifetime performance: {mean_lifetime:.2f}")
print(f"Standard deviation of lifetime performance: {std_lifetime:.2f}")
print(f"Probability of positive lifetime performance: {p_positive_lifetime:.2f}")
print(f"Probability of lifetime performance above {threshold}: {p_lifetime_above_threshold:.2f}")
