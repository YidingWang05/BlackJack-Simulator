# Developing logbook

### 02/08/2025
Set up the function to prepare cards for the game. 

new tasks: 

- [ ] should introduce a new variable to keep track of the total buy-in of the players to track the long term profit (Optional)
- [x] enable the function that allows players buy-in chips in the middle of a game.

### 03/08/2025
Finished the basic game. Now it can play with minimum option (`buy-in`, `hit` and `stand`). 

next stage:
Finish `Advanced rules` add `blackjack check` to check if player or dealer has `blackjack` and pay out accordingly

### 04/08/2025
Finished the `multi-hand` function. Got prepared for `split`. Too many loops used--potentially to be improved.

Note:
A difficulty is `bust` check. For `multi-hand` game, if all player's hand bust, dealer will skip drawing cards for them. Also, once a player bust, this hand will be instantly lose.

An idea is that directly `pop()` the busted hand, when the `player` list is empty, we skip drawing cards for dealer. 
pro: easy algo, less complexity, reduce the number of loops used.
con: might be confusing for real user.


