import random

def randomPassword(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    length = int(input("¬ведите длину парол€: "))
    password = randomPassword(length)
    print("—генерированный пароль:", password)

if __name__ == "__main__":
    main()