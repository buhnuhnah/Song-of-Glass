label ch1_s9:
    stop music2 fadeout 1.0
    play music "dark magic music (level 1).ogg" fadein 1.0 loop

    scene inn room with fade
    "I toss and turn and can't fall asleep. When I do, I dream of combat and scary monsters who used to be human but no longer are."
    $ dmood = 'sad'
    show dobrava at center with dissolve
    d "No! No!"
    $ dmood = 'surprised'
    "A knock on the door wakes me up. I get dressed quickly and move to open the door."
    stop music fadeout 1.0
    play music2 "Quiet Moments.ogg" fadein 1.0 loop
    if ch1s8_buddy == "zygmunt":
        jump ch1_s9_zygmunt
    elif ch1s8_buddy == "bogdan":
        jump ch1_s9_bogdan
    else:
        jump ch1_s9_andia

label ch1_s9_zygmunt:
    show dobrava at rightish with move
    show zygmunt at farleft with dissolve
    $ zmood = 'sad'
    z "You were screaming. Did you have a nightmare?"
    $ dmood = 'sad'
    d "Yes... about what happened today."
    z "Do you want to talk about it?"
menu:
    "Say you do":
        jump ch1_s9_zygmunt2
    "Say you don't":
        jump ch1_s9_zygmunt3

label ch1_s9_zygmunt2:
    d "Sure. That would help."
    z "Can I come inside?"
    d "Sure."
    show dobrava at right
    show zygmunt at left
    with move
    "I move to the side and let Zygmunt enter my room. He sits on the bed and pats the spot next to him. I sit down."
    z "We've all been through this... first combat, first kill. It's hard at first... getting used to the brutality of it and to taking the lives of others."
    d "Yes, it's easier for me with the monsters... the undead that are supposed to be dead. I feel like it's a mercy to put those bones to rest."
    d "But when I thought that zombie was a human? I couldn't handle the thought of ending someone else's life. Even though it wouldn't have been by my hand."
    d "Just standing by while others kill... it's like you've killed too."
    z "It's not the same feeling, but I get what you mean. I hope you never have to take another person's life yourself."
    z "As for why we were so quick to try and kill that man before, even before we knew he was an undead..."
    z "The Green Zmiy bandits are evil bastards who kidnap women and children and sell them to slavers."
    z "It's better to eliminate every one of them. But still, they are human. Even though they lack basic human morals."
    d "I didn't know they were that evil..."
    z "They are. I hope that makes it a bit easier for you."
    jump ch1_s9_zygmunt4

label ch1_s9_zygmunt3:
    d "No, sorry, I don't feel like talking about it."
    z "Alright, I won't pressure you."
    z "Just know I'm here for you if you need me."
    d "Of course."
    jump ch1_s9_zygmunt4

label ch1_s9_zygmunt4:
    $ zmood = 'sad'
    z "But if you want to quit our party, I understand."
    "Do I want to quit the party? Is it too much for me?"
menu:
    "You want to continue adventuring with them":
        jump ch1_s9_zygmunt5
    "You want to quit":
        jump ending1

label ch1_s9_zygmunt5:
    $ dmood = 'neutral'
    d "I'm not a quitter. It's too early to give up. I've barely been with you one day."
    $ zmood = 'happy'
    z "I'm happy to hear that. I'd be so sad to lose you as a member of our team."
    z "I hope you can rest peacefully. I'm going to go to my room to sleep now."
    $ dmood = 'happy'
    d "Alright. Thank you for talking with me."
    z "I'm always up for a conversation. You can share all your worries with me."
    d "Thank you."
    hide zygmunt with dissolve
    show dobrava at center with move
    "Zygmunt leaves and I lock the door behind him. It's time to try to sleep again."
    "I feel lighter now, as if a weight has been lifted off my shoulders. I'm glad he understands and acknowledges how I feel."
    jump ch1_s10

label ch1_s9_bogdan:
    $ bmood = 'surprised'
    show dobrava at rightish with move
    show bogdan at farleft with dissolve
    b "You were screaming! Did you have a nightmare?"
    $ dmood = 'sad'
    d "Yes... about what happened today."
    $ bmood = 'sad'
    b "Do you want to talk about it?"
menu:
    "Say you do":
        jump ch1_s9_bogdan2
    "Say you don't":
        d "No, sorry, I don't feel like talking about it."
        b "Alright, I won't pressure you."
        $ bmood = 'neutral'
        b "Just know that I'm here for you if you need me."
        d "Of course"
        jump ch1_s9_bogdan3

