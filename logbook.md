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

