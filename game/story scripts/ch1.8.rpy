label ch1_s8:
    scene tavern
    show zygmunt at farright
    show bogdan at rightish
    show andia at leftish
    show dobrava at farleft
    with fade

    "Back in the tavern, my companions book rooms for the night. We decide not to talk about today's events until morning and instead take time to recuperate."
    z "We tend to spend the evenings separately, Dobrava, as each of us relaxes better doing different things."
    a "You are welcome to do whatever you want or join one of us."
    d "What's everyone going to do?"
    a "I'll be in my room painting."
    b "I'm going outside to train."
    z "And I will be in the tavern playing cards."
    "Who do I want to spend the evening with?"
menu:
    "With Andia watching her paint":
        $ andia += 5
        $ ch8_buddy = "andia"
        jump ch1_s8_andia
    "With Bogdan watching him train":
        $ bogdan += 5
        $ ch8_buddy = "bogdan"
        jump ch1_s8_bogdan
    "With Zygmunt playing cards":
        $ zygmunt += 5
        $ ch8_buddy = "zygmunt"
        jump ch1_s8_zygmunt
    "Alone working as a bard":
        jump ch1_s8_alone

label ch1_s8_andia:
    $ dmood = 'happy'
    d "I'd like to watch you paint, if that's not a problem, Andia?"
    $ amood = 'happy'
    a "Not at all. I'm happy you want to spend time with me. Let's go upstairs then."
    "We leave the guys and go up to Andia's room."

    scene inn room
    show dobrava at right
    show andia at left
    with fade

    "Andia's room is very similar to mine. I suppose all the tavern guestrooms are the same."
    "Andia takes out some sheets of paper and painting supplies from her satchel by the bed."
    $ dmood = 'happy'
    d "What are you going to paint?"
    $ amood = 'neutral'
    a "Hmm..."
    "She looks at me for a moment, thinking."
    $ amood = 'shy'
    a "How about you? Would you mind?"
    $ dmood = 'surprised'
    "That's a new expression I've never seen before on her. She's... blushing?"
menu:
    "Agree to Andia's request":
        jump ch1_s8_andia1
    "Say you're not comfortable with being painted":
        jump ch1_s8_andia2

label ch1_s8_andia1:
    $ dmood ='happy'
    d "Of course! I'd be very happy if you painted me!"
    a "...Thank you. Sit down on the chair, please."
    "Andia lights a candle next to me with a snap of her fingers and sits down on the bed."
    $ dmood = 'surprised'
    d "You make magic look so easy!"
    $ amood = 'neutral'
    a "It is easy... if you've studied it enough, that is."
    "Andia has me turn to one side, then the other until she is satisfied with my pose."
    $ dmood = 'neutral'
    d "Did you study at the Academy in the capital?"
    a "Actually, I didn't. I studied under the Krasny Ludek here in Priporovy Forest."
    $ dmood = 'surprised'
    d "The Krasny Ludek? The gnomes? As an elf?"
    a "As you might have noticed, I'm not exactly... traditional. I don't fit into the stereotype of an elf perfectly."
    $ amood = 'sad'
    a "The truth is... I didn't want to be forced into an arranged marriage when I came of age. So, right before that, I ran away from home and hid in Priporovy Forest."
    a "The Krasny Ludek found me and took me into their hidden town. There, they taught me magic."
    $ dmood = 'sad'
    d "I didn't know you had a secret like that. You're a high elf, one of the nobility?"
    a "I am a noble, but I don't feel much like one anymore."
    $ amood = 'happy'
    a "At least with the choice I've made, I can pick the person I spend the rest of my life with."
    $ dmood = 'happy'
    d "You're rather a romantic, I see."
    a "That I am."
    "Andia paints me for a while before she declares the painting finished. I get up from my spot and sit next to her."
    "Then I look at the painting and-"
    $ dmood = 'surprised'
    d "That's me?!"
    if pronoun == "she":
        "I see a beautiful dark-skinned woman smiling back at me."
    else:
        "I see a beautiful dark-skinned person smiling back at me."
    d "Is that how you see me?"
    $ amood = 'shy'
    a "Is it... bad?"
    d "Of course not! It's amazing!"
    a "You can have it... if you want."
    $ dmood = 'happy'
    d "Of course I do. Oh, how can I ever repay you!"
    a "Ah... you don't have to!"
