def hanoi(height, from_pole, to_pole, with_pole):
    if height >= 1:
        hanoi(height - 1, from_pole, with_pole, to_pole)
        print("Move disk from", from_pole, " to ", to_pole)
        hanoi(height - 1, with_pole, to_pole, from_pole)

hanoi(3, 'A', 'B', 'C')
