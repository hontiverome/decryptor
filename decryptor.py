# ACTIVITY NO2 PSEUDO CODE WITH GIT COMMITS
# Ask for input:
StrInput=str(input("What is your string?\n:"))
StrOutput=""
# Check each of the letters input using loop
for i in range(len(StrInput)):
    # If letter is *, change to a
    if StrInput[i] == "*":
        StrOutput += "a"
# If letter is &, change to e
    if StrInput[i] == "&":
        StrOutput += "e"
# If letter is #, change to i
    if StrInput[i] == "#":
        StrOutput += "i"
# If letter is +, change to o
    if StrInput[i] == "+":
        StrOutput += "o"
# If letter is !, change to u
    if StrInput[i] == "!":
        StrOutput += "u"
# End loop
# Execute the code
print(StrOutput)

# String to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
# expected text: the quick brown fox jumps over the lazy dog.