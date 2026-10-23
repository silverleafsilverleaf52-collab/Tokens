#this is how Ai splits text into tokens

text = input("You: \n")
#spliting
tokens = text.split()

for i, token in enumerate(tokens):
    print(f"{i + 1}: {token}")
