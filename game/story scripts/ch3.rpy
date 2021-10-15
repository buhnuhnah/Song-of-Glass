label ch3_s1:
    stop music2 fadeout 1.0
    play music "Russian Polka.ogg" fadein 1.0 loop
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene tavern
    show andia at farleft
    show bogdan at farright
    show zygmunt at rightish
    show dobrava at leftish
    with fade

    "It's breakfast again. All four of us sit around the table, munching on some toast with jam while the scepter's handle lies in the middle. I stare at it intently as if that would change anything."
    $ amood = 'happy'
    a "Dobrava, you're going to burn a hole into it with your stare."
    "I ignore her joke. There's one thing we haven't tried yet. The others fear it's cursed, but it doesn't seem that way."
    $ amood = 'surprised'
    $ bmood = 'surprised'
    $ zmood = 'surprised'
    "Before anyone can stop me, I move quickly and touch the handle."
    b "Dobrava!"
    z "No, don't touch it!"
    a "What are you doing?!"
    "Despite their worries, nothing bad happens. I don't feel my energy being drained or a weight on my shoulders trying to drag me down to the underworld."
    $ dmood = 'happy'
    d "Folks, calm down. It's not cursed."
    a "But you didn't know that before you touched it. Why risk it?"
    d "Hey, no risk, no fun. Have you not learned that from Zygmunt?"
    $ zmood = 'neutral'
    z "Don't drag me into this!"
    $ amood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    "I focus on the handle again. There is one weird thing about it."
    $ dmood = 'determined'
    d "I feel like it's trying to pull me somewhere. Like I should hold it in my hand and let it guide me."
    $ bmood = 'sad'
    b "So it's cursed after all."
    d "I don't think so, its energy feels clear."
    "Andia puts her hand on the handle too."
    a "Hmm... yes, the energy feels clear and light. But I don't feel it pulling me anywhere."
    d "I'm not lying!"
    a "I'm not saying you are. You might be more susceptible to this kind of energy than I am. That's why you feel the pull while I don't."
    d "Well it clearly wants me to go somewhere... should we listen to it?"
    z "Hmm... I'm curious where it'll lead us."
    $ bmood = 'happy'
    b "Adventure?"
    $ amood = 'happy'
    a "I would like to find out too."
    $ dmood = 'happy'
    d "Alright, let's go then!"
    $ zmood = 'happy'
    "With the scepter's handle in hand we leave for the place it is leading us to."
    "Wherever that is..."
    jump ch3_s2

label ch3_s2:
    stop music fadeout 1.0
    play music2 "Elven Ruin.ogg" fadein 1.0 loop
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene forest path
    show dobrava at center
    with fade

    "Everyone is abnormally quiet and on edge today. They all walk apart from each other."
    "Whom should I approach?"
menu:
    "Talk to Zygmunt":
        $ zygmunt += 5
        jump ch3_s2_zygmunt
    "Talk to Bogdan":
        $ bogdan += 5
        jump ch3_s2_bogdan
    "Talk to Andia":
        $ andia += 5
        jump ch3_s2_andia
    "Don't bother anyone":
        $ songbird += 5
        "I shouldn't bother anyone with idle chatter. If they don't want to talk, there's no point in trying to engage them in conversation."
        "It's a bit lonely to walk in silence, but we {i}are{/i} on a mission. So, we continue walking to wherever the handle is guiding me."
        jump ch3_s3

label ch3_s2_zygmunt:
    show dobrava at right with move
    show zygmunt at left with dissolve
    "I walk over to Zygmunt. He looks as if he's deep in thought, so unlike him."
    $ dmood = 'happy'
    d "Hey, Zygmunt! I was wondering..."
    z "Hmm?"
    "I try to quickly come up with a topic."
    d "...How many stable partners have you had?"
    $ zmood = 'surprised'
    "Oh no, why did I ask that? He looks at me surprised."
    d "That got your attention, didn't it?"
    "Let's cover this up. It's not like I'd really like to know or anything."
    $ zmood = 'neutral'
    z "Just one boyfriend. Or rather, fiance. We were engaged in front of the gods."
    $ dmood = 'sad'
    d "Oh..."
    "Should I ask more?"
menu:
    "Continue the conversation":
        $ zygmunt += 5
        jump ch3_s2_zygmunt2
    "Do not pry into Zygmunt's personal affairs":
        if zygmunt > 10:
            $ end_buddy = 'zygmunt'
        "We continue talking about lighter topics while we follow the handle's pull towards the unknown."
        jump ch3_s3

