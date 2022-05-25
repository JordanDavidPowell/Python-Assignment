if __name__ == '__main__':

    print("Stop! Who would cross the Bridge of Death, Must answer me these questions three,"
          "'ere the other side he see.")
    name = input("Hello. Who are you? ").lower()
    if "arthur" in name:
        print("My liege! You may pass")
    else:
        grail = input("What do you seek?")
        if "grail" or "GRAIL" or "Grail" in grail:
            colour = input("What is your favourite colour?").lower()
            if colour.lower().startswith(name[0]):
                print("Okay you may pass.")
            else:
                print("Incorrect! You must now face the Forge of Eternal Peril. ")
        else:
            print("Only those who seek the Grail may pass.")



