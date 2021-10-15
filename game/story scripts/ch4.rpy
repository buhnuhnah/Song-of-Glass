label ch4_s1:
    stop music fadeout 1.0
    play music2 "dark magic music (level 3).ogg" fadein 1.0 loop
    $ dmood = 'angry'
    $ ymood = 'smirk'
    scene throne room
    show dobrava at right
    show yarlomila at left
    with Fade(0.5, 1.0, 0.5)

    "Several days pass. I don't feel the need to eat or sleep. It's like I've been frozen in time alongside everything else."
    "Occasionally, Yarlomila's zombie servants bring her fresh piles of bones from some poor souls whose graves have been desecrated."
    "She places the souls of the dead which float around in one of the castle's rooms - beautiful lights which I thought were nothing special - into those bones, creating new skeleton servants."
    "One time she creates a zombie and I almost faint from the smell of death as it passes by me."
    "One day when Yarlomila is not busy, I decide to have a serious talk with her."
    stop music2 fadeout 1.0
    play music "Yarlomila Theme (main).ogg" fadein 1.0 loop
    d "Hey!"
    y "Oh, so you've decided to finally grace me with your beautiful voice?"
    d "I won't sing for you. Ever! But we can talk."
    y "Please go ahead. What would you like to talk about?"
    d "You. Why do you seem so sad? So lonely?"
    $ ymood = 'sad'
    y "Because as you can see there is no one here. I'm alone in this world."
    $ ymood = 'smirk'
    y "Well, until you arrived. So I've decided to keep you. Now I have company."
    $ dmood = 'neutral'
    d "Do you realise that as long as you keep me caged, I'll never want to be your friend?"
    $ ymood = 'surprised'
    y "Friend? That's too much to ask for someone such as I. The presence of another is enough for me."
    "So she doesn't believe she can have friends. Do I want to be her friend? I guess I do, since from the first time I met her I felt like I wanted to save her..."
    $ dmood = 'happy'
    d "Ok, I know what we should do, Yarlomila!"
    y "Yes?"
    d "Let's get to know each other! Then we can decide if we can be friends!"
    $ ymood = 'neutral'
    y "If it means hearing your beautiful voice... Sure, let's talk."

    if songbird >= 10 or (andia < 10 and bogdan < 10 and zygmunt < 10) or end_buddy == 'self':
        jump end_songbird
    else:
        if end_buddy == 'zygmunt':
            jump ch4_s2_zygmunt
        elif end_buddy == 'bogdan':
            jump ch4_s2_bogdan
        else:
            jump ch4_s2_andia

label end_songbird:
    stop music fadeout 1.0
    play music2 "kujawiak (accompanied).ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    $ ymood = 'smirk'
    "Days pass by and Yarlomila and I get to know each other better."
    "I grow to like her, but she never lets me out of the cage and I can't convince her of the true value of friendship... because my so-called friends never come to rescue me."
    $ dmood = 'sad'
    "I feel so disappointed when I think about it."
    $ dmood = 'neutral'
    "But I have Yarlomila now. I will talk only to her and sing only for her. And I will stay forever in this golden cage."
    $ ymood = 'happy'
    y "My Songbird..."
    scene black with Fade(0.75, 0.0, 0.0)
    "Ending 2: Songbird"
    return

label ch4_s2_zygmunt:
    stop music fadeout 1.0
    play music2 "combat music (level 0).ogg" fadein 1.0 loop
    $ zmood = 'angry'
    $ bmood = 'sad'
    $ amood = 'neutral'
    scene tavern
    show bogdan at right
    show andia at left
    show zygmunt at center
    with Fade(0.5, 0.75, 0.5)

    if pronoun == 'she':
        z "Where is she?! We need to find her!"
    else:
        "Where are they?! We need to find them!"
    "I kick the chair while screaming at the scepter's handle. As if it would answer. The only thing my outburst accomplishes is knocking the chair over." with sshake
    $ bmood = 'surprised'
    b "Zygmunt, calm down!"
    if pronoun == 'she':
        jump ch4_s2_zygmunt2a
    else:
        jump ch4_s2_zygmunt2b