label ch3_s2_zygmunt2:
    d "...Why did you break up?"
    "Wait... what if they didn't break up? Is he still in a relationship?"
    if ch1s8_buddy == "zygmunt":
        "But he asked me for a kiss the other night!"
        if ch2_buddy == "zygmunt":
            if holdZygmunt:
                "And we held hands while shopping... to not get separated, but still. It counts!"
            elif ch2_thief:
                "And we stole things together - we're partners in crime. That means we're close, right?"
        if not kissZygmunt:
            "As his friend, I feel like I should know!"
    $ zmood = 'surprised'
    "Zygmunt looks at me dumbfounded, clearly shocked I'd ask such a delicate question."
    "I keep staring at him until he sighs and gives in."
    $ zmood = 'sad'
    z "He cheated on me with his childhood friend. Ever since then, I've given up on serious relationships."
    z "I sleep around to try and satisfy my need for intimacy, but of course it doesn't work."
    d "I'm sorry to hear that..."
    "How do I feel about Zygmunt?"
menu:
    "You want to be friends with Zygmunt":
        $ end_buddy = 'zygmunt'
        $ zygmunt += 5
        d "I won't say I shouldn't have asked. I consider you a friend and as such, I think I should know these things."
        z "I'm happy to be considered your friend."
        d "Of course you are, silly."
        "We continue talking about lighter topics while we follow the handle's pull towards the unknown."
        jump ch3_s3
    "You want a relationship with Zygmunt":
        $ end_friendship = False
        $ end_buddy = 'zygmunt'
        $ zygmunt += 5
        jump ch3_s2_zygmunt3

label ch3_s2_zygmunt3:
    "He continues as if he's not listening to me at all.."
    z "I've given up on relationships... but have I really?"
    d "I hope you haven't."
    "That gets his attention again."
    $ zmood = 'neutral'
    z "Why?"
    $ dmood = 'shy'
    d "Because I... I might be interested in something like that with you."
    d "I-I know it's a bit early t-to talk about things like that. We've only m-met the day before yesterday..."
    $ zmood = 'sappy'
    z "You're stuttering. How cute."
    d "It's not cute!"
    z "It is! It's true we only met a couple of days ago, but so much has happened since then. And I feel an irresistible pull towards you too."
    "He stops walking and I stop too. He bends down a bit to put his face at the same height as mine."
    z "See? Something's pulling me towards you."
    "And he kisses me firmly on the lips. The kiss quickly turns passionate and we get lost in each other's taste."
    "We are interrupted by the sounds of clapping and cat-calling. I push Zygmunt away and he pouts."

    $ dmood = 'surprised'
    $ zmood = 'happy'
    $ bmood = 'happy'
    $ amood = 'happy'
    show dobrava at farright
    show zygmunt at rightish
    with move
    show bogdan at leftish
    show andia at farleft
    with dissolve

    b "Woohoo! Don't mind us. Keep going!"
    a "I knew this was bound to happen. Congratulations."
    d "It's too early to-"
    z "Well, thank you."
    "Zygmunt takes one step ahead of me then turns around and offers his hand to me, bowing slightly."
    $ dmood = 'happy'
    if pronoun == 'she':
        z "Would {i}m'lady{/i} allow me to court her?"
    else:
        z "Would you allow me to court you?"
    "This is embarrassing but makes me giddy with joy too even though his tone is mocking and I know he is not serious. All this means is that we want to try being exclusive. I take his hand in my own."
    d "Yes, I would."
    "We continue talking about lighter topics while we follow the handle's pull towards the unknown."
    jump ch3_s3

label ch3_s2_bogdan:
    show dobrava at right with move
    show bogdan at left with dissolve

    "I walk over to Bogdan. He looks as if he's deep in thought. Very unlike him."
    $ dmood = 'happy'
    d "Hey, Bogdan! I was wondering..."
    b "Hmm?"
    "I try to quickly come up with a topic."
    d "...How many stable partners have you had?"
    $ bmood = 'surprised'
    "Oh no, why did I ask that? He looks at me surprised."
    d "That got your attention, didn't it?"
    "Let's cover this up. It's not like I'd really like to know or anything."
    $ bmood = 'neutral'
    b "Honestly... I've never had one. A partner that is."
    $ dmood = 'surprised'
    d "Oh..."
    "Well, that's unexpected. As handsome as he is, I thought for sure there would have been someone."
    $ bmood = 'happy'
    b "What? Are you asking me to court you?"
    "Court me? As in being committed to each other?"
    "How do I feel about Bogdan?"
