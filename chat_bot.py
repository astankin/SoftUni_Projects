from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is(.*)",
        ["Hello %2, how are you today ?", ]
    ],
    [
        r"(.*)help(.*)",
        ["What  can I help you ?", ]
    ],
    [
        r"(.*)are you ?",
        ["I am doing well", "I am not too bad !"]
    ],
    [
        r"(.*)(hi|hey|hello)(.*)",
        ["Hello", "Hi there"]
    ],
    [
        r"(.*)created(.*)",
        ["Atanas Stankin created me using Python"]
    ],

    [
        r"(.*)your name?",
        ["My name is Robot and I am a chatbot."]
    ],

    [
        r"(.*)(bye|chao|exit)(.*)",
        ["Bye for now. See you soon :)", "It was nice talking to you . See you soon :)"]
    ]

]
print("Hi, I am chat bot and I am here to help you .")
chat = Chat(pairs, reflections)
chat.converse()