import random

def generate_powerball_numbers():
    white_balls = [str(random.randint(1, 69)) for _ in range(5)]
    red_ball = str(random.randint(1, 26))
    
    return ' '.join(white_balls) + '    ' + red_ball

def main():
    print("Welcome to the Powerball number generator!")
    answer = input("Would you like some Powerball numbers? (yes/no): ")
    
    if answer.lower() == "yes":
        numbers = generate_powerball_numbers()
        print("Here are your numbers:")
        print(numbers)
    else:
        print("Alright, maybe next time. Goodbye!")

if __name__ == "__main__":
    main()