#Word Counter
str = 'Open your eyes in sea water and it is difficult to see much more than a murky, bleary green colour. Sounds, too, are garbled and difficult to comprehend. Without specialised equipment humans would be lost in these deep sea habitats, so how do fish make it seem so easy? Much of this is due to a biological phenomenon known as electroreception – the ability to perceive and act upon electrical stimuli as part of the overall senses. This ability is only found in aquatic or amphibious species because water is an efficient conductor of electricity.'
word_count = 0
for letter in str:
    if letter == ' ':
        word_count = word_count + 1
print("No. of words: ",word_count+1)