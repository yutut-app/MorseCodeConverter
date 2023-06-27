# Morse Code変換用の辞書を定義します。
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.'
}

def convert_to_morse(input_str):
    """
    文字列をMorse Codeに変換する関数
    input_str: Morse Codeに変換したい文字列
    """

    # 結果を格納する空の文字列を作成します。
    morse_code = ''

    # 入力された文字列の各文字に対して、以下の操作を行います。
    for char in input_str:
        # 文字がアルファベットか数字かを確認します。
        if char.isalnum():
            # Morse Code変換用の辞書を用いて変換を行い、結果を追加します。
            # 大文字小文字を区別しないため、.upper()を使用します。
            morse_code += morse_code_dict[char.upper()] + ' '
        elif char == ' ':  # スペースがあれば、Morse Codeではスペースを '/ 'で表現します。
            morse_code += '/ '
    
    # 生成されたMorse Codeを返します。
    return morse_code

# ユーザーからの入力を受け取る部分です。
user_input = input("Enter a string to convert to Morse Code: ")

# Morse Codeに変換して出力します。
print(convert_to_morse(user_input))
