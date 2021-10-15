label zygmuntFriend_end:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Song of Glass (main title).ogg" fadein 1.0 loop
    $ zmood = 'neutral'
    $ dmood = 'angry'
    scene office
    show zygmunt at left
    show dobrava at right
    with Fade(0.75, 0.5, 0.75)
    z "I still think it was worth it."
    d "It totally was not!"
    "I scream at Zygmunt as we leave the mayor's office... after I paid for his release from the jail underneath the townhouse."

    scene marketplace
    show zygmunt at left
    show dobrava at right
    with fade

    d "When will you ever learn?!"
    $ zmood = 'sad'
    z "But..."
    d "We have enough money to get by, Zygmunt. You don't have to steal."
    z "But... it's stronger than me. The rush I get while stealing... the satisfaction when I succeed."
    $ dmood = 'sad'
    d "You need to get help, Zygmunt."
    z "I know..."
    "After that conversation, Zygmunt agrees to see a therapist for his kleptomania. It takes almost half a year but he does get better. All that time, I'm there for him."
    "I'm there for him when he cries. When he has to relive his childhood on the streets, before the orphanage took him in."
    "When he has to remember the hunger and when he realizes it's no longer there. That he doesn't need to steal."
    $ zmood = 'neutral'
    $ dmood = 'happy'
    "It takes years of therapy for Zygmunt to heal. But he heals. It's not easy but with belief in oneself and support from others, one can get better. And Zygmunt does."
    $ zmood = 'happy'
    z "Thank you, Dobrava, for being there for me."
    d "I'll always be there for you, Zygmunt. You're my best friend."
    z "And you are mine."
    scene black with Fade(0.75, 0.0, 0.0)
    "Zygmunt Friendship Ending"
    return

label zygmuntLove_end:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Song of Glass (main title).ogg" fadein 1.0 loop
    $ zmood = 'neutral'
    $ dmood = 'neutral'
    scene marketplace
    show zygmunt at left
    show dobrava at right
    with Fade(0.75, 0.5, 0.75)

    "It's been two years since we defeated Yarlomila and cleansed her heart from evil."
    "Today is the day Zygmunt and I are visiting the orphanage he grew up in after he was picked up from the streets."
    z "Is everything in order, Dobrava? The candy? The toys? The blankets? Did we forget anything?"
    $ dmood = 'happy'
    d "We've got everything, Zygmunt. Don't worry so much! Now knock on the door, my arms are getting tired from carrying all this stuff!"
    "Zygmunt knocks on the door reluctantly at first and more firmly the second time. The door opens and the sight of a tired-looking middle-aged woman greets us."
    $ zmood = 'happy'
    z "Slava. It's me, Zygmunt."
    "The woman looks at us surprised."
    "Slava" "Zygmunt! What are you doing here, my child! You never visit us!"
    $ zmood = 'neutral'
    z "I... figured I'd like to change that. I hope we are not intruding."
    "Slava" "Of course not! You're always welcome here. Come in!"
    "We enter the building and are quickly surrounded by thin but happy-looking children."
    "Boy" "Ohh, it's the bard from the tavern. Tell us a story!"
    "Girl" "Sing us a song!"
    d "One at a time! Gods, I'm so popular!"
    "I look at Zygmunt who looks like he'd rather talk to the staff than play with the children."
    d "Go on! I'm good here!"
    z "Are you sure?"
    d "Of course! Just come back later to play with us!"
    "Boy" "Promise to play with us!"
    "Girl" "Promise, promise!"
    z "Okay, I promise to play with you later."
    "Boy" "Yay!"
    hide zygmunt with dissolve
    d "Now sit down and listen to the story I have for us. Long ago in a land far far away there was..."
    "An hour passes as I entertain the children when Zygmunt returns. He looks more like his usual, confident self. Gone is the uncertainty."
    $ zmood = 'happy'
    show zygmunt at left with dissolve
    z "Now, children, you've bothered the bard enough. Let's play!"
    "Girl" "Let's play hide and seek."
    z "Alright, hide and seek it is then."
    "Boy" "You're it!"
    "Zygmunt plays hide and seek with the children. I see he has a lot of fun. I take some time to rest, then I join them too. Another hour passes before we realise it."
    z "It was fun, but we have to go."
    "Boy" "Nooo!"
    "Girl" "Please come play with us again!"
    z "I will, don't worry!"
    "We leave the orphanage."

    $ zmood = 'neutral'
    $ dmood = 'neutral'
    scene forest path
    show zygmunt at left
    show dobrava at right
    with fade

    "We walk back to the tavern. Zygmunt is deep in thought but at once he stops and looks at me."
    z "I'd like to have children too, Dobrava."
    $ dmood = 'surprised'
    d "Wha-?!"
    z "At least four. Two from us and two adopted."
    d "But... we're adventurers, Zygmunt. Who's going to take care of the children while we adventure?"
    z "We don't have to be adventurers forever."
    $ zmood = 'sad'
    z "Please... I want to be a father more than I want to be an adventurer. I want to give children the home I never had."
    d "It's just... so sudden, Zygmunt. Please give me some time to think about it."
    $ zmood = 'neutral'
    $ dmood = 'neutral'
    "I had thought about having children before... with the right person. I think I know my answer to his plea. But I need some time to come to terms with the changes my answer will bring."
    $ zmood = 'sappy'
    $ dmooe = 'shy'
    "Most importantly though, we are happy and Zygmunt has found his dream too."
    scene black with Fade(0.75, 0.0, 0.0)
    "Zygmunt's Romance End"
    return