menu:
    "You want to be friends with Bogdan":
        $ end_buddy = 'bogdan'
        $ bogdan += 5
        $ dmood = 'happy'
        d "Good joke, friend!"
        b "Ha, I thought that'd get you at least a little bit flustered!"
        d "In your dreams, Bogdi!"
        "We continue talking about lighter topics as we follow the handle's pull towards the unknown."
        jump ch3_s3
    "You want to be in a relationship with Bogdan":
        $ end_friendship = False
        $ end_buddy = 'bogdan'
        $ bogdan += 5
        jump ch3_s2_bogdan2
    "You don't care about Bogdan in any way":
        $ songbird += 5
        d "Ha, good joke!"
        $ bmood = 'sad'
        b "I wasn't joking..."
        d "Well, I don't care. It's funny to me."
        "Bogdan looks sad, but I really don't care. I separate from Bogdan and continue walking alone."
        jump ch3_s3

label ch3_s2_bogdan2:
    $ dmood = 'shy'
    d "What if I am asking you to court me...?"
    $ bmood = 'surprised'
    b "What?!"
    "He gapes at me, his eyes filled with surprise."
    d "You didn't expect that, did you? It's stupid, I know. We've only known each other for a few days..."
    $ bmood = 'angry'
    b "It's not stupid! I just...!"
    $ bmood = 'shy'
    b "I never expected someone like you would want to be with someone like me..."
    $ dmood = 'surprised'
    d "What do you mean, \"someone like me\"?"
    b "You're smart, confident, and outgoing, and so pretty... and I'm..."
    $ dmood = 'happy'
    d "Strong, protective, and kind. And let's not forget handsome, too."
    b "...Is that really how you see me?"
    $ dmood = 'shy'
    d "...Yes."
    "Bogdan takes a step closer to me and puts his face on level with mine."
    b "Is it fine if I kiss you, then?"
    d "...Yes."
    "He gently takes my face in his calloused hands and kisses me on the lips. We kiss each other for a while, before we deepen the kiss. He tastes surprisingly fresh, like mint."

    $ dmood = 'surprised'
    $ bmood = 'surprised'
    $ amood = 'happy'
    $ zmood = 'happy'
    show dobrava at farright
    show bogdan at rightish
    with move
    show andia at farleft
    show zygmunt at leftish
    with dissolve

    "We are interrupted by the sound of clapping from the direction we were walking in."
    a "I knew this was bound to happen. Congratulations."
    z "You go man! You couldn't have picked better!"
    $ bmood = 'shy'
    $ dmood = 'shy'
    b "...Thank you."
    "Bogdan takes my hand in his and smiles softly. I smile back at him and we walk hand in hand, joining the others."
    jump ch3_s3

label ch3_s2_andia:
    show dobrava at right with move
    show andia at left with dissolve
    "I walk over to Andia. She looks as if she's deep in thought."
    $ dmood = 'happy'
    d "Hey, Andia! I was wondering..."
    a "Hmm?"
    "I try to quickly come up with a topic."
    d "...How many stable partners have you had?"
    $ amood = 'surprised'
    "Oh no, why did I ask that? She looks at me surprised."
    d "That got your attention, didn't it?"
    "Let's cover this up. It's not like I'd really like to know or anything."
    $ amood = 'sad'
    a "It's cruel to ask me something like that when I've told you how serious I am about relationships..."
    a "I've never been in one. I guess I've never found the right girl..."
    $ dmood = 'surprised'
    d "Oh..."
    "How do I feel about Andia?"
menu:
    "You want to be friends with Andia":
        $ end_buddy = 'andia'
        $ andia += 5
        $ dmood = 'happy'
        d "Andia, I consider you a dear friend. I'll cheer you on when you finally find your special someone!"
        $ amood = 'happy'
        a "Thank you, Dobrava. I also see you as a precious friend. And I hope I meet that person someday soon."
        "We continue talking about lighter topics as we follow the handle's pull towards the unknown."
        jump ch3_s3
    "You want to be in a relationship with Andia":
        $ end_friendship = False
        $ end_buddy = 'andia'
        $ andia += 5
        jump ch3_s2_andia2