label ch4_s2_zygmunt2a:
    z "This useless piece of trash... tell me where she is!"
    "When I went to wake Dobrava the morning after meeting Leshy, she was gone."
    "We looked everywhere for her: the town, the forest, the ruins. Nothing. Not a single stone was left unturned, and yet we could not find her."
    "It's not like her to disappear on us like that... On me..."
    if not end_friendship:
        "I thought we had feelings for each other... or the beginning of them at least. She agreed to be courted by me... No, stop with the doubts!"
    else:
        "I thought she was my friend... no, stop with the doubt! She {i}is{/i} my friend!"
    "She wouldn't just leave! I have a bad feeling about this. She must have been abducted somehow... but by whom and why?"
    jump ch4_s2_zygmunt3

label ch4_s2_zygmunt2b:
    z "This useless piece of trash... tell me where they are!"
    "When I went to wake Dobrava the morning after meeting Leshy, they were gone. We looked everywhere for them: the town, the forest, the ruins. Nothing.Not a single stone was left unturned, and yet we could not find them."
    "It's not like them to disappear on us like that... On me..."
    if end_buddy == 'zygmunt' and not end_friendship:
        "I thought we had feelings for each other... or the beginning of them at least. They agreed to be courted by me... No, stop with the doubts!"
    else:
        "I thought they were my friend... no, stop with the doubt! They {i}are{/i} my friend!"
    "They wouldn't just leave! I have a bad feeling about this. They must have been abducted somehow... but by whom and why?"
    jump ch4_s2_zygmunt3

label ch4_s2_zygmunt3:
    "I kick the chair laying on the ground but all I accomplish is hurting my foot." with pain
    z "Ouch!"
    "Innkeeper Marysia" "Stop damaging my property, Zygmunt!"
    "Marysia comes out of the kitchen with a frying pan and waves it around threateningly."
    $ zmood = 'sad'
    z "Ah... sorry."
    "Innkeeper Marysia" "Look, I know you're worried about Dobrava, but my furniture is not at fault here."
    "With a sigh I stand the chair upright again and sit down."
    $ bmood = 'sad'
    z "I'm sorry."
    "Innkeeper Marysia" "That's better."
    "The innkeeper disappears back to the kitchen. My friends sit down by the table."
    b "I'm really worried, Zygmunt-"
    $ amood ='happy'
    a "I see!"
    $ bmood = 'surprised'
    $ zmood = 'surprised'
    "Andia who has been ignoring my outburst - much to my annoyance as I wanted everyone to witness my theatrics - finally looks up from the notebook in which she had scribbled a bunch of Elven mumbo-jumbo."
    $ bmood = 'neutral'
    $ zmood = 'neutral'
    "We both look at her expectantly. As much as I dislike her unnecessary rambling, especially about ancient Elven history, I know when it's time to let her talk."
    a "So, the text on the handle says that only light can defeat darkness and that this scepter has the power to remove darkness from anyone's heart."
    a "But only the wielder of the scepter is capable of using its power."
    $ zmood = 'surprised'
    z "And...? How will that help us find Dobrava?"
    if pronoun == 'she':
        a "Because she is the wielder of the scepter! And since she's separated from the scepter, she can be found if someone who cares for her deeply touches it and thinks of her."
    else:
        a "Because they are the wielder of the scepter! And since they're separated from the scepter, they can be found if someone who cares for them deeply touches it and thinks of them."
    $ amood = 'neutral'
    a "It is a precaution the Elves put in place for situations such as the one we find ourselves in."
    z "So all I need to do is touch it and it will lead me to Dobrava?"
    a "That's what the text says. It's an instruction for the usage of this artifact."
    b "Try it, Zygmunt."
    $ zmood = 'neutral'
    z "Alright, let's try it then."
    if pronoun == 'she':
        "I take the handle in my hand and picture Dobrava. Memories of our time together flash in my mind. I think about the times she was angry, sad, and hurt. Ready to cry and call it quits."
        "But more importantly, I think about the times she had a brilliant smile on her face, her kindness and courage shining through all the more brightly. Gods, what a woman."
    else:
        "I take the handle in my hand and picture Dobrava. Memories of our time together flash in my mind. I think about the times they were angry, sad, and hurt. Ready to cry and call it quits."
        "But more importantly, I think about the times they had a brilliant smile on their face, their kindness and courage shining through all the more brightly. Gods, what a person."
    "Then I feel the pull."
    $ zmood = 'surprised'
    z "It's working!"
    $ bmood = 'surprised'
    b "Really?"
    a "No time to waste then, let's go!"

    $ amood = 'sad'
    $ zmood = 'angry'
    $ bmood = 'sad'

    scene forest path
    show andia at left
    show bogdan at right
    show zygmunt at center
    with fade

    "We gather our equipment and follow the pull of the scepter into the forest. We all have solemn expressions and don't talk while walking."
    "We walk and we walk... further north than we have ever traveled before. Eventually the road ends and we start walking through the forest proper."
    "Further and further we go... into the heart of the forest."

    scene ruins
    show andia at left
    show bogdan at right
    show zygmunt at center
    with fade
    "The scepter pulls us to another Elven ruin. One in which we have not been before. We don't venture this far away from civilization."
    "The further away, the more dangerous and easier it is to meet evil spirits and horrifying monsters."
    "But for Dobrava I would go to the underworld and back. Anything that dares stand between us, I would surmount."
    "However, the ruin is abandoned. There is no life or undeath here. The scepter pulls us to what looks like a mirror."
    $ zmood = 'surprised'
    z "Hmm... what is this?"
    $ amood = 'neutral'
    a "Maybe try touching the scepter to it?"
    "I do what she says and the mirror's surface starts shimmering with golden light. A whirlwind forms."
    $ amood = 'surprised'
    $ bmood = 'surprised'
    a "Ah... it's a portal!"
    "I look at my companions and they nod."
    $ zmood = 'determined'
    z "Let's go then! To rescue Dobrava!"
    "We step through the whirling lights, into a realm unknown."
    jump ch4_s3

