# Spelling bee solver

Just a quick little python script to get words that solve the daily spelling bee game from New York Times.

The word list comes from `/usr/share/dict/words` (`words` package in Arch). This list is probably incomplete, since it does not contain all the words necessary to get a perfect score, but it is usually sufficient to at least get to the final tier (genius).

Do note that the words list contains tons of words that are not valid inside the Spelling Bee, so the solution list will also contain invalid words. I just try all of them and see which works, but there is probably a better way to do that.

`oneliner.py` shows how the solution could be computed in one single expression, just for fun.

## How to use

Change the two first variables in `main.py` (`CENTER` and `LETTERS`) to the letters in the game.
