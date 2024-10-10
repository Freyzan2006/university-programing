def reverse_words(text: str) -> str:
    text_split = text.split()
    
    words = [word[::-1] if len(word) >= 5 else word for word in text_split]
    result = " ".join(words)
    
    return result

def main() -> None:
    inp = "Hey fellow warriors"
    print(inp, "-->", reverse_words(inp)) 



# print("---------task 1--------------")
# inp = "Hey fellow warriors"
# print(inp, "-->", reverse_words(inp)) 