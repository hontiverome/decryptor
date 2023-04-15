import pyfiglet, termcolor, time
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
def ShowResults():
    showResults="Here is the decrypted text from your input:\n"
    for i in range(len(showResults)):
        print(termcolor.colored(showResults[i], 'green'), end='', flush=True)
        time.sleep(0.1)
def CypherPlainText(): 
    Seperate= ' '.join(StrOutput)
    # Font using pyfiglet, whilst giving it color using termcolor
    print(termcolor.colored(pyfiglet.figlet_format(StrOutput, font="smkeyboard", justify="center"), 'red'))
    print("or:\n")
    # Same code as show result to show complete text in a readable manner
    # Made use of 'join' function to add spaces between each text
    for i in range(len(Seperate)):
        print(termcolor.colored(f"{Seperate[i]}", 'red'), end='', flush=True)
        time.sleep(0.05)


# Execute the code
StrOutput=DecryptorCode()
ShowResults()
CypherPlainText()


# String to decrypt: th& q!#ck br+wn f+x j!mps +v&r th& l*zy d+g.
# expected text: the quick brown fox jumps over the lazy dog.

# HONTIVEROS JEROME ANDREI O.
# BSCPE1-5