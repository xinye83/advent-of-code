__supported_types = ["integer", "double", "string"]


def read_table(file_name, *types):
    for type in types:
        if type not in __supported_types:
            print(f"** Error: unsupported data type {type}.")
            exit(-1)

    try:
        file = open(file_name, "r")
    except:
        print(f"** Error: input file f{file_name} doesn't exit.")
        exit(-1)

    temp = [line.split() for line in file]
    data = [list(column) for column in zip(*temp)]

    for i, type in enumerate(types):
        if type == "integer":
            data[i] = list(map(int, data[i]))
        elif type == "double":
            data[i] = list(map(float, data[i]))

    return data


# read paragraphs separated by an empty line
def read_paragraph(file_name):
    try:
        file = open(file_name, "r")
    except:
        print(f"** Error: input file f{file_name} doesn't exit.")
        exit(-1)

    return file.read().split("\n\n")