label ch1_s9_bogdan2:
    d "Sure. That would help."
    b "Can I come inside?"
    d "Sure."
    show dobrava at right
    show bogdan at left
    with move
    "I move to the side and let Bogdan enter my room. He paces the room and I sit down on the bed."
    b "It's not about.... the misunderstanding today, right?"
    $ dmood = 'surprised'
    d "What? No! It's about the fighting."
    b "Ah... phew... so what exactly is bothering you about it? I'm not the most insightful person, but I can listen and maybe give some advice?"
    $ dmood = 'sad'
    d "Thank you, Bogdan. I really appreciate it."
    d "This was my first fight, the first kill I've witnessed. I guess the brutality of it... is something I have to get used to."
    $ bmood = 'surprised'
    b "The brutality of it... I guess it is pretty gruesome, now that I think of it. When I'm fighting, all I think about is winning."
    $ bmood = 'neutral'
    b "On the other side of my sword is a monster who will take someone's life if I don't do something about it."
    d "Yes, it's easier for me to accept if we are speaking of monsters... the undead that are supposed to be dead. I feel like it's a mercy to put those bones to rest."
    d "But when I thought that zombie was a human? I couldn't handle the thought of ending someone else's life. Even though it wouldn't have been by my hand."
    d "Just standing by while others kill... it's like you've killed too."
    $ bmood = 'sad'
    b "It's not the same feeling, but I get what you mean."
    $ bmood = 'angry'
    b "But the man there... he was a monster too. One of the Green Zmiy bandits who are evil bastards! They kidnap women and children and sell them to slavers."
    $ bmood = 'sad'
    b "It's better to eliminate every one of them. But still, they are human. Even though they lack basic human morals."
    d "I didn't know they were that evil..."
    b "They are. I don't know if that makes it any easier for you but I hope it does."
    jump ch1_s9_bogdan3

label ch1_s9_bogdan3:
    $ bmood = 'sad'
    b "But if you want to quit being an adventurer, I totally get it and I will speak wth Zygmunt on your behalf."
    $ dmood = 'neutral'
    "Do I want to quit the party? Is it too much for me?"
menu:
    "You want to continue adventuring with them.":
        jump ch1_s9_bogdan4
    "You want to quit":
        jump ending1

label ch1_s9_bogdan4:
    d "I'm not a quitter. It's too early to give up. I've barely been with you one day."
    $ bmood = 'neutral'
    b "You really don't have to force yourself!"
    d "I'm not! I want to spend more time with you... get to know you better, achieve something together!"
    $ bmood = 'happy'
    b "I'm so happy! I'd be sad if I had to lose you as a member of our team."
    $ dmood = 'happy'
    b "I hope you'll sleep better now. I'm going back to my room."
    d "Alright. Thank you for talking with me."
    b "I'm always happy to talk!"
    d "Thank you."
    hide bogdan with dissolve
    show dobrava at center with move
    "Bogdan leaves and I lock the door behind him. It's time to try to sleep again."
    "I feel lighter now, as if a weight has been lifted off my shoulders. I'm glad he understands and acknowledges how I feel."
    jump ch1_s10

label ch1_s9_andia:
    $ amood = 'sad'
    show dobrava at rightish with move
    show andia at farleft with dissolve
    a "You were screaming. Did you have a nightmare?"
    $ dmood = 'sad'
    d "Yes... about what happened today."
    a "Do you want to talk about it?"
menu:
    "Say you do":
        jump ch1_s9_andia2
    "Say you don't":
        d "No, sorry. I don't feel like talking about it."
        a "Alright, I won't pressure you."
        $ amood = 'neutral'
        a "Just know I'm here for you if you need me."
        d "Of course."
        jump ch1_s9_andia3

