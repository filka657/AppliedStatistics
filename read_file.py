def read_file(data):
    with open("1.txt") as f:
        for line in f:
            data.append(int(line.replace('\n', '')))
    return data