label ch4_s2_bogdan:
    stop music fadeout 1.0
    play music2 "combat music (level 0).ogg" fadein 1.0 loop
    $ amood = 'neutral'
    $ bmood = 'sad'
    $ zmood = 'angry'

    scene tavern
    show andia at left
    show zygmunt at right
    show bogdan at center
    with Fade(0.5, 0.75, 0.5)

    if pronoun == 'she':
        b "Where is Dobrava? We need to find her!"
        "When I went to wake Dobrava the morning after meeting Leshy, she was gone."
        "We looked everywhere for her: the town, the forest, the ruins. Nothing. Not a single stone was left unturned, and yet we could not find her."
        "It's not like her to disappear on us like that... On me..."
        if end_friendship:
            "I thought she was my friend... no, of course she is my friend! The very best!"
        else:
            "I thought we had feelings for each other... She asked me to court her... No, stop with the doubts!"
        "She wouldn't just leave!"
        b "I have a bad feeling about this."
        $ zmood = 'sad'
        z "I agree. She must have been abducted somehow... but by whom? And why?"
        b "I'm so worried. What if something bad is happening to her right now?"
        b "I can't protect her when I'm here and she's... somewhere else!"
    else:
        b "Where is Dobrava? We need to find them!"
        "When I went to wake Dobrava the morning after meeting Leshy, they were gone."
        "We looked everywhere for them: the town, the forest, the ruins. Nothing.Not a single stone was left unturned, and yet we could not find them."
        "It's not like them to disappear on us like that... On me..."
        if end_friendship:
            "I thought they were my friend... no, of course they are my friend! The very best!"
        else:
            "I thought we had feelings for each other... They asked me to court them... No, stop with the doubts!"
        "They wouldn't just leave!"
        z "I agree. They must have been abducted somehow... but by whom? And why?"
        b "I'm so worried. What if something bad is happening to them right now?"
        b "I can't protect them when I'm here and they're... somewhere else!"

    $ amood = 'happy'
    a "I see!"
    "We both look at Andia who finally looks up from the notebook in which she had scribbled down a bunch of Elven mumbo-jumbo. I don't understand any of it, but I trust Andia."
    a "So, the text on the handle says that only light can defeat darkness and that this scepter has the power to remove darkness from anyone's heart."
    a "But only the wielder of the scepter is capable of using its power."
    $ zmood = 'neutral'
    b "But how can that help us find Dobrava?"
    if pronoun == 'she':
        a "Because she is the wielder of the scepter! And since she's separated from the scepter, she can be found if someone who cares for her deeply touches it and thinks of her."
    else:
        a "Because they are the wielder of the scepter! And since they're separated from the scepter, they can be found if someone who cares for them deeply touches it and thinks of them."
    $ amood = 'neutral'
    a "It is a precaution the Elves put in place for situations such as the one we find ourselves in."
    $ bmood = 'surprised'
    b "So all I need to do is touch it and it will lead me to Dobrava?"
    a "That's what the text says. It's an instruction for the usage of this artifact."
    z "Try it, Bogdan."
    "I'm scared... what if it zaps me? But for Dobrava, I will touch it if I must."
    $ bmood = 'neutral'
    b "For Dobrava!"
    if pronoun == 'she':
        "I take the handle in my hand and picture Dobrava. Memories of our time together flash in my mind. I think about the times she was angry, sad, and hurt. Ready to cry and call it quits."
        "But more importantly, I think about the times she had a brilliant smile on her face, her kindness and courage shining through all the more brightly. She's the greatest..."
    else:
        "I take the handle in my hand and picture Dobrava. Memories of our time together flash in my mind. I think about the times they were angry, sad, and hurt. Ready to cry and call it quits."
        "But more importantly, I think about the times they had a brilliant smile on their face, their kindness and courage shining through all the more brightly. They're the greatest..."
    "Then I feel the pull."
    $ bmood = 'surprised'
    b "It's working!"
    $ zmood = 'surprised'
    z "Are you sure? That's fantastic, Bogdi!"
    a "No time to waste then, let's go!"

    $ amood = 'sad'
    $ zmood = 'sad'
    $ bmood = 'sad'

    scene forest path
    show andia at left
    show zygmunt at right
    show bogdan at center
    with fade

    "We gather our equipment and follow the pull of the scepter into the forest. We all have solemn expressions and don't talk while walking."
    "We walk and we walk... further north than we have ever traveled before. Eventually the road ends and we start walking through the forest proper."
    "Further and further we go... into the heart of the forest."

    scene ruins
    show andia at left
    show zygmunt at right
    show bogdan at center
    with fade
    "The scepter pulls us to another Elven ruin. One in which we have not been before. We don't go this far away from the towns."
    "The further away, the more dangerous it is. And easier to meet evil spirits and horrifying monsters. I don't mind that at all. More challenges are always appreciated. But I don't want to put my friends in danger."
    if pronoun == 'she':
        "But for Dobrava I would go to the underworld and back. Of course I will fight anything for her!"
    else:
        "But for Dobrava I would go to the underworld and back. Of course I will fight anything for them!"
    "However, the ruin is abandoned. There is no life or undeath here. The scepter pulls us to what looks like a mirror."
    $ bmood = 'surprised'
    $ amood = 'neutral'
    $ zmood = 'neutral'
    b "Hmm... what is this?"
    a "Maybe try touching the scepter to it?"
    "I do what she says and the mirror's surface starts shimmering with golden light. A whirlwind forms."
    $ zmood = 'surprised'
    $ amood = 'surprised'
    a "Ah... it's a portal!"
    "I look at my companions and they nod."
    $ bmood = 'happy'
    b "Let's go then! To rescue Dobrava!"
    $ zmood = 'neutral'
    $ amood = 'neutral'
    "We step through the whirling lights, into a realm unknown."
    jump ch4_s3