menu:
    "Kiss her on the cheek":
        $ andia += 5
        scene andiaCG with dissolve
        "I lean in to Andia and gently kiss her cheek. She turns beet red and I smile at her as she holds a palm to the place I kissed."
        d "Thank you!"
        a "Y-you're welcome!"
        "She stutters when she's really embarrassed. How cute!"
        scene inn room
        show dobrava at right
        show andia at left
        with fade

        jump ch1_s9
    "Say you'll buy her more painting supplies":
        d "Oh, I know! I'll buy you more painting supplies!"
        $ amood = 'neutral'
        a "I guess I... would appreciate that. Thank you."
        d "No, thank you!"
        jump ch1_s9

label ch1_s8_andia2:
    $ dmood = 'neutral'
    d "Unfortunately, I don't feel comfortable with being painted."
    $ amood = 'neutral'
    a "Ah... ok."
    "We spend some time chatting about everything and nothing. Eventually, Andia yawns and I feel tired too so I decide to return to my room."
    jump ch1_s9

label ch1_s8_bogdan:
    $ dmood = 'happy'
    d "I'd like to watch Bogdan train."
    $ bmood = 'happy'
    b "Oh, I'm so happy you want to spend time with me, Dobrava!"
    b "I'll be sure to put on the best show for you!"
    $ amood = 'happy'
    a "Just don't trip and impale yourself on your sword."
    $ bmood = 'angry'
    b "Very funny! As if you didn't know I'm the best swordsman around!"
    a "Of course you are! Was there ever any doubt?"
    $ bmood = 'neutral'
    b "Now I'm not sure whether that was sincere or not. What do you think, Dobrava?"
    d "You are of course the best swordsman I know!"
    "I don't know many warriors though."
    $ bmood = 'happy'
    b "See, Dobrava thinks I'm awesome. You're amazing too, Dobrava! You're beautiful, smart, and always know what to say."
    "Uh-oh... do I like the direction this is going in?"
menu:
    "Be flirty":
        d "Well, of course I am. It's always nice to hear compliments from someone as handsome and capable as you..."
        $ amood = 'annoyed'
        a "Bleh... maybe it's time you get some time alone. I'll take my leave."
        $ zmood = 'happy'
        z "Same here. Good luck, you two."
        b "Luck? I don't need luck, I have Dobrava!"
        "I just laugh in response."
        jump ch1_s8_bogdan2
    "Say you just want to be friends with Bogdan":
        $ dmood = 'neutral'
        d "Thank you, Bogdan, but I don't want any misunderstanding between us. I just want us to be friends."
        $ bmood = 'sad'
        b "Oh..."
        "Now I've made him sad, but it's better to be clear when we've just started getting to know each other."
        d "Don't be upset. Friends are a great thing too. Friendship is as powerful as Andia's magic or a swing of your sword!"
        $ bmood = 'happy'
        b "Ah... that's right! Let's be the best of friends, Dobrava!"
        "I guess he cheers up as quickly as he gets sad. How endearing."

label ch1_s8_bogdan2:
    $ dmood = 'neutral'
    $ bmood = 'neutral'

    scene forest path
    show dobrava at right
    show bogdan at left
    with fade

    "Bogdan and I make our way outside. The tavern is located just off the main road through the forest so the calm and serene woods greet us when we exit the tavern."
    "Bogdan leads me to a clearing just a few minutes away from the tavern."
    "I watch as Bogdan takes his sword off his back and starts swinging it, showing off various complicated stances. I can't help but feel impressed."
    "It doesn't take long before he takes off his shirt and I can also be impressed watching his muscles flex in the light of the setting sun."
    $ dmood = 'shy'
    "Gods, what a view!"
    "At some point Bogdan stops to drink water and looks at me."
    $ bmood = 'surprised'
    b "Why is your face so red?"
    "Uh-oh. I must be blushing really hard for it to be visible on my darker complexion."
    d "It's nothing!"
    "Bogdan approaches me. He kneels in front of where I'm sitting on a log and looks at me with worry in his eyes."
    b "Whoa... your ears are red too."
    d "I'm saying it's nothing!"
    "He ignores me and, with a focused expression, places one hand on each of our foreheads."
    $ bmood = 'sad'
    b "Hmm.. you seem to have a fever, Dobrava!"
    "How do I get out of this? I don't know, but one thing's for sure: I'm too embarrassed to explain it to him!"