label bogdanLove_end:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Song of Glass (main title).ogg" fadein 1.0 loop
    $ bmood = 'happy'
    $ dmood = 'angry'
    scene tavern
    show yarlomila at farleft
    show andia at leftish
    show zygmunt at center
    show bogdan at right
    show dobrava at farright
    with fade

    b "And then I took a swing at the ugly bastard's face and cut his head off!"
    d "Why do you always have to tell gruesome stories while people are trying to eat?"
    $ zmood = 'happy'
    z "Uh-oh. You've made Dobrava angry."
    $ bmood = 'surprised'
    b "Oh no, Dobrava, don't be angry at me. I love you."
    $ dmood = 'neutral'
    d "I love you too, you dork. But why do you have to talk about killing people at the table?"
    "Vshebora" "Because he's my son, that's why!"
    $ bmood = 'happy'
    "A tall woman takes Bogdan in a bear hug from behind. She looks beautiful, a muscular and powerful warrior."
    $ dmood = 'surprised'
    d "You're Bogdi's mum?!"
    "Vshebora" "Yes, and you are?"
    b "Hi, mum! That's my lover, Dobrava!"
    "Vshebora" "Your what?!"
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    z "We'll excuse ourselves..."
    hide yarlomila
    hide andia
    hide zygmunt
    with dissolve
    show bogdan at left
    show dobrava at right
    with move
    "Zygmunt, Andia, and Yarlomila hurry away and Bogdan's mother sits down heavily opposite us."
    b "My life-partner!"
    if pronoun == 'she':
        "Vshebora" "Not your wife?"
    else:
        "But you're not married?"
    $ bmood = 'surprised'
    b "Ah..."
    d "It was Bogdan's and my choice not to marry. We decided we don't need-"
    "Vshebora" "To be joined in front of the gods?! Are you two crazy?! What if you die?! Your souls won't be able to find each other and join together in the afterlife!"
    d "I'm not exactly religious enough to believe..."
    "Vshebora" "Well, suit yourselves. You should at least say your vows to each other. I can be the keeper of your vows."
    "Vshebora" "Then your souls will be safe and there won't be a large ceremony... that's what you are dreading, are you not?"
    $ bmood = 'neutral'
    b "Well, yes, mum."
    d "We have many friends so we thought if we were to do a wedding, it would be very expensive and too grand and..."
    "Vshebora" "If money is the issue, I've got plenty from my adventures."
    d "No, we really don't want a large wedding ceremony."
    b "We don't."
    d "But the private vows in front of your mother sound nice, don't they, Bogdi?"
    $ bmood = 'happy'
    b "They do!"
    "Vshebora" "Argh, don't call me a mother, it makes me feel so old. I'm Vshebora."
    $ dmood = 'happy'
    d "Dobrava."
    b "Bogdi!"
    $ dmood = 'angry'
    d "We already know that!"
    $ bmood = 'neutral'
    b "Oh no, she's angry at me again!"
    $ dmood = 'happy'
    $ bmood = 'happy'
    "Vshebora laughs at our antics. We leave for the forest behind the tavern."

    $ dmood = 'shy'
    $ bmood = 'shy'
    scene forest path
    show bogdan at left
    show dobrava at right
    with fade
    "Bogdan and I take our places opposite each other and Vshebora stands next to us with her back to a tall tree."
    "We place our right hands on each other's hearts and look each other deeply in the eyes."
    "Vshebora" "In the eyes and ears of the gods, I, Vshebora, will be the witness to the vows between Dobrava and Bogdan today."
    if pronoun == 'she':
        "Vshebora" "Bogdan, blood of my blood, do you take Dobrava as your wife and swear to love her in good and bad, health and sickness, til death parts you?"
    else:
        "Vshebora" "Bogdan, blood of my blood, do you take Dobrava as your partner in marriage and swear to love them in good and bad, health and sickness, til death parts you?"
    $ bmood = 'happy'
    b "I swear."
    "Vshebora" "Dobrava, chosen of my son's heart, do you take Bogdan as your husband and swear to love him in good and bad, health and sickness, til death parts you?"
    $ dmood = 'happy'
    d "I swear."
    if pronoun == 'she':
        "Vshebora" "You are now, in the eyes and ears of the gods, husband and wife."
    else:
        "Vshebora" "You are now, in the eyes and ears of the gods, married."
    "Vshebora" "As simple as that and as your mother, I can sleep peacefully knowing that my son and his beloved won't be seperated in life or death."
    "Vshebora" "Now, who are you and what have you done to bewitch my son, Dobrava?"
    "I get the feeling that Vshebora won't be an easy one to convince I'm the right one for her son. But, hey, we are married so what can she do?"
    "I look at my new husband and smile at him happily. Bogdi smiles back. I'm so happy with him. And I will continue to be happy for the rest of my days."
    scene black with Fade(0.75, 0.0, 0.0)
    "Bogdan's Relationship Ending"
    return

