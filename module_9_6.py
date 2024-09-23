def all_variants(text):
    for j in range(len(text)):
        j += 1
        for start in range(len(text)):
            stop = j + start
            if stop >= (len(text) + 1):
                continue
            yield text[start:stop]


a = all_variants("abc")
for i in a:
    print(i)
