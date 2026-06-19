import itertools

def main ():
    letters = ["b", "o", "b", "a"]
    perms = set(itertools.permutations(letters))
    print ((len(perms)))

main ()