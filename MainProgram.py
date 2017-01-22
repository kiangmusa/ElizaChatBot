__author__ = 'Eliza & Angky'

import re
import os
from pip._vendor.distlib.compat import raw_input

os.system('cls')
words = ''
while words != "/endchat":
    words = raw_input("You : ")

    # Matching words
    match1 = re.search(r'feel+.(so \w+|\w+)+.[\w\s]+.because+.([\w\s]+)',words)
    match2 = re.search(r'feel+.(so \w+|\w+)',words)
    match3 = re.search(r'([S|s]he|[H|h]e)+.always+.(\w+)',words)
    match4 = re.search(r'I\'m (depressed|sad|guilty|bored|annoyed|angry)',words)
    match5 = re.search(r'[l|L]ike',words)
    match6 = re.search(r'[\w\s\W]+.want to tell something',words)
    match7 = re.search(r'I\'m+.(so \w+|\w^a+)',words)
    match8 = re.search(r'[m|M]y (boy|girl)friend',words)
    match9 = re.search(r'[m|M]y ex (girlfriend|boyfriend)',words)
    match10 = re.search(r'I don\'t understand',words)
    match11 = re.search(r'another+.(girl|boy|man|woman)',words)
    match12 = re.search(r'fight',words)
    match13 = re.search(r'([S|s]he|[h|H]e)+.angry',words)
    match14 = re.search(r'([T|t]hank you)',words)
    match15 = re.search(r'without any reason',words)
    match16 = re.search(r'[h|H]ow?',words)
    match17 = re.search(r'I love (him|her)',words)
    match18 = re.search(r'beautiful',words)
    match19 = re.search(r'don\'t want to hurt+.(him|her)',words)
    match20 = re.search(r'\W',words)


    if words == "/endchat":
        print("ElizaBot : Byee!")
    elif match1:
        print("ElizaBot : Why "+match1.groups()[1]+" ?")
    elif match2:
        print("ElizaBot : Why? If you don't mind you can tell me why are you feeling "+match2.groups()[0])
    elif match3:
        if match3.groups()[1] == "asking":
            print("ElizaBot : That mean "+(match3.groups()[0]).lower()+" cares about you")
        else:
            print("ElizaBot : Can you think of a specific example?")
    elif match4:
        print("ElizaBot : I'm sorry to hear that you are "+match4.groups()[0]+". You can tell me why you are "++match4.groups()[0]+" I feel free to hear that")
    elif match5:
        print("ElizaBot : Really?")
    elif match6:
        print("ElizaBot : Ok! I will hear you")
    elif match7:
        print("ElizaBot : Why are you "+match7.groups()[0]+"?")
    elif match8:
        print("ElizaBot : So you are a "+match8.groups()[0]+"?")
    elif match9:
        print("ElizaBot : You still love your ex "+match9.groups()[0]+"?")
    elif match10:
        print("ElizaBot : You can ask Google if you don't understand")
    elif match11 or match12:
        print("ElizaBot : I'm sorry to hear that")
    elif match13:
        print("ElizaBot : Why "+match13.groups()+" angry with you?")
    elif match14:
        print("ElizaBot : You don't need to say "+match14.groups()[0].lower()+". I know everybody needs me. I'm so useful")
    elif match15:
        print("ElizaBot : There is a reason, you have to find it")
    elif match16:
        print("ElizaBot : Don't ask me, i don't even have an experience about it. I'm just a bot. A smart bot")
    elif match17:
        print("ElizaBot : May I know what makes you love "+match17.groups()[0]+"?")
    elif match18:
        print("ElizaBot : Wow beautiful! Kinda like love, hurt but beautiful. Oops sorry I have to tell it to you")
    elif match19:
        print("ElizaBot : See you don't want to hurt "+match19.groups()[0]+". Woah i saw a pair of wings behind your back there. You are such an angel!")
    elif match20:
        print("ElizaBot : I know right. Sometimes I'm just being a silly. LOL")
    else:
        print("ElizaBot : You are a problem")