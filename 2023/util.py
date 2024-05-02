from pathlib import Path
import inspect


def get_input(example=False):
    caller = Path(inspect.stack()[1].filename)

    if not example:
        file = caller.parent / (caller.stem + ".in")
    else:
        file = caller.parent / (caller.stem + "_ex.in")

    if not file.is_file():
        raise Exception("input file doesn't exist")

    return file.read_text().rstrip("\n")