menu:
    "Tell him nothing's wrong":
        d "Nothing is wrong... I'm fine, really."
        $ bmood = 'angry'
        b "Why are you lying to me?!"
        jump ch1_s8_bogdan3
    "Admit to having a fever":
        d "Yes, it seems I do have a fever."
        $ bmood = 'angry'
        b "Figured!"

label ch1_s8_bogdan3:
    "Uh-oh. Now he's angry."
    scene bogdanCG with dissolve
    "Before I can react, Bogdan takes me in his arms."
    $ dmood = 'surprised'
    d "What are you doing?! Put me down!"
    b "You're sick. I have to take care of you. My mother always told me a warrior's strength is in how they can protect others."
    "This is the first time I've heard about Bogdan's mother."
menu:
    "Ask about Bogdan's mother":
        $ bogdan += 5
        jump ch1_s8_bogdan4
    "It's too private. Drop the subject":
        jump ch1_s8_bogdan5

label ch1_s8_bogdan4:
    $ dmood = 'surprised'
    d "Your mother, Bogdan... would you tell me more about her?"
    $ dmood = 'happy'
    b "Ah, my mother! Her name is Vshebora. She's an amazing warrior!  She was the one who taught me to use swords, axes, and maces. She can kill monsters like no one else I know."
    "Bogdan's mother is probably the source of his fascination with being a strong warrior and powerful weapons."
    $ dmood = 'happy'
    d "That's amazing! Where is she now?"
    $ bmood = 'sad'
    b "Probably somewhere to the west, adventuring at the border of Darkness."
    $ dmood = 'sad'
    d "Isn't that the most dangerous place in Ostoya?"
    b "It is! But my mother is powerful! No one can defeat her!"
    $ dmood = 'happy'
    d "Of course!"
    $ dmood = 'neutral'
    "I can't help but feel worried though. There are all manner of abominations, creatures from nightmares that no one can imagine, lurking at the edge between Ostoya and the Darkness-eaten lands."
    "But someone has to protect us, the ones trying to just live our lives in this land, from the Darkness."
    "And those courageous people are Ostoya's most powerful adventurers."
    "I guess Bogdan's mother is one such individual. I feel grateful to her for both giving birth to Bogdan and dedicating her life to protecting others."
    d "Do you hope to one day join Vshebora on the border, Bogdan?"
    $ bmood = 'happy'
    b "Yes, of course! But she said I need to get even stronger first! She'll come pick me up in a few years. I hope the rest of the party will come too!"
    "This is the most I've ever heard Bogdan speak. I can tell how important his mother is to him."
    d "Thank you for sharing this with me."
    $ bmood = 'shy'
    b "Ehh... no need to thank me. If you want to know something, just ask."

label ch1_s8_bogdan5:
    $ dmood = 'neutral'
    $ bmood = 'neutral'
    "The subject is probably too private for Bogdan to talk about with someone he met just a few hours ago."
    "We walk back to the tavern in silence."
    jump ch1_s8_bogdan6

