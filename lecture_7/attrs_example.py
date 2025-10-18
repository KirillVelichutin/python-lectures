from attr import define

@define
class Smth:
    c: str
    a: int = 2
    b: int = 3

    
if __name__ == "__main__":
    s = Smth(c="ab")
    print(s)