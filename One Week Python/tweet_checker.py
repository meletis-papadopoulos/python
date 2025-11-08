tweet = input("Enter your tweet: ")
char_count = len(tweet)

max_chars = 140
overhead = char_count - max_chars

if len(tweet) < max_chars:
    print(f"That {char_count} char tweet will work!")
else:
    overhead = char_count - max_chars
    print(f"Your {char_count} tweet is {overhead} chars too long")