label ch1_s8_bogdan6:
    $ zmood = 'surprised'
    $ bmood = 'neutral'
    $ dmood = 'shy'

    scene tavern
    show zygmunt at left
    show bogdan at center
    show dobrava at right
    with fade

    z "Whoa... what's wrong?!"
    "Zygmunt leaves his table where he was playing cards with some other tavern patrons and runs up to us."
    $ bmood = 'sad'
    b "Dobrava is sick."
    d "I feel much better now, Bogdan. You can put me down."
    "But he doesn't. Instead he makes his way up the stairs to my room."
    $ zmood = 'sad'
    z "What's wrong with her?"
    if pronoun == 'she':
        b "She has a fever."
    else:
        b "They have a fever."
    d "Not anymore, I'm fine!"

    scene inn room
    show zygmunt at left
    show bogdan at center
    show dobrava at right
    with dissolve

    $ zmood = 'neutral'
    "Bogdan puts me on the bed very gently and kneels to take off my shoes."
    d "Bogdan! Stop this!"
    if pronoun == 'she':
        b "Look at how red her face is!"
    else:
        b "Look at how red their face is!"
    "Zygmunt looks at the shirtless Bogdan kneeling in front of me and then at my face which is surely beet red. Then he smiles brightly, understanding in his eyes."
    $ zmood = 'happy'
    z "Well, excuse me then, it looks like you've got the situation under control, Bogdi. I'm going back to my table."
    if pronoun == 'she':
        b "Aren't you even a bit worried about her health?!"
        z "She's not sick, Bogdan. You're just embarrassing her parading around half-naked. How cute."
    else:
        b "Aren't you even a bit worried about their health?!"
        z "They're not sick, Bogdan. You're just embarrassing them parading around half-naked. How cute."
    $ bmood = 'surprised'
    "Chuckling, he leaves. Bogdan looks at me with wide eyes."
    b "Oh..."
    "I hide my face in my hands. This is so embarrassing."
    d "I'm sorry, Bogdan..."
    $ bmood = 'shy'
    b "Sorry... there's no need to be sorry... it's a misunderstanding on my part..."
    b "I will take my leave."
    "Well, that was awkward."
    jump ch1_s9

label ch1_s8_zygmunt:
    $ dmood = 'happy'
    d "I'd like to play cards with Zygmunt."
    $ zmood = 'happy'
    z "I'm happy you want to spend time with me, Dobrava!"
    $ zmood = 'neutral'
    z "Or do you just want to play cards?"
menu:
    "Be flirty":
        d "Why? Are you scared your charms won't work on me? Of course I'd like to spend more time with you and get to know you better, handsome!"
        $ zmood = 'happy'
        z "That's music to my ears, my dear. Come, let's play!"
        jump ch1_s8_zygmunt2
    "You just want to play cards with a friend":
        d "I just want to play cards. With the additional benefit of getting to know a friend better."
        $ zmood = 'happy'
        z "A friend? Alright. I see. Playing games with a friend is a fine way to spend any evening"
        jump ch1_s8_zygmunt2

label ch1_s8_zygmunt2:
    hide bogdan
    hide andia
    show zygmunt at left
    show dobrava at right
    with fade

    "Zygmunt leads me to one of the tables in the middle of the tavern. We sit down opposite each other. From his bag he pulls out a deck of cards."
    $ dmood = 'neutral'
    d "What will we be playing?"
    $ zmood = 'neutral'
    z "Kings and Queens? Leshy?"
    $ dmood = 'happy'
    d "Let's go with Leshy."
    $ zmood = 'happy'
    z "If so, we should place bets."
    $ dmood = 'surprised'
    d "Bets? I don't know about you, but I don't have an awful lot of money."
    z "Not that type of bet. Let's say... the person who loses has to grant one wish to the winner."
    "That's dangerous... but exciting nonetheless."
menu:
    "Agree":
        jump ch1_s8_zygmunt3
    "Say you'd rather play without betting":
        $ dmood = 'neutral'
        d "I'd rather play without betting. I don't like this idea."
        $ zmood = 'neutral'
        z "Alright, as you wish."
        "We play a few rounds of cards and pass the evening in happy companionship."
        "Eventually it's time to go to sleep, so we head to our respective rooms."
        jump ch1_s9

label ch1_s8_zygmunt3:
    $ dmood = 'happy'
    d "Alright. Anything?"
    $ zmood = 'happy'
    z "Yes, anything as long as it's consensual. And nothing big, it should be done in a minute or so and here in the tavern."
    "Whoa? I wonder what his wish is. Should I lose on purpose to find out?"
