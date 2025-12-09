from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")

beam = set([data[0].index("S")])
timeline = {i: 0 for i in range(len(data[0]))}
timeline[data[0].index("S")] = 1
count = 0

for line in data[2::2]:
    i = 0
    beam_new = set()

    while i < len(line):
        try:
            j = line.index("^", i)
        except:
            break
        i = j + 1

        if j in beam:
            count += 1
            beam.remove(j)
            beam_new.add(j - 1)
            beam_new.add(j + 1)

            timeline[j - 1] += timeline[j]
            timeline[j + 1] += timeline[j]
            timeline[j] = 0

    beam.update(beam_new)

print(count)
print(sum([value for _, value in timeline.items()]))