label bogdanFriend_end:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Song of Glass (main title).ogg" fadein 1.0 loop
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ amood = 'neutral'
    $ zmood = 'neutral'
    $ ymood = 'neutral'
    scene marketplace
    show yarlomila at farleft
    show andia at leftish
    show zygmunt at center
    show bogdan at rightish
    show dobrava at farright

    b "I'm so nervous."
    "It's been two years since we defeated Yarlomila and cleansed her heart. Today, Bogdi is supposed to meet his mother and she's to determine whether or not we are ready to adventure with her at the border of Darkness."
    $ dmood = 'happy'
    d "Don't be. If we are not ready, it's not the end of the world. We will get another chance in two years."
    "Every two years is when Vshebora, Bogdi's mother, returns to Priporovy Forest. That's when Bogdan gets to see her and she judges our party's strength."
    "Since Yarlomila and I were not party members the last time Vshebora visited, this is the first time we are meeting her."
    "Vshebora" "My son!"
    "A beautiful, muscular warrior emerges from the crowd and hugs Bogdan tightly."
    $ bmood = 'happy'
    b "Mum!"
    "Vshebora" "And who is here with you? Zygmunt and Andia have not left you yet it seems... and are those two new additions to the party?"
    $ zmood = 'happy'
    z "Yes, Vshebora, those are Dobrava, a bard and Yarlomila, a wizardess."
    "Vshebora" "There's not enough frontliners in your party, Bogdan."
    $ zmood = 'neutral'
    z "Well, I switched to dual-wielding a shortsword and a dagger to help us with that, but..."
    a "You may be right, Vshebora."
    "Vshebora" "You should look for another warrior. But not now. Now that I'm here, it's time to judge how strong you've gotten in the past two years."

    $ bmood = 'happy'
    $ dmood = 'neutral'
    $ amood = 'neutral'
    $ zmood = 'neutral'
    $ ymood = 'neutral'
    scene forest path
    show yarlomila at farleft
    show andia at leftish
    show zygmunt at center
    show bogdan at rightish
    show dobrava at farright
    "We follow Vshebora outside of town into the forest where we find a nice clearing. She takes turns fighting all of us... and hands our butts to each of us too."
    $ bmood = 'angry'
    b "I will... defeat you mum!"
    "Bogdan is the last one and he doesn't give up easily."
    "Vshebora" "Not in a hundred years, but I'm happy to see you try!"
    "Try as he might, Bogdan can't break through her defences. Finally, unhappily, he surrenders."
    $ bmood = 'sad'
    b "I'm not strong enough..."
    "Vshebora" "You're plenty strong, all of you are."
    b "But..."
    "Vshebora" "And I believe you're strong enough to join us at the border."
    $ bmood = 'surprised'
    b "What?!"
    $ dmood = 'happy'
    $ ymood = 'happy'
    $ amood = 'happy'
    $ zmood = 'happy'
    "We all jump up and surround Vshebora, excited."
    b "Mum?! You're not joking are you?!"
    "Vshebora" "Of course I'm not!"
    $ bmood = 'happy'
    "I look at my best friend, Bogdi. Tears start to well up in the corners of his eyes."
    "Fighting alongside his mother is all he's ever wanted and I'm so happy to be with him the moment his dream comes true."
    "And I will continue to be there for him for many months to come as his dream of becoming a powerful and successful adventurer is realized."
    "Maybe we'll even defeat the Darkness that tries to devour Ostoya."
    "Who knows what the future will bring? For now, I can say I'm happy to see my best friend cry from happiness."

    scene black with Fade(0.75, 0.0, 0.0)
    "Bogdan's Friendship Ending"
    return

