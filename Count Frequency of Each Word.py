text = "apple banana apple orange apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