label ch4_s2_andia:
    stop music fadeout 1.0
    play music2 "combat music (level 0).ogg" fadein 1.0 loop
    $ amood = 'neutral'
    $ bmood = 'sad'
    $ zmood = 'angry'

    scene tavern
    show bogdan at left
    show zygmunt at right
    show andia at center
    with Fade(0.5, 0.75, 0.5)

    b "How could we let this happen? Where is Dobrava?"
    if pronoun == 'she':
        z "I don't know but it looks to me like she was abducted. By whom and how, I don't know."
        "I tune out the guys' voices. The day we met Leshy, we all went to bed and the next morning, when I went to wake up Dobrava she wasn't there."
        "We looked everywhere for her: the town, the forest, the ruins. Nothing. Not a single stone was left unturned, and yet we could not find her."
        "It's not like her to disappear on us like that... On me..."
        if end_friendship:
            "She called me her precious friend."
        else:
            "She's my lover. The one I had been searching for for so long...."
        "She wouldn't leave me like that. I have no doubt."
    else:
        "I don't know but it looks to me like they were abducted. By whom and how, I don't know."
        "I tune out the guys' voices. The day we met Leshy we all went to bed and the next morning when I went to wake up Dobrava they weren't there."
        "We looked everywhere for them: the town, the forest, the ruins. Nothing. Not a single stone was left unturned, and yet we could not find them."
        "It's not like them to disappear on us like that... On me..."
        if end_friendship:
            "They called me their precious friend."
        else:
            "They're my lover. The one I had been searching for for so long...."
        "They wouldn't leave me like that. I have no doubt."

    "I focus my mind back to my purpose - studying the scepter. Understanding this thing is the only way we can find Dobrava. I'm sure of that."
    "Then it hits me... and suddenly I understand everything."
    $ amood = 'happy'
    a "I see!"
    $ bmood = 'surprised'
    $ zmood = 'surprised'
    "The guys cease shouting at each other... which I was only slightly aware of, so deep was I in my thoughts. They look at me expectantly. I take a deep breath and start explaining what I found."
    a "So, the text on the handle says that only light can defeat darkness and that this scepter has the power to remove darkness from anyone's heart."
    a "But only the wielder of the scepter is capable of using its power. "
    z "And...? How can any of that help us find Dobrava?"
    if pronoun == 'she':
        a "Because she is the wielder of the scepter!  And since she's separated from the scepter, she can be found if someone who cares for her deeply touches it and thinks of her."
    else:
        "Because they are the wielder of the scepter.  And since they're separated from the scepter, they can be found if someone who cares for them deeply touches it and thinks of them."
    $ amood = 'neutral'
    a "It is a precaution the Elves put in place for situations such as the one we find ourselves in."
    z "So all you need to do... is touch it and it will lead us to Dobrava?"
    $ bmood = 'happy'
    b "Try it, Andia!"
    $ zmood = 'neutral'
    a "That's what the text says. It's an instruction for the usage of this artifact. I'm going to try it."
    if pronoun == 'she':
        "I take the handle in my hand and picture Dobrava. Memories of our time together flash in my mind. I think about the times she was angry, sad, and hurt. Ready to cry and call it quits."
        "But more importantly, I think about the times she had a brilliant smile on her face, her kindness and courage shining through all the more brightly. She's amazing."
    else:
        "I take the handle in my hand and picture Dobrava. Memories of our time together flash in my mind.  I think about the times they were angry, sad, and hurt. Ready to cry and call it quits."
        "But more importantly, I think about the times they had a brilliant smile on their face, their kindness and courage shining through all the more brightly. They're amazing."
    "Then I feel the pull."
    $ amood = 'surprised'
    a "It's working!"
    $ bmood = 'surprised'
    $ zmood = 'surprised'
    b "Really?"
    $ amood = 'neutral'
    a "No time to waste then, let's go!"

    $ amood = 'sad'
    $ zmood = 'sad'
    $ bmood = 'sad'
    scene forest path
    show bogdan at left
    show zygmunt at right
    show andia at center
    with fade

    "We gather our equipment and follow the pull of the scepter into the forest. We all have solemn expressions and don't talk while walking."
    "We walk and we walk... further north than we have ever traveled before. Eventually the road ends and we start walking through the forest proper."
    "Further and further we go... into the heart of the forest."

    scene ruins
    show bogdan at left
    show zygmunt at right
    show andia at center
    with fade
    "The scepter pulls us to another Elven ruin. One in which we have not been before. We don't venture this far away from civilization."
    "I've been this far away only in the presence of Krasny Ludek. With them, I felt safe from the monsters and the dangers of the Priporovy Forest."
    "But for Dobrava I would go to the underworld and back. Anything that stands between us, I would surmount."
    "However, the ruin is abandoned. There is no life or undeath here. The scepter pulls us to what looks like a mirror."
    $ zmood = 'surprised'
    z "Hmm... what is this?"
    $ amood = 'neutral'
    a "Maybe I should try touching the scepter to it?"
    "I do it and the mirror's surface starts shimmering with golden light. A whirlwind forms."
    $ amood = 'surprised'
    $ bmood = 'surprised'
    a "Ah... it's a portal!"
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ zmood = 'neutral'
    "I look at my companions and they nod."
    a "Let's go then! To rescue Dobrava!"
    "We step through the portal."
    jump ch4_s3

