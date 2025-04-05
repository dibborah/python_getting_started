# Emoji converter

emoji_mappings = {
    ':)': '😀',
    ':(': '😔'
}

words = input('>').split(' ')

output = ''
for word in words:
    output += emoji_mappings.get(word, word) + ' '
print(output)