label ch3_s2_andia2:
    $ dmood = 'determined'
    d "Andia, I was serious when I asked you this question. I... I know we've only known each other for a couple of days, but..."
    $ dmood = 'shy'
    d "I really, really like you!"
    $ amood = 'surprised'
    a "Oh!"
    d "And not just as a friend, but as something more!"
    if pronoun == 'she':
        "Andia looks at me wide eyed and my heart drops. What if she doesn't like girls? What if she doesn't like me?"
    else:
        "Andia looks at me wide eyed and my heart drops. What if she doesn't like me?"
    $ amood = 'shy'
    a "Dobrava, I... I feel the same way about you."
    "Wait... really?!"
    $ dmood = 'happy'
    d "Oh, gods, I'm so glad!"
    "I jump closer to Andia and hug her tightly. I lean in to kiss her and she kisses me back sweetly."

    $ dmood = 'surprised'
    $ amood = 'surprised'
    $ bmood = 'happy'
    $ zmood = 'happy'
    show dobrava at farright
    show andia at rightish
    with move
    show bogdan at farleft
    show zygmunt at leftish
    with dissolve

    "We are interrupted by the sounds of clapping and cat-calling from the direction we were walking in."
    b "Woohoo! Don't mind us. Keep going!"
    z "Go Andia, go! You couldn't have picked better!"
    "I take Andia's hand in mine and we smile softly at each other. We walk hand in hand, joining the others."
    jump ch3_s3

label ch3_s3:
    stop music2 fadeout 1.0
    play music "combat music (level 2).ogg" fadein 1.0 loop

    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    scene ruins with fade

    if end_buddy == 'andia':
        show bogdan at farleft
        show andia at leftish
        show dobrava at rightish
        show zygmunt at farright
        with None
    elif end_buddy == 'bogdan':
        show bogdan at leftish
        show andia at farleft
        show dobrava at rightish
        show zygmunt at farright
        with None
    else:
        show andia at farleft
        show bogdan at farright
        show dobrava at leftish
        show zygmunt at rightish
        with None

    "Eventually, we reach another Elven ruin. We explore the various chambers fighting skeletons. I buff the party and everything goes smoothly."
    "In the ruin's final room is a skeleton with a giant sword guarding a chest."
    d "The handle is pulling towards the chest."
    $ bmood = 'happy'
    b "Then let's fight this thing!"
    "We engage the skeleton in combat. I buff the party but the skeleton is a strong opponent, its bones sturdy and well-connected."
    play sound "A Song of Healing.ogg"
    "At one point, the skeleton injures Bogdan and I play the song of healing. Bogdan's wound closes."
    b "Thank you, Dobrava! Now let's finish this!"
    "With a final swing of his sword, Bogdan destroys the skeleton. Its bones shatter on the ground. Bogdan approaches the chest-"
    $ zmood = 'surprised'
    z "Wait, let me check for traps!"
    $ zmood = 'neutral'
    "Bogdan stops with his hand still in the air. Zygmunt approaches the chest and pokes at it with his thieves' tools."
    $ zmood = 'happy'
    z "A-ha! There was a trap! And... now it's disarmed!"
    "Disarming traps is just like Andia's magic: completely over my head. But I trust Zygmunt if he says it's safe."
    d "Open it."
    "Zygmunt opens the chest with a look of anticipation, but his expression quickly changes to one of disappointment."
    $ zmood = 'sad'
    stop music fadeout 1.0
    play music2 "Elven Ruin.ogg" fadein 1.0 loop
    z "What is this trash?!"
    "I look over his shoulder. What looks like another part of the scepter's handle lies inside, but the indent where a jewel would sit is empty. It's adorned with Elven markings."
    "I feel a sense of accomplishment for finding this, but the feeling is not my own. The handle, somehow, looks incredibly pleased with itself"
    d "This is it. This is what the handle wanted me to find."
    $ zmood = 'angry'
    z "But this is just a piece of trash!"
    $ amood = 'annoyed'
    a "Don't be rash and jump to conclusions. It has the same markings as the other part. If we put them together, we only need to find the jewel and the scepter will be complete."
    $ bmood = 'neutral'
    $ zmood = 'neutral'
    b "And then what?"
    $ amood = 'neutral'
    a "That's a good question. I hope the Elven language on this piece will bring us closer to determining the scepter's purpose. "
    $ dmood = 'happy'
    d "Fingers crossed."
    z "There's a pouch with a handful of ancient Elven coins too. That should pay for a week's room and board. At least if the scepter turns out to be a dud this excursion wasn't {i}entirely{/i} pointless."
    $ dmood = 'neutral'
    d "Don't say that. It's never pointless to adventure together."
    $ bmood = 'happy'
    b "I agree with Dobrava. Adventuring is all that matters."
    $ amood = 'happy'
    a "And gaining knowledge."
    $ zmood = 'happy'
    z "You folks are hopeless. Am I the only one who worries about getting enough money to eat and sleep?"
    "We laugh at that. Taking the new part of the scepter in hand, we try to fit it together with the one we already had. It fits without a problem."
    "Andia packs it in her pouch and we start our trip back to the tavern."
    jump ch3_s4