label ch4_s3:
    stop music2 fadeout 1.0
    play music "Yarlomila Theme (main).ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    $ ymood = 'smirk'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene throne room
    show yarlomila at left
    show dobrava at right
    with Fade(0.5, 0.75, 0.5)
    y "So will you sing for me today?"
    "Should I? She's been asking me this for a few days now. I know it's important to her for some reason."
    "Before I can make my decision though, there is a blinding flash of golden light. A portal opens in the middle of the throne room." with flash
    $ ymood = 'angry'
    y "What is light magic doing in my domain?!"
    "From the portal three people emerge. I immediately recognise them."
    show yarlomila at right
    show dobrava at farright
    with move
    if end_buddy == 'zygmunt':
        show bogdan at leftish
        show andia at farleft
        show zygmunt at center
        with dissolve
        "Zygmunt, Bogdan and then Andia come out one after another. The portal closes."
    elif end_buddy == 'bogdan':
        show andia at farleft
        show zygmunt at leftish
        show bogdan at center
        with dissolve
        "Bogdan, Zygmunt and then Andia come out one after another. The portal closes."
    else:
        show bogdan at leftish
        show zygmunt at farleft
        show andia at center
        with dissolve
        "Andia, Bogdan and then Zygmunt come out one after another. The portal closes."

    a "Well, our one known exit closing isn't ideal..."
    $ zmood = 'surprised'
    $ bmood = 'surprised'
    $ amood = 'surprised'
    "Then they notice the birdcage with me inside it."
    if end_buddy == 'zygmunt':
        z "Dobrava?! What the hell are you doing there?!"
        $ dmood = 'happy'
        d "Just hanging around, I guess."
        $ zmood = 'angry'
        $ dmood = 'neutral'
        z "This is no time for jokes! Why are you in a cage? Who in the world would do something like this?!"
    elif end_buddy == 'bogdan':
        b "Dobrava?! What are you doing in there?!"
        $ dmood = 'sad'
        d "I'm trapped, as you can see."
        $ bmood = 'angry'
        b "What the hell! I'll kill whoever has done this to you!"
    else:
        a "Dobrava?! What in the world are you doing in a cage?!"
        $ dmood = 'sad'
        d "I'm trapped here, I guess."
        $ amood = 'angry'
        a "Who would dare imprison you?!"
    $ dmood = 'neutral'
    $ amood = 'angry'
    $ bmood = 'angry'
    $ zmood = 'angry'
    "They then notice Yarlomila standing next to the cage. She is smiling her creepy smile again, her eyes emotionless."
    y "Hello. Welcome to my domain."
    z "Who in the world are you?!"
    b "Someone to fight, that's for sure!"
    a "I think that's the necromancer Leshy tasked us with defeating."
    $ ymood = 'sad'
    y "Correct! Now dear guests, do you want to defeat the great evil and become heroes?"
    "I notice she looks somewhat sad as she says that, regret and sorrow tinging her voice. It couldn't be... does she want to die and be freed from her loneliness and pain?"
    stop music fadeout 1.0
    play music2 "combat music (level 3).ogg" fadein 1.0 loop
    "Is that why she has done all this? Did she capture me to lure my friends here and have them play heroes?"
