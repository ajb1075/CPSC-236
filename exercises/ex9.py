from random import randrange

def generate_question() -> (int, int, int):
    n1, n2 = sorted((randrange(1, 10), randrange(1, 10)), reverse=True)
    return (n1, n2, n1-n2)

if __name__ == '__main__':
    correct = 0
    num_questions = 3
    for _ in range(0, num_questions):
        question = generate_question()
        answer = int(input(f"{question[0]} - {question[1]} = "))
        correct += 1 if answer == question[2] else 0

    print(f"\nYou have gotten {correct}/{num_questions} correct!")
