def main():
        dalva=convert(input())
        print(dalva)
def convert(text):
        text= text.replace(":)"," 🙂").replace(":(","🙁")
        return text
main()
    
        