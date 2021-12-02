__supported_types = ["integer", "double", "string"]


def read_file(file_name, *types):
    for type in types:
        if type not in __supported_types:
            print(f"** Error: unsupported data type {type}.")
            exit(-1)

    try:
        file = open(file_name, "r")
    except:
        print(f"** Error: input file f{file_name} doesn't exit.")
        exit(-1)

    data = []
