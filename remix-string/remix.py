"""
you get a string and get where the string needs to go to

there may be multiple permutations of the string,
you must use the result of the last one to generate the new one

there is also a special output requirement, it should be pretty self-explanatory
"""

_, remixes, special_prints = [int(v) for v in input().split()]

string = input()
remixed_strings = []

for i in range(remixes):
    remix = sorted([(int(pos), string[i]) for i, pos in enumerate(input().split())])
    remixed_strings.append("".join(c[1] for c in remix))
    string = remixed_strings[i]

for i in range(special_prints):
    print("".join(s[i] for s in remixed_strings))