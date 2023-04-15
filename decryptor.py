import termcolor, time
# ACTIVITY NO2 PSEUDO CODE WITH GIT COMMITS
def DecryptorCode():
    # Ask for input:
    StrInput=str(input("What is your string?\n:"))
    StrOutput=""
    # Check each of the letters input using loop
    for i in range(len(StrInput)):
        # If letter is *, change to a
        if StrInput[i] == "*":
            StrOutput += "a"
        # If letter is &, change to e
        elif StrInput[i] == "&":
            StrOutput += "e"
        # If letter is #, change to i
        elif StrInput[i] == "#":
            StrOutput += "i"
        # If letter is +, change to o
        elif StrInput[i] == "+":
            StrOutput += "o"
        # If letter is !, change to u
        elif StrInput[i] == "!":
            StrOutput += "u"
        # End loop, by compiling all letters
        else:
            StrOutput+= StrInput[i]
    return StrOutput

# Design Purposes>
result="test"
for i in range(len(result)):
    print(termcolor.colored(result[i], 'green'), end='', flush=True)
    time.sleep(0.1)
exit()
# Execute the code
StrOutput=DecryptorCode()
print(StrOutput)


# String to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
# expected text: the quick brown fox jumps over the lazy dog.

# HONTIVEROS JEROME ANDREI O.
# BSCPE1-5