label andiaLove_end:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Song of Glass (main title).ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    $ amood = 'neutral'
    scene forest path
    show andia at left
    show dobrava at right
    with Fade(0.75, 0.5, 0.75)

    a "It should be somewhere around here."
    "It's been two years since we defeated Yarlomila and cleansed her heart."
    "Today, Andia and I journeyed to the place where she learned magic... to the fabled city of Krasny Ludek."
    d "Aren't you worried they won't like you revealing the location of their city to me?"
    a "No. They won't even let us find the city if they don't want you there."
    d "Maybe that's why I feel like we've been going in circles?"
    a "Maybe... they are probably discussing whether they should let you in or not as we speak."
    $ amood = 'happy'
    a "Ah, there it is!"
    $ dmood = 'surprised'
    "Suddenly we enter a clearing and are surrounded by numerous houses inside giant mushrooms."
    d "Wow! They really do live in mushrooms!"
    a "Of course they do!"
    "Gnomes run around my feet playing catch with each other. In one of the houses, a gnome housewife is hanging out freshly washed clothes from the window."
    "It's so weird seeing how normal their lives are. Those are fabled creatures and what they do in their everyday life is not at all different from the lives of us... larger folk."
    "???" "Andia! Welcome back!"
    a "Hello, Archibald!"
    "Archibald" "And who is your friend?"
    if pronoun == 'she':
        a "This is Dobrava. She's my lover."
    else:
        a "This is Dobrava. They are my lover."
    "Andia looks at me with love in her eyes and I return the gaze."
    "Archibald" "Ah... so you've finally found the one. Welcome to our humble city, chosen of Andia's heart."
    d "It's very nice to meet you."
    "Archibald" "Don't be shy, don't be shy. Does anything in particular bring you here, Andia?"
    a "Straight to the point as always, aren't you, Archibald? Well, yes, there is something. Dobrava here seems to have an affinity for light magic beyond the skills of a bard."
    if pronoun == 'she':
        a "I believe she could become a light wizard... with your and your colleague's guidance."
        "Archibald" "I see. And is Dobrava willing to stay with us for several months until her training is complete and not disclose the location of our city once she leaves?"
    else:
        a "I believe they could become a light wizard... with your and your colleague's guidance."
        "Archibald" "I see. And is Dobrava willing to stay with us for several months until their training is complete and not disclose the location of our city once they leave?"
    $ dmood = 'happy'
    d "As long as Andia's with me, it doesn't matter to me where I live."
    "Archibald" "I see, I see. Well, well, I'll be happy to teach you, if you are willing to learn."
    d "I am!"
    "Archibald" "Brilliant, let's start immediately. As you know light is..."
    "The gnome starts walking deeper into the city. I take Andia's hand and follow. In a few months time, I will be an even stronger adventurer."
    "Maybe with my affinity for light magic I will be able to banish the Darkness from those lands one day... Well, that's a tall dream, but dreaming is no sin, right?"
    "With Andia by my side I feel powerful. I feel complete. I'm happy."

    scene black with Fade(0.75, 0.0, 0.0)
    "Andia's Relationship Ending"
    return

