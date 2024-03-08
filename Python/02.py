def fibonacci(number):
    fibonacci_sequence = [0, 1]
    while fibonacci_sequence[-1] < number:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence

def verify_fibonacci(sequence, number):
    if number in sequence:
        print(f'O número {number} pertence a sequência de fibonacci.')
    else: 
        print(f'O número {number} não pertence a sequência de fibonacci.')

if __name__ == "__main__":
    chosen_number = int(input("Digite um número: "))
    sequence = fibonacci(chosen_number)
    verify_fibonacci(sequence, chosen_number)