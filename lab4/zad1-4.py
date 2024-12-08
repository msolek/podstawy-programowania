
def litery():
    zdanie = input("podaj zdanie: ").lower()
    albafet = set("abcdefghijklmnopqrstuvwxyz")
    
    litery_w_naszym_zdaniu = sorted(set(zdanie) & set(albafet))
    
    print(f"litery w zdaniu: {litery_w_naszym_zdaniu}")
    
    brakujace_litery = set(albafet) - set(litery_w_naszym_zdaniu)
    print(f"brakujace litery: {brakujace_litery}")

litery()