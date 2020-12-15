# The Van Eck sequence!
# https://www.youtube.com/watch?v=etMJxB-igrc
if __name__ == "__main__":
    target = 2020
    numbers = "2,20,0,4,1,17"
    numbers = [int(n) for n in numbers.split(",")]
    last_spoken = numbers[-1]
    spoken_numbers = {n: i + 1 for i, n in enumerate(numbers[:-1])}
    for prev_turn in range(len(numbers), target):
        new_spoken = prev_turn - spoken_numbers.get(last_spoken, prev_turn)
        spoken_numbers[last_spoken] = prev_turn
        last_spoken = new_spoken
    print(last_spoken)
