s = input()
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in sorted(freq):
    print(f"{ch} : {freq[ch]}")