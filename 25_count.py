# 25. Count consonants
count = sum(1 for ch in text if ch.isalpha() and ch.lower() not in vowels)
print("Consonants:", count)