menu:
    "You can't lose. You always play to win":
        "No, it would be unlike me to not play to win, and it wouldn't be fair towards Zygmunt either."
        "The first two rounds of Leshy we play are a tie. I'm good at Leshy, but clearly Zygmunt is too."
        z "Wow, you are a fierce opponent."
        d "So are you."
        $ dmood = 'surprised'
        "But with the third game the luck is not on my side and I pull weak cards. I win one round of three but I lose the other two."
        jump ch1_s8_zygmunt4
    "Lose on purpose":
        "I'm too curious about what Zygmunt wants from me. I'm usually super competitive and good at Leshy, but I think I'll play to lose this time around."
        "We play three rounds and I win only one of them, not to arouse any suspicion. This makes me the loser."
        jump ch1_s8_zygmunt4

label ch1_s8_zygmunt4:
    $ dmood = 'sad'
    d "I lost..."
    z "Hah. That means I won. Double or nothing?"
    $ dmood = 'neutral'
    d "No, it's fine. You're too strong an opponent for me. So, what's your wish?"
    $ zmood = 'shy'
    "He hesitates for a moment and blushes. Huh? He blushes?"
    z "This has to be consensual so you can always say no."
    d "Uh-huh."
    z "But may I ask you for a kiss?"
    $ dmood = 'surprised'
    "Huh?! He wants to kiss me?!"
menu:
    "Agree and kiss him on the lips":
        $ zygmunt += 5
        $ kissZygmunt = True
        jump ch1_s8_zygmunt5
    "Agree, but kiss him on the cheek":
        $ kissZygmunt = True
        jump ch1_s8_zygmunt6
    "Say no. You want to be friends":
        jump ch1_s8_zygmunt7

label ch1_s8_zygmunt5:
    z "Forget it... that might have been too much to ask..."
    $ dmood = 'happy'
    $ zmood = 'surprised'
    "I get up and go around the table to his side. Then I grab him by the collar of his shirt and kiss him. He is surprised at first but kisses me back."
    "Well, I have to say he is good at this. But when he licks my lower lip, asking for permission to deepen the kiss, I pull back. That's too much for my first kiss with him."
    "Either way, I enjoyed our moment of intimacy and I don't regret it. I smile at him and he smiles back."
    z "I didn't expect you would agree to that..."
    d "Then I'm happy to have surprised you."
    "We play a few more rounds of cards and pass the evening in happy companionship. Eventually it's time to go to sleep, so we head to our respective rooms."
    jump ch1_s9
label ch1_s8_zygmunt6:
    z "Forget it... that might have been too much to ask..."
    $ dmood = 'neutral'
    "I go around the table to his side and lean in front of him. But I kiss him on the cheek. When I pull back he looks surprised and a bit disappointed."
    $ zmood = 'sad'
    z "That's not what I meant..."
    $ dmood = 'happy'
    d "You didn't specify where the kiss should be. I believe I upheld my end of the bet."
    $ zmood = 'happy'
    z "Alright. I'll be more precise with my words next time."
    "We play a few more rounds of cards and pass the evening in happy companionship. Eventually it's time to go to sleep, so we head to our respective rooms."
    jump ch1_s9
label ch1_s8_zygmunt7:
    z "Forget it... that might have been too much to ask..."
    $ dmood = 'sad'
    d "I think you've got the wrong idea about... us, Zygmunt. I just want to be friends with you."
    $ zmood = 'sad'
    z "Ah... ok. I understand."
    "He looks so sad and disappointed that I get up and go over to his side of the table. I lean in and give him a hug."
    $ zmood = 'neutral'
    z "Thank you. I appreciate the consolation prize."
    $ dmood = 'happy'
    d "I'm glad you liked it."
    "We play a few more rounds of cards and pass the evening in happy companionship. Eventually it's time to go to sleep, so we head to our respective rooms."
    jump ch1_s9

label ch1_s8_alone:
    hide zygmunt
    hide bogdan
    hide andia
    with dissolve
    show dobrava at center with move
    "I decide to spend my evening doing bard things. After all, everyone needs a bit of time to themselves. So do I."
    "I sit at my usual spot, tell stories, and play the flute."
    "Eventually it's time to go to sleep, so I head up to my room."
    jump ch1_s9
