# 24. Count vowels
text = "hello world"
vowels = "aeiou"
count = sum(1 for ch in text if ch.lower() in vowels)
print("Vowels:", count)