label andiaFriend_end:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Song of Glass (main title).ogg" fadein 1.0 loop
    $ amood = 'happy'
    $ bmood = 'happy'
    $ dmood = 'happy'
    $ ymood = 'happy'
    $ zmood = 'happy'
    scene forest path

    show bogdan at farright
    show zygmunt at rightish
    show dobrava at center
    show andia at farleft

    a "And here we go!"
    "Andia throws the bridal bouquet behind her as the custom dictates. As it happens... I am the one to catch it."
    b "Ohh... lucky catch!"
    z "I wonder who the lucky individual will be!"
    "That's what I'm wondering too. While I may have caught the bouquet, there's no one in my heart at the moment."
    "At least not like in the heart of my best friend, Andia, who is the one getting married today! To none other than..."
    show andia at leftish with move
    show yarlomila at farleft with dissolve
    "Yarlomila, our rescued villainess. It's been two years since we defeated her and I successfully cleansed the evil from her heart."
    "Andia was looking for that special someone all her life. And she found her in Yarlomila."
    d "I'm so happy for you, Andia."
    "I hug my best friend, wishing her anything and everything she can dream of."
    a "I already have everything I dreamt about."
    "She looks with love at Yarlomila who returns the look."
    y "And so do I."

    scene black with Fade(0.75, 0.0, 0.0)
    "Andia's Friendship Ending"
    return

label end_guilt:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Yarlomila Theme (gentle).ogg" fadein 1.0 loop
    $ amood = 'neutral'
    $ dmood = 'sad'
    $ zmood = 'happy'
    $ bmood = 'happy'
    "I look at Yarlomila's lifeless body lying on the floor of the ruined throne room. Was it really right to take her life... was there no other way? I will never know."
    "Now she's dead and death is final, even for a necromancer."
    z "We defeated the evil necromancer!"
    b "She was strong, but we did it!"
    a "She will poison the lands with her dark magic no more."
    d "I guess we did defeat her... by killing her. But it makes me so sad."
    $ bmood = 'surprised'
    $ zmood = 'surprised'
    $ amood = 'surprised'
    b "What are you talking about, Dobrava? She imprisoned you."
    a "Is everything okay with your head?"
    d "Maybe I'm not okay... and it'll probably take me a while to be fine again."
    $ zmood = 'sad'
    $ amood = 'sad'
    $ bmood = 'sad'
    z "I see... take all the time you need, Dobrava."
    a "Well, after being locked up in a cage for a week, that's to be expected."
    d "I'm sorry, folks. I don't feel like I can do this anymore. Adventuring that is... not for a while."
    b "It's okay, Dobrava."
    z "Let's go back to the tavern."
    d "Andia, can you burn Yarlomila's body?"
    a "Of course."
    "Despite her typical reluctance to use fire magic, Andia does so without hesitation this time."
    "The flames burn, smoke rises, and soon there is nothing left of the wizardess named Yarlomila except ash."
    d "May she finally find peace..."
    "Andia scatters Yarlomila's remains on the wind and we return to the tavern."

    scene inn room with Fade(0.5, 0.75, 0.5)
    "I sleep for several days, lacking the energy to get out of bed. The rest of the party comes to visit me but I feel distant from them. The guilt of what we did is dragging me down."

    stop music fadeout 1.0
    play music2 "Quiet Moment.ogg" fadein 1.0 loop
    $ dmood = 'sad'
    $ amood = 'happy'
    $ zmood = 'happy'
    $ bmood = 'happy'
    scene tavern
    show dobrava at offscreenright
    show bogdan at farleft
    show andia at rightish
    show zygmunt at leftish
    with fade
    show dobrava at farright with move
    "One day I emerge from my hiding. But when I see them sitting around a table, smiling, laughing, as if they've never ended a person's life... I feel disgusted."
    "Can I ever get over this feeling? This guilt? This disgust I feel towards them and myself for not stopping the murder of someone who could still be saved?"
    "I don't know. I don't know if I ever will."
    scene black with Fade(0.75, 0.0, 0.0)
    "Ending 4: Living with the Guilt"
    return
