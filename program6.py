def vacuum(world, pos):
    for i, state in enumerate(world):
        if state == "Dirty":
            print(f"Location {i+1} is Dirty. Cleaning...")
            world[i] = "Clean"
        else:
            print(f"Location {i+1} is already Clean.")
    print("All locations are clean:", world)

world = ["Dirty", "Clean"]
vacuum(world, 0)