menu:
    "Let your friends kill the necromancer":
        jump ch4_s3_2
    "Scream at your friends to let you out":
        jump ch4_s3_3

label ch4_s3_2:
    $ dmood = 'angry'
    "What does it matter why she's done it? She's evil after all. She's killed many and has played with the boundary between life and death. She should die."
    "Bogdan moves in to attack Yarlomila while holding her undead servants at bay. Zygmunt shoots arrows at her from behind and Andia prepares a spell."
    "Her incantation takes several moments, but the effect is spectacular when she finally casts it."
    "A whirlwind envelops the necromancer and raises her into the air. Up and up she goes towards the tall ceiling of the throne room."
    "When Yarlomila reaches the room's ceiling, Andia releases the spell and the evil wizardess drops to the floor like a puppet whose strings have been cut."
    "And she doesn't get up. For good measure, Bogdan stabs her with his sword."
    scene black with fade
    "The castle of glass shatters." with sshake

    stop music2 fadeout 1.0
    play music "Elven Ruin.ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ zmood = 'neutral'
    scene ruins
    show bogdan at farleft
    show andia at farright
    show zygmunt at leftish
    show dobrava at rightish
    "We are back in an  Elven ruin, one I have not seen before. But my friends seem familiar with this place. The birdcage crumbles and I fall on my butt on the remains of a tiled floor."
    "When I look around the room we find ourselves in what looks like the throne room I've been imprisoned in for so long. However, it's not made of glass but of crumbling stone instead."
    $ mood = 'sad'
    d "I'm so glad you've killed her. That it's finally over..."
    jump end_guilt

