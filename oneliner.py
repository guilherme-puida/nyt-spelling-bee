print(
    "\n".join(
        [
            w
            for w in map(
                lambda x: x.upper(), open("words.txt").read().strip().splitlines()
            )
            if (
                len(w) > 3
                and "O" in w
                and all(True if x in "UPAMRDO" else False for x in w)
            )
        ]
    )
)
