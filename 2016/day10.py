from pathlib import Path

data = (
    (Path(__file__).parent / (Path(__file__).stem + ".in"))
    .read_text()
    .strip("\n")
    .split("\n")
)

compare = dict()  # compare rules for each bot
bot2 = dict()  # bots with two chips [low ,high]
bot1 = dict()  # bots with one chips
output = dict()  # output bins

for line in data:
    if line[:5] == "value":
        v, b = line[5:].split("goes to bot")
        v = int(v)
        b = int(b)

        if b in bot2:
            raise Exception
        elif b in bot1:
            bot2[b] = sorted([v, bot1.pop(b)])
        else:
            bot1[b] = v
    else:
        b, line = line[3:].split("gives low to")
        low, high = line.split("and high to")

        dl, nl = low.strip().split()
        dh, nh = high.strip().split()

        compare[int(b)] = ((dl[0], int(nl)), (dh[0], int(nh)))


def add_output(dst, chip):
    if dst not in output:
        output[dst] = [chip]
    else:
        output[dst].append(chip)


def add_bot(dst, chip):
    if dst in bot2:
        raise Exception
    elif dst in bot1:
        bot2[dst] = sorted([chip, bot1.pop(dst)])
    else:
        bot1[dst] = chip


while bot2:
    b, c = list(bot2.items())[0]
    del bot2[b]

    if c[0] == 17 and c[1] == 61:
        print(f"bot {b} is comparing 17 and 61")

    if compare[b][0][0] == "o":
        add_output(compare[b][0][1], c[0])
    else:
        add_bot(compare[b][0][1], c[0])

    if compare[b][1][0] == "o":
        add_output(compare[b][1][1], c[1])
    else:
        add_bot(compare[b][1][1], c[1])

value = 1
for i in output[0] + output[1] + output[2]:
    value *= i

print(value)