label ch4_s3_3:
    $ dmood = 'sad'
    "It can't end like this. I believe we can save Yarlomila from herself even more now that I've had the chance to speak with her. She's not irredeemable."
    "Her means are evil, but her actions are the result of pain and loneliness. She doesn't deserve to die."
    "Bogdan moves in to attack Yarlomila while holding her undead servants at bay. Zygmunt shoots arrows at her from behind and Andia prepares a spell."
    "I notice it's a powerful one by how the magic shifts around her. If she succeeds in casting that, it's over."
    $ dmood = 'neutral'
    d "Andia! Help me get out of here!"
    $ amood = 'neutral'
    "She hesitates for a moment."
    d "Andia! I don't want to be here. I can't stand it any longer!"
    "That seals the deal and Andia comes closer to the cage. She breaks the lock using a blast of magic and opens the door. I jump out immediately."
    $ dmood = 'happy'
    d "Thank you!"
    $ bmood = 'hurt'
    b "Ouch!"
    $ dmood = 'surprised'
    "Bogdan yells in pain. I look at him and his arm is scorched, covered by black miasma. That's a curse that I don't have the ability to lift."
    $ dmood = 'angry'
    d "Shit!"
    "We will have to see a priest about it later."
    $ amood = 'annoyed'
    a "Here's your flute. You had better be ready to fight."
    "Andia looks annoyed. I guess she thinks Bogdan got hurt because of the delay my release caused."
    $ dmood = 'determined'
    d "Do you have the scepter too, Andia?"

    if end_buddy == 'zygmunt':
        a "Zygmunt has it. But now is not the time to-"
        "I run up to Zygmunt and scream at him to give me the scepter's handle. He looks confused but I must look very determined because he gives it to me without any questions."
    elif end_buddy == 'bogdan':
        a "Bogdan has it. But now is not the time to-"
        "I run up to Bogdan, into the center of the fight."
        $ bmood = 'surprised'
        $ zmood = 'surprised'
        b "Dobrava, what are you-"
        d "Give me the scepter's handle!"
        "Bogdan looks confused but I must look very determined because he gives it to me without any questions."
    else:
        a "I have it here. But now is not the time to-"
        d "Give it to me!"
        "Andia looks confused but I must look very determined because she gives it to me without any questions."

    $ amood = 'surprised'
    $ bmood = 'surprised'
    $ zmood = 'surprised'
    $ dmood = 'determined'
    $ ymood = 'surprised'
    "With the scepter in hand, I run up to the throne where the shining yellow jewel still sits. I put it in its place in the scepter. Then I point the weapon at Yarlomila."
    "I know what to do. I sing in ancient Elven - a language I've never spoken in my life - as the correct words somehow fill my head."
    d "Light vanquish darkness, bring good to evil, cleanse the heart of the necromancer and break the walls of the castle of glass!"
    "There is a blinding flash of light, seemingly brighter than the sun. I cover my eyes."
    "Then I feel warmth. Safety. Comfort. I feel joy and happiness. So much so that I could cry."
    $ ymood = 'sad'
    "The sounds of fighting cease. Yarlomila screams but her screams quickly turn into sobs of relief."
    scene black with fade
    "The castle of glass shatters." with sshake

    stop music2 fadeout 1.0
    play music "Elven Ruin.ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ zmood = 'neutral'
    $ ymood = 'sad'
    scene ruins
    show bogdan at farleft
    show andia at left
    show zygmunt at center
    show dobrava at rightish
    show yarlomila at farright
    "We are back in an Elven ruin, one I have not seen before. But my friends seem familiar with this place."
    "When I look around the room we find ourselves in what looks like the throne room I've been imprisoned in for so long. However, it's not made of glass but of crumbling stone instead."
    "Yarlomila is sitting on the floor sobbing and my friends stand around her, weapons drawn, but confused about what to do."
    $ dmood = 'happy'
    d "Let her be. She's not evil anymore. I cleansed her heart."
    $ dmood = 'sad'
    d "I'm so glad that it's finally over..."
    $ dmood = 'surprised'
    "I realise that I'm crying, tears streaming down my face."
    if end_buddy == 'zygmunt':
        if not end_friendship:
            "Zygmunt runs up to me and hugs me. He kisses my tears. I feel comforted, safe."
        else:
            "Zygmunt runs up to me and hugs me. I feel comforted, safe."
        "I didn't even realise I was so scared. I weep."
        $ zmood = 'neutral'
        z "Hush. It's over now. We're here now. You're safe."
        d "...thank you for saving me."
        $ zmood = 'happy'
        z "I will always come for you."
        $ bmood = 'happy'
        b "And so will we."
        $ amood = 'happy'
        a "Of course."
    elif end_buddy == 'bogdan':
        show bogdan at center
        show zygmunt at left behind bogdan
        show andia at farleft
        with move
        "Bogdan runs up to me and takes me in his arms. I weep even louder, hiding my face in his chest. With him I feel safe."
        "I didn't even realise how scared I was."
        $ bmood = 'sad'
        b "Hush. It's okay now. You're safe."
        d "...thank you for saving me."
        $ bmood = 'happy'
        b "I will always come for you."
        $ zmood = 'happy'
        z "And so will we."
        $ amood = 'happy'
        a "Of course."
    else:
        show andia at center
        show zygmunt at left behind andia
        with move
        "Andia runs up to me and hugs me tightly. I weep even louder, my face on her shoulder. With her, I feel safe again."
        "I didn't even realise how scared I was."
        $ amood = 'sad'
        a "Hush. It's okay now. You're safe."
        d "...thank you for saving me."
        $ amood = 'happy'
        a "I will always come for you."
        $ bmood = 'happy'
        b "And so will we."
        $ zmood = 'happy'
        z "Of course."
    jump end_secondChance

