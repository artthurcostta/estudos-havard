def main():
    akarasta = input("What time is it")
    time = convert(akarasta)
    if time >=7 and time<=8:
        print("breakfast time")
    elif time >=12 and time <=13:
        print("lunch time")
    elif time >=18 and time <=19:
        print("dinner time")
    else:
        print("safado")

def convert(time):
    horas, minutos = time.split(":")
    minutos = float(minutos) / 60
    return float(horas) + minutos


if __name__ == "__main__":
    main()