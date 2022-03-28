CENTER = "O"  # The letter in the center - The one in yellow
LETTERS = "UPAMRD" + CENTER  # The rest of the letters - The ones in gray

with open("words.txt") as f:  # words.txt comes from /usr/share/dict/words
    words = f.read().strip().splitlines()
    words = map(lambda x: x.upper(), words)

for w in words:
    if len(w) > 3 and CENTER in w and all(True if x in LETTERS else False for x in w):
        print(w)