label end_secondChance:
    stop music fadeout 1.0
    play music2 "Yarlomila Theme (gentle).ogg" fadein 1.0 loop
    $ zmood = 'neutral'
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    z "Now, about her... I'm not sure what we should do with her."
    "Zygmunt is looking at Yarlomila who kneels on the floor of the ruined throne room, crying."
    d "The scepter cleansed her soul. She should be good again."
    b "Are we sure of that?"
    "Bogdan still has his hand on his sword handle."
    a "If we take the laws of magic and the writing on the scepter's handle into account, that should be the proper result."
    z "You mean this is what the scepter was supposed to do?"
    $ amood = 'annoyed'
    a "Were you not listening at the tavern? That's what I said."
    $ dmood = 'sad'
    d "Yarlomila?"
    "I approach Yarlomila. She looks up at me, her beautiful face in tears."
    y "Why do I feel... so guilty...? I haven't felt an emotion so strong in decades..."
    $ dmood = 'neutral'
    d "It's good that you feel guilty. After all, you've done many bad things. But... I forgive you. On the account that you will use the rest of your life to atone for your sins."
    y "Will that make the guilt go away?"
    d "I don't think anything can make it go away entirely. But hey, at least you are alive to find out."
    $ dmood = 'happy'
    d "Anyone can change so long as they live."
    $ ymood = 'neutral'
    y "Thank you, Dobrava. For not giving up on me."
    d "Of course I didn't give up, I knew you could be saved."
    "I look at the party and I see them looking at Yarlomila curiously. Andia has an especially puzzled expression on her face."
    d "Care to welcome another member of our party?"
    $ zmood = 'surprised'
    z "What... you can't just-"
    $ bmood = 'happy'
    b "She's strong. I like her."
    $ amood = 'neutral'
    a "I suppose we can find a place for one more wizard... as long as she doesn't use any forbidden magic."
    y "I won't. I promise."
    d "Zygmunt?"
    z "This is outrageous! How can you folks forgive her so easily?"
    d "Everyone deserves a second chance."
    b "Remember that time you stole at the market..."
    $ amood = 'happy'
    a "Or that time you tried to seduce the mayor's daughter..."
    $ zmood = 'happy'
    z "Ok, ok! I know I'm no saint myself! Fine! Welcome to the party, Yarlomila!"
    $ ymood = 'happy'
    y "I'm happy to be part of this... whatever this is..."
    b "An adventuring party!"
    $ ymood = 'neutral'
    y "So I'm a hero now? How cool."
    d "Yes, we are the most amazing adventuring party there is in Priporovy Forest."
    z "And, with time, in the whole of Ostoya!"
    b "Maybe one day we can catch up to my mother! She's an amazing adventurer too!"
    a "I'm sure we will, Bogdan. I'm sure we will!"
    if end_buddy == 'zygmunt':
        if end_friendship:
            jump zygmuntFriend_end
        else:
            jump zygmuntLove_end
    elif end_buddy == 'bogdan':
        if end_friendship:
            jump bogdanFriend_end
        else:
            jump bogdanLove_end
    else:
        if end_friendship:
            jump andiaFriend_end
        else:
            jump andiaLove_end
