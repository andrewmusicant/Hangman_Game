def game_display():
    print("   |-------|    \n",
          "   |       |    \n",
          "           |    \n",
          "           |    \n",
          "           |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def one_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "           |    \n",
          "           |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def two_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "   |       |    \n",
          "           |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def three_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "  /|       |    \n",
          "           |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def four_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "  /|\      |    \n",
          "           |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def five_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "  /|\      |    \n",
          "    \      |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def six_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "  /|\      |    \n",
          "  / \      |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def seven_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "  /|\      |    \n",
          " </ \      |    \n",
          "           |    \n",
          "       ____|____\n",sep="")

def eight_wrong():
    print("   |-------|    \n",
          "   |       |    \n",
          "   0       |    \n",
          "  /|\      |    \n",
          " </ \>     |    \n",
          "           |    \n",
          "       ____|____\n",sep="")
    print("you lost")
    exit()


def win():
    print("""    |-------|
    |       |
            |
            |
  \ 0 /     |
    |       |
  </ \>  ___|___ """)
    print("You Win")
