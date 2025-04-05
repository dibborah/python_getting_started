# creating reusable functions

# Emoji converter

def emoji_converter(message):
    words = message.split(' ')
    emoji_mappings = {
    ':)': '😀',
    ':(': '😔'
    }

    output = ''
    for word in words:
        output += emoji_mappings.get(word, word) + ' '
    return output


message = input('>')
print(emoji_converter(message))