label ch1_s9_andia2:
    d "Sure. That would help."
    a "Can I come inside?"
    d "Sure."
    show dobrava at right
    show andia at left
    with move
    "I move to the side and let Andia enter my room. I sit down on the bed and Andia takes the chair and moves it to sit opposite me."
    a "It's about the fight with the zombie today, isn't it?"
    d "It is. This was my first fight, the first kill I've witnessed. I guess the brutality of it... is something I have to get used to."
    d "It's easier for me to accept if we are speaking of monsters... the undead that are supposed to be dead. I feel like it's a mercy to put those bones to rest."
    d "But when I thought that zombie was a human? I almost couldn't handle the thought of ending someone else's life. Even though it wouldn't have been by my hand."
    d "Just standing by while others kill... it's like you've killed too."
    a "It's not the same feeling, but I get what you mean."
    a "But the man there... he was a monster too. One of the Green Zmiy bandits who kidnap women and children and sell them to slavers."
    $ dmood = 'surprised'
    d "I see.."
    $ amood = 'annoyed'
    a "It's better to eliminate every one of them. But still, they are human. Even though they lack basic human morals."
    $ dmood = 'sad'
    d "I didn't know they were that evil..."
    $ amood = 'sad'
    a "They are. I don't know if that makes it any easier for you but I hope it does."
    jump ch1_s9_andia3

label ch1_s9_andia3:
    $ amood = 'sad'
    a "But if you want to quit being an adventurer... after today it would be understandable."
    "Do I want to quit the party? Is it too much for me?"
menu:
    "You want to continue adventuring with them":
        jump ch1_s9_andia4
    "You want to quit":
        jump ending1

label ch1_s9_andia4:
    $ dmood = 'neutral'
    d "I'm not a quitter. It's too early to give up. I've barely been with you one day."
    $ amood = 'neutral'
    a "Okay, but if you ever feel like it's too much for you, let me know."
    d "I want to spend more time with you... get to know you better, achieve something together."
    a "That's good. I'd be sad if I had to lose you as a member of our team."
    a "I hope you'll sleep better now. I'm going back to my room."
    $ dmood = 'happy'
    d "Alright. Thank you for talking with me."
    a "You can always talk to me, if something is bothering you."
    d "Thank you."
    hide andia with dissolve
    show dobrava at center with move
    "Andia leaves and I lock the door behind her. It's time to try to sleep again."
    "I feel lighter now, as if a weight has been lifted off my shoulders. I'm glad she understands and acknowledges how I feel."
    jump ch1_s10

label ending1:
    stop music2 fadeout 1.0
    play music "mazurka (accompanied).ogg" fadein 1.0 loop
    $ dmood = 'sad'
    d "I guess that's right. I... I'd like to stop doing this...if you don't mind."
    if ch1s8_buddy == "zygmunt":
        $ zmood = 'neutral'
        z "Of course I don't. We dragged you into adventuring and you tried. Now you can say that you tried and you don't like it. That's better than having never tried at all."
    elif ch1s8_buddy == "bogdan":
        $ bmood = 'happy'
        b "Don't worry about it, Dobrava! We dragged you into adventuring and you tried. This isn't for everyone and it doesn't have to be for you!"
    else:
        $ amood = 'neutral'
        a "You should first and foremost care about yourself, Dobrava. We dragged you into adventuring and it ended up being not for you. No hard feelings on my part."
    $ dmood = 'neutral'
    d "You're right."

    $ amood = 'sad'
    $ bmood = 'sad'
    $ dmood = 'neutral'
    $ zmood = 'sad'

    scene tavern
    show bogdan at leftish
    show andia at farleft
    show zygmunt at rightish
    show dobrava at farright
    with fade

    "In the morning I explain the situation to everyone. They are sad, but they let me go."
    hide bogdan
    hide andia
    hide zygmunt
    with dissolve
    show dobrava at center with move
    "They leave for another adventure, while I take my place on my stool by the fireplace. I tell stories and play my flute."
    "Just another day in a bard's life."
    scene black with Fade(1, 0.0, 0.0)
    "Ending 1: Not an Adventurer"
    return

label ch1_s10:
    stop music2 fadeout 1.0
    play music "dark magic music (level 0).ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    scene yarlomilaCG with Fade(0.75, 1.0, 0.75)

    "When I fall asleep, I'm inside a strange castle. It's walls, floors, and ceilings are translucent, as if made of glass. But when I touch them they feel solid and sturdy."
    "The castle is very bare-bones, lacking any sort of decorations. Everything is a bit fuzzy to me and I realise I'm dreaming."
    "In front of me on a throne sits a beautiful woman with long, flowing raven-hair. She has a bored expression on her face but when I approach her, she smiles. She smiles, but her eyes remain cold."
    d "Who are you?"
    "I ask her but she doesn't respond. She just keeps smiling."
    scene inn room with dissolve
    "The dream ends and I wake up, hearing a knock on the door. It's Zygmunt calling me for breakfast. I get dressed quickly and come down to the main tavern room."
    jump ch2_s1
