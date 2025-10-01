# Developing logbook

### 02/08/2025
Set up the function to prepare cards for the game. 

new tasks: 

- [ ] should introduce a new variable to keep track of the total buy-in of the players to track the long term profit (Optional)
- [x] enable the function that allows players buy-in chips in the middle of a game.

### 03/08/2025
Finished the basic game. Now it can play with minimum option (`buy-in`, `hit` and `stand`). 

next stage:
- Finish `Advanced rules` add `blackjack check` to check if player or dealer has `blackjack` and pay out accordingly

### 04/08/2025
- Finished the `multi-hand` function. Got prepared for `split`. Too many loops used--potentially to be improved.
- Finished the `last card`. This mimic the real situation, dealer will shuffle the cards again when there are too less card left in the shoe.
    - In the real casino, the last card is marked by a coloured card that inserted in to the decks. This "marker" will be inserted by human dealer and therefore, it's impossible to ensure the same position each time. To simulate this, in this project, I use a random number to choose a position near the end of the decks. 

Note:
- A difficulty is `bust` check. For `multi-hand` game, if all player's hand bust, dealer will skip drawing cards for them. Also, once a player bust, this hand will be instantly lose.

- An idea is that directly `pop()` the busted hand, when the `player` list is empty, we skip drawing cards for dealer. 
  - pro: easy algo, less complexity, reduce the number of loops used.
  - con: might be confusing for real user.

### 05/08/2025
- Finished the `double down`. Past the test for it
- Finished the `bust` check. Final decision was use the idea above

Problem: 
- Optimize `double down`: Currently, if user don't want to double down, they have to press the key for other action twice. e.g. press `h` twice for `hit`. The possible solution to solve this has been attached in the `game.py`

### 06/08/2025
- Improved `double down`, player can directly choose from `double` `hit` or `stand`
- Improved the approach for storing hands' info
   - following structure used: 
     `player_hands = [{"cards": [], "point": int, "hand_id": int, "split_id": int, "bet": double, "side_bets": [], }....]`
      - By this new structure, the readability of the codes can be improved. The following developing would be much easier. Furthermore, this enable a steady id for each hand to avoid confusing for real player.

### 07/08/2025
- Finished `split`, now the user can split their hand when they have pairs or two tens

- Note: 
  - Improve UI before any further work done. The UI now is in bad logic and layout, the instruction is unclear which even make testing difficult. (It should be done much earlier, now I couldn't even understand my own UI `:(`)

### 08/08/2025
- Partially optimize UI, the UI now is easier for testing, but further improvement required.
- Note:
    Work delayed-Help my classmate prepare resite--(I'm a good man, i enjoy helping others, so....sorry my project). Expected resume date: 15/08/2025

### 12/08/2025
- Fixed bugs of the control of `split` and `double`
- Fixed the bugs of `count_points()`

### 13/08/2025
- Further improvement of `split`

### 28/08/2025
- DELAYED! Due to a friend visiting.
- Improved the UI for better clarity. 
- Finalized the `game` part. Start the research for strategies
- Spent some time in the real casinos across the UK over the last week, found that the most popular rules:
    - 6 decks in play with auto shuffle machine
    - Dealer stays on soft 17
    - No insurance bets
    - Split Ace one card only 
    - No `blackjack` after splitting
- Therefore, proper adjustments to the plans of this projects need to be done to match the real world situation.

### 15/09/2025
- DELAYED! Due to holiday--Give myself a bit of time to relax before new term. 
- Finished "No `blackjack` after splitting"
- Adjusted the logic of `blackjack` checking
- Finished `Split Ace one card only`