label ch3_s4:
    stop music2 fadeout 1.0
    play music "mazurka (accompanied).ogg" fadein 1.0 loop
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    scene forest path with fade

    if end_buddy == 'andia':
        show bogdan at farleft
        show andia at leftish
        show dobrava at rightish
        show zygmunt at farright
        with None
    elif end_buddy == 'bogdan':
        show bogdan at leftish
        show andia at farleft
        show dobrava at rightish
        show zygmunt at farright
        with None
    else:
        show bogdan at farright
        show andia at farleft
        show dobrava at leftish
        show zygmunt at rightish
        with None

    d "I can't help but wonder why the scepter wants us to gather all of its parts."
    a "I guess every item wants to be complete. There is beauty in completeness."
    z "Academic bullshit. I agree with Dobrava - it feels fishy."
    $ bmood = 'happy'
    b "Are we having fish for dinner today? I like fish!"
    "Zygmunt facepalms. Andia and I snicker."
    $ dmood = 'happy'
    d "If it's available at the tavern, why not?"
    "We continue our conversation while continuing towards the tavern. We are all in high spirits, albeit tired."
    "I can't help but feel like something bad is going to happen, but I don't know what. How do I stop something like that?"
    stop music fadeout 1.0
    play music2 "Guardian of the Forest.ogg" fadein 1.0 loop
    "Leshy" "You can't stop fate."
    $ amood = 'surprised'
    $ bmood = 'surprised'
    $ dmood = 'surprised'
    $ zmood = 'surprised'
    "We all stop walking. Suddenly in the forest to the left there is a figure where none was before."
    a "Leshy! Guardian of the Forest!"
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    "We all bow in reverence of the figure of wisdom and the protector of everything living in the forests of Ostoya."
    z "To what do we owe the pleasure, Ancient One?"
    "Leshy" "You are in possession of the Scepter of Light. You should collect the last piece. It has chosen you to defeat it's archenemy."
    $ dmood = 'surprised'
    d "We were chosen?"
    "Leshy" "Yes, you were. Some time ago, a wizardess named Yarlomila turned away from the light. She experimented with death and sacrificed many in search of immortality."
    $ dmood = 'neutral'
    "Leshy" "But all she found was sadness and loneliness. Now she seeks revenge on the world for making her an outcast. She creates undead and uses them to harm the people of Ostoya."
    "Leshy" "Only the Scepter of Light can stop her."
    z "Thank you, Ancient One for setting us on this quest. We will defeat the evil wizardess."
    b "You can count on us. We are capable warriors."
    a "May your knowledge guide us."
    d "..."
    "Wait... Leshy said this wizardess is doing those things because she is sad and lonely. Maybe she can be reasoned with. Why is everyone so quick to attack her?"
    "Leshy" "May the blessings of the forest light your path."
    "We all thank Leshy for their blessing. Then, in the same manner they appeared out of nowhere, between one blink of our eyes and the other, they disappear from sight."
    $ dmood = 'sad'
    stop music2 fadeout 1.0
    play music "kujawiak (accompanied).ogg" fadein 1.0 loop
    d "I can't help but feel sad for this wizardess..."
    $ bmood = 'surprised'
    $ amood = 'surprised'
    $ zmood = 'surprised'
    b "What?"
    a "What do you mean, Dobrava?"
    $ amood = 'annoyed'
    $ zmood = 'neutral'
    $ bmood = 'neutral'
    a "You are aware that the undead we've been fighting the past few days were likely created by this Yarlomila?"
    $ dmood = 'surprised'
    d "That's... probably true. So she's out to destroy Priporovy Forest and the people living near it?"
    $ amood = 'neutral'
    a "That would be my guess."
    $ zmood = 'surprised'
    z "She is an evil necromancer, Dobrava. She must be defeated! If she isn't, think of the harm and destruction she could cause!"
    $ dmood = 'sad'
    d "Well, yes, I know she must be stopped one way or another. But maybe we could try talking with her?"
    $ zmood = 'neutral'
    "They all look at each other. Finally Zygmunt sighs."
    z "You're too kind, Dobrava... Very well, we will try talking to her before we engage in a fight."
    $ dmood = 'neutral'
    d "Thank you, that's all I ask."
    "I feel a bit better with the reassurance that we won't fight without reason. We continue on the road to the tavern."
    jump ch3_s5

