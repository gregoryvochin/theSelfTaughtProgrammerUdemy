def bottles_of_beer(bob):
    if bob < 1:
        print("No more bottles of beer on the wall. No more bottles of beer.")

        return

    tmp = bob

    bob -= 1

    print(f"{tmp} bottles of beer on the wall, {tmp} bottles of beer! Take one down, "
          f"pass it around, {bob} bottles of beer on the wall!")

    bottles_of_beer(bob)


bottles_of_beer(10)
