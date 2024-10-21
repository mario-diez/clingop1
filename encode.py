def find_trees():
    with open("example1.txt", 'r') as file:
        lines = file.readlines()

    positions = []
    dim = len(lines[0].strip())
    
    for row, line in enumerate(lines[:-2]):
        for col, char in enumerate(line.strip()):
            if char == 't':
                positions.append((row, col))

    return positions, dim


def write_file_encoded():
    trees,dim = find_trees()
    with open("domain.lp", 'w') as file:
        file.write(f"rows({dim}).\n")
        for row, col in trees:
            file.write(f"tree({row}, {col}).\n")

def main():
    write_file_encoded()

if __name__ == "__main__":
    main()    