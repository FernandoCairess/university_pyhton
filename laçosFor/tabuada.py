#desafio1: criar uma tabuada usando o laço for de 1 até 25
for i in range(1,25+1):
    print("-------------------------")
    print(f"tabuada do {i}")
    print("-------------------------")
    for t in range(1,25+1):
        tabuada=i*t
        print(f"{i}x{t}={tabuada:<20}", end="  ")
    print()