label ch3_s5:
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    scene tavern with fade
    "Upon reaching the tavern we are dead tired, so after eating dinner we decide to call it a day."
    scene inn room with fade
    "I can't help but think of the evil wizardess Yarlomila, but I'm ready to fall asleep as soon as my head hits the pillow."
    "Too much has happened in the past few days and I'm not used to the stress. I hope my companions can be talked into having a day off tomorrow."
    "I give in to my tiredness."

    scene throne room
    show dobrava at center
    with Fade(0.5, 0.5, 0.5)
    stop music fadeout 1.0
    play music2 "dark magic music (level 3).ogg" fadein 1.0 loop
    "I'm in the same glass castle as I was the previous two nights. Without delay, I make my way to the throne room to meet the beautiful woman. Maybe tonight I can engage her in a proper conversation."
    "The only thing that changed in the throne room is the fact that there is now a large golden birdcage in there."
    "I briefly wonder what kind of bird such a large cage could be for? I can only think of the mythical phoenix."
    $ ymood = 'neutral'
    show dobrava at right with move
    show yarlomila at left with dissolve
    "I focus on the woman's expression as I approach her. She looks so sad and lonely. I can't leave her like this!"
    "I come closer to the throne than ever and stand in front of the woman."
menu:
    "Take her hand":
        "Without hesitation, I take her hand in mine."
        jump ch3_s5_2
    "Try speaking to her":
        $ dmood = 'sad'
        d "Why do you look so lonely?"
        "She doesn't reply but instead grabs my hand."
        jump ch3_s5_2
    "Do nothing":
        "We stare each other in the eyes for a moment before she grabs my hand."
        jump ch3_s5_2

label ch3_s5_2:
    $ ymood = 'smirk'
    "She smiles her creepy smile which doesn't reach her eyes. Her hand is very cold, but I don't pull away. Maybe I can have some sort of connection with her this way? Reach her?"
    $ dmood = 'surprised'
    "Before I know it, she teleports to the cage and pushes me inside. The door closes behind me with a loud bang and the lock clicks. The woman laughs."
    stop music2 fadeout 1.0
    play music "Yarlomila Theme (main).ogg" fadein 1.0 loop
    "???" "My precious Songbird. Now you are mine."
    d "What are you doing?! Who are you?!"
    y "They call me Yarlomila."
    d "The necromancer?!"
    y "The very same."
    "The one Leshy told us about! The evil wizardess!"
    $ dmood = 'angry'
    d "Let me out!"
    y "I have no intention to."
    d "I want to wake up!"
    "I pinch myself but nothing happens."
    y "Oh, do you think this is a dream? It is not. You are in my domain."
    d "What? Where are we?"
    y "Somewhere we will never be found."
    d "That's not true! My friends will come for me!"
    y "Oh, they can try. But they can't reach this place."
    y "Now sing for me, Songbird."
    d "What? No way! I won't!"
    y "One day you will."
    "I look past Yarlomila, averting her gaze. I'm angry at her. I notice a glowing object on the throne. A yellow jewel is there, shining brightly."
    "I feel a sense of familiarity from this object. Is that the last piece of the scepter? Then, maybe the pull can direct the party to me... but wasn't I the only one who felt the pull?!"
    "Ahh... this is so complicated. How did it come to this?!"
    "Nevermind, the \"how\" isn't as important as the \"what next?\". Right now, I have to focus on my survival and hope for the best."
    "But Yarlomila? She makes me so angry. Who in their right mind would imprison another person in a birdcage and call them a songbird?! Despicable."
    jump ch4_s1
