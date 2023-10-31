def main():
    time = input("What time is it? ")
    hours, minutes = time.split(":")
    convert(minutes, hours)


def convert(minutes, hours):
    converted = float((int(minutes) / 60) + int(hours))
    res = round(converted, 1)
    if 7 <= res <= 8:
        print("breakfast time!")
    elif 12 <= res <= 13:
        print("lunch time!")
    elif 18 <= res <= 19:
        print("dinner time!")
    else:
        pass


if __name__== "__main__":
    main()