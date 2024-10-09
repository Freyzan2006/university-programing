def reverse_words(text: str) -> str:
    text_split = text.split(" ")
    
    result = ""
    for word in text_split:
        result += word[::-1] + " "
    
    return result

def show_result() -> None:
    print("---------task 1--------------")
    inp = "Hey fellow warriors"
    print(inp, "-->", reverse_words(inp)) 
