label ch1_s1:
    scene tavern

    "Customer Man" "Dobrava, tell us a story about a hero!"
    show dobrava at center with dissolve
    "I look at the crowd gathered around me. As any other bard, I enjoy the attention. And I have many stories to tell, oh I do."
    "A hero they say? They probably expect a story about someone who slew a dragon or any other monsters. But what about someone who saved a Princess because he was a good man who had made friends?"
    "Let's see if they like it as much as I do."
    $ dmood = "happy"
    d "The Shoemaker Dratevka was a poor man, who travelled around Ostoya and fixed people's shoes and helped everyone in need."
    $ dmood = "neutral"
    d "Once, Dratevka came across an ant hill destroyed by a bear. He fixed it and the ants thanked him."
    d "Another time, he found a destroyed beehive and helped the bees fix it."
    d "Yet another time, he encountered ducks who were hungry and fed them some bread. The ducks thanked him."
    "I pause and play a happy tune on the flute to make the show even better. The people look at me with happy faces. There is a group of adventurers at one of the tables. They stop talking and look at me expectantly."
    $ dmood = "determined"
    d "One day he came across a tower in the woods. In it, a Princess was imprisoned by an evil Witch. The Witch told Dratevka she would release the Princess if he completes two tasks for her and solves a riddle."
    "I pause again to play something dramatic."
    d "And so, Dratevka was tasked with picking poppy seeds out of a sack of sand by the morning."
    "Another pause and another tune on the flute."
    "Customer Child" "Oh, no!"
    $ dmood = "sad"
    d "He felt desperate. How was he supposed to complete such a task in such a short period of time?"
    $ dmood = "happy"
    d "Then his friends came to the rescue - the ants! They completed the task for him and when the Witch came to see the result in the morning, everything was sorted in neat piles."
    "I play a victorious tune and the crowd cheers. The adventurers get up from their seats and come to watch closer."
    "There are two men, both very handsome, and a beautiful woman. I try not to be distracted. I am working, gods damn it, don't flash your stupid gorgeous faces in front of me!"
    $ dmood = "determined"
    d "The Witch then tasked Dratevka to find a golden key in the lake. How was he supposed to find a small key at the bottom of a giant pool of water?"
    $ dmood = "happy"
    d "But his friends, the ducks, came to help!"
    "Customer Child" "Awesome!"
    $ dmood = "determined"
    d "And so only the last test stood before Dratevka - the riddle. The Witch led him to a room, where nine maidens sat. All of them wore the same clothes and their faces were hidden under veils."
    d "The Witch told him \"Now find your Princess!\" and cackled."
    "I make another dramatic pause to play my flute. The crowd is focused on me. I enjoy their attention."
    "Customer Man" "Oh no! How will he be able to do that? He can't tell them apart!"
    $ dmood = "happy"
    d "And again, Dratevka's friends, the bees, came to the rescue. They flew through the window and circled the head of one of the maidens. Trusting his friends, Dratevka chose her."
    d "The Witch, defeated, transformed into a bird and flew away. And the Princess, grateful to be saved, embraced Dratevka."
    d "Then they married and lived happily ever after in the witch's castle."
    "I end my story with a victorious tune. I really love this one and the crowd does too. I wish I had friends like Dratevka. Trust and camaraderie is invaluable."
    "The crowd claps and cheers. Money gets thrown on the coat I had spread under my feet."
    "Customer Man" "Tell us another story, Dobrava!"
    "Customer Child" "Yes, one more! One more!"
    d "I'm very sorry, but I need to take a break now. All this storytelling and playing got me hungry."
    "Innkeeper Marysia" "I'll get some food ready for you."
    "Marysia the innkeeper feeds me for free. After all, thanks to me, customers come to the tavern and stay here longer. There is no one in Ostoya who does not like a good song and story."
    "And I'm the very best at what I do."
    "Customer Child" "Oh nooo! I want to hear another story!"
    "Customer Man" "Later, my son. Let the bard rest. It's well-deserved after such a beautiful performance."
    jump ch1_s2

label ch1_s2:
    "The crowd disperses, returning to their now cold meals. I look down at my flute and start to clean it."
    "???" "Bard... your name is Dobrava, right?"
    $ dmood = "surprised"
    $ zmood = "neutral"
    show dobrava at farright with move
    show zygmunt at rightish with dissolve
    "I look up again, surprised. The pretty adventurers are still gathered around me."
    d "...! Yes, that's right. I'm Dobrava."
    $ dmood = "neutral"
    "There's a handsome half-elven man with two daggers at his hips. Must be some kind of rogue."
    show bogdan at leftish behind zygmunt with dissolve
    "Another beautiful man, this one a human in full armor, stands to his left. Some sort of fighter, probably."
    show andia at farleft with dissolve
    "And a gorgeous elven lady with a stern expression stands slightly behind them. A pointy, wide-brimmed hat gives her away as some sort of mage."
    $ dmood = "shy"
    "Ohhh quit staring, Dobrava. So what if you suddenly got approached by so many pretty faces? And bodies? You're not too shabby-looking yourself, after all..."
    $ dmood = "happy"
    d "How can I help you, handsome?"
    "Yes, let's approach this in the usual manner!"
    $ zmood = "surprised"
    z "...Ha, I see you are a lady made of the same clay as I am. My name is Zygmunt."

menu:
    "Correct that you are not a lady":
        $ pronoun = "they"
        d "Not a lady, but nice to meet you too."
        z "Ah, I meant no offence."
        d "I know. Thus none was taken."
        jump ch1_s2_2
    "Thank him for calling you a lady":
        $ pronoun = "she"
        d "I appreciate you recognizing me as a lady."
        "Innkeeper Marysia" "You were not much of a lady that one time when you..."
        $ dmood = "shy"
        d "Quiet, Marysia! I told you not to speak about it! Especially not in front of strangers..."
        $ zmood = "happy"
        "Zygmunt laughs openly at that and the other man chuckles too. The elven woman looks like she does not want to be part of this conversation, cringing visibly."
        jump ch1_s2_2

label ch1_s2_2:
    $ dmood = "neutral"
    $ zmood = "neutral"
    "I look at the other members of the party expectantly."
    b "Ahh... my name is Bogdan. I stab things for a living."
    $ amood = "annoyed"
    a "A very eloquent way to introduce yourself, Bogdan. I applaud your creativity. I'm Andia."
    $ dmood = "happy"
    d "Are you the kind of wizard who blows things up?"
    a "Gods forbid, I am not. My element is more subtle than that. I work with wind."
    $ zmood = "happy"
    z "And I also stab things for a living as well as try to talk them out of their clothes."
    d "You are a man of words, truly."
    "They seem like nice folks. But what do they want with me?"
    d "So... what brings you to me? Did you like the story? My playing? Or just my looks?"
    z "All of it, of course! As you can see we are a party of three adventurers: a frontline fighter, a stealthy rogue, and a powerful wizard. What is missing in our lives then?"
    $ bmood = "surprised"
    b "...Money?"
    a "Gods, help us!"
    z "Well, that too. But I wasn't asking you, I was asking Dobrava. What do you think?"
    "What do I think they are missing?"

menu:
    "Powerful magical items":
        $ bogdan += 5
        $ dmood = "neutral"
        d "You don't seem to be very well-equipped."
        $ bmood = "sad"
        b "My sword is good for stabbing people!"
        $ zmood = "happy"
        z "Yes, I am sure of that... after thte last maiden who ran away after spending a night with you."
        $ bmood = "surprised"
        b "But that's not what I meant at all!"
        $ zmood = "neutral"
        z "But yes, we are indeed missing magical items. Though that's not why we approached you."
        jump ch1_s2_3
    "Fame":
        $ zygmunt += 5
        $ dmood = "neutral"
        d "This is the first time I saw you around here. Are you a new group? Not famous yet?"
        $ zmood = "sad"
        z "It pains my heart, you've never heard of us: The... what are we called again?"
        a "I'd rather not be called anything as a group than go by a cringy name you come up with."
        z "You wound me. But it's true, my sense of naming is terrible. Maybe Dobrava could help us later."
        $ zmood = "happy"
        z "But that's not why we approached you."
        jump ch1_s2_3
    "Knowledge":
        $ andia += 5
        $ dmood = "neutral"
        d "Are you seeking knowledge? I know any stories about the heroes and villains of these lands."
        $ amood = "neutral"
        a "And I am very interested in learning everything you know. Are you familiar with..."
        $ zmood = "neutral"
        z "Now now, Andia!"
        a "But..."
        z "When Andia starts, she won't leave you be. And while I appreciate your knowledge, that's not why we approached you."
        jump ch1_s2_3

label ch1_s2_3:
    $ dmood = "neutral"
    d "Then why did you?"
    $ zmood = "neutral"
    z "Do you know any healing spells?"
    d "...Yes, of course. Healing songs were part of my training as a bard and I'm knowledgeable about herbalism and alchemy as well as first aid."
    $ zmood = "happy"
    z "See! Told you she knows her stuff!"
    $ bmood = "happy"
    if pronoun == "they":
        b "They seem very capable indeed!"
    else:
        b "She seems very capable indeed!"
    $ amood = "neutral"
    a "Reluctant as I am to agree with you on anything, I must admit you are right this time."
    z "A rare occasion!"
    d "I still don't understand. What do healing spells have to do with you approaching me?"
    z "Well of course I want you to join us!"
    $ dmood = "surprised"
    d "Join... you...?"
    a "Yes, as the party's healer. An adventurer."
    z "Life as a bard may be nice, but are you interested in trying something more action-oriented?"
    d "I..."
    b "...In watching us stab monsters and having a new story to tell and sing about?"
    d "Well..."
    a "...In travelling the land with us and gathering ancient knowledge and uncovering forgotten lore?"
    d "..."
    "Am I? I was trained with the possibility of being an adventuring bard, rather than one who always sits in the same tavern, telling stories and singing songs for anyone who wanted to listen."
    "But... fighting actual monsters rather than singing about them? Is that something I can do?"
    a "...You're not afraid, are you?"
    $ bmood = "sad"
    b "Maybe she just doesn't like us..."
    $ zmood = "neutral"
    z "Hush, let her think."
    "Even if I was scared, I would never admit that to their beautiful faces!"
    $ dmood = "happy"
    d "Who? Me? Scared? What do you take me for?! Of course I'm not afraid! What would I be afraid of? After all, I would be with brave adventurers who will protect me!"
    d "I'll do it!"
    "...What?"
    "Did I just... agree to join them?"
    $ zmood = "happy"
    z "Brilliant!"
    $ amood = "happy"
    a "Happy to have you with us!"
    $ bmood = "happy"
    b "Yay! Now I can actually be in less pain after being bitten by a monster!"
    "...What have I done?!"
    z "Welcome to the party, Dobrava! I hope our time together will bring us many riches, glory, and knowledge! As well as many stories for you to tell!"
    $ dmood = "neutral"
    d "...yes, thank you."
    jump ch1_s3

label ch1_s3:
    scene tavern
    show bogdan at leftish
    show andia at farleft
    show zygmunt at rightish
    show dobrava at farright
    with fade

    "After eating dinner with my new adventuring party, the time comes - my first quest. There's a first time for everything, I guess."
    $ amood = "neutral"
    a "There's this Elven ruin nearby I'm interested in. It's about 500 years old, from before the time-"
    $ zmood = "happy"
    $ amood = "annoyed"
    z "And we are sure to find some treasure in here!"
    $ bmood = "happy"
    b "And monsters to stab!"
    $ menuset = set()
menu:
    set menuset
    "Ask about the history of the ruin":
        jump ch1_s3_2
    "Ask about the plentiful treasure":
        jump ch1_s3_3
    "Ask about the scary monsters":
        jump ch1_s3_4

label ch1_s3_2:
    $ menuset.add("Ask about the history of the ruin")
    $ dmood = "neutral"
    d "Please tell us more about the history of the ruin, Andia."
    $ amood = "happy"
    a "Finally someone interested in more than just riches and combat. Very well. As you know, Dobrava, Ostoya was the land of elves, called Eduan."
    a "That was before the Darkness came and swallowed the whole continent, making vast areas of it unlivable. The Elves could not stand living among the shorter-living races and most of them left for the New Land and Kingdoms of the Sun and Moon."
    a "But their ruins remained. Many still hold secrets behind locked doors as few people these days can read the ancient Elven tongue."
    d "Do you know the Elven tongue, Andia?"
    $ amood = "neutral"
    a "I would not call myself an expert on it, but I can read and understand many of the words."
    a "I'm not as good at speaking and writing it as I rarely have the chance to use those skills as an adventurer."
    $ amood = "happy"
    a "But if there is a riddle to solve or a magic barrier which requires a key word to open, I think I'll be able to figure it out. I've done so in the past."
    a "I'm great at finding the right answers."
    $ bmood = "happy"
    b "And if Andia is wrong, then many monsters come out which is good too!"
    $ zmood = "happy"
    z "There is never a wrong answer, since we get gold out of it either way!"
    $ amood = "annoyed"
    a "Monsters and gold, that's all they care about. I'm happy to finally have someone interested in history and lore on the team."
    $ dmood = "happy"
    d "I'm always happy to talk and learn more!"
menu:
    set menuset
    "Ask about the history of the ruin":
        jump ch1_s3_2
    "Ask about the plentiful treasure":
        jump ch1_s3_3
    "Ask about the scary monsters":
        jump ch1_s3_4
jump ch1_s3_5

label ch1_s3_3:
    $ menuset.add("Ask about the plentiful treasure")
    $ dmood = "neutral"
    d "This treasure you are talking about-what could it be?"
    $ zmood = "happy"
    z "Anything related to Elves that withstood the passage of time. Weapons, amulets, jewels, ancient coins..."
    $ amood = "happy"
    a "Books!"
    d "I don't think any books would be left in a damp ruin after 500 years..."
    a "Ah, but they could if the cabinet they were stored in was magically preserved!"
    $ zmood = "neutral"
    z "What are the chances of that?"
    $ amood = "sad"
    a "...Very low."
menu:
    set menuset
    "Ask about the history of the ruin":
        jump ch1_s3_2
    "Ask about the plentiful treasure":
        jump ch1_s3_3
    "Ask about the scary monsters":
        jump ch1_s3_4
jump ch1_s3_5

label ch1_s3_4:
    $ menuset.add("Ask about the scary monsters")
    $ dmood = "neutral"
    d "What kind of monsters can we expect, Bogdan?"
    $ bmood = "happy"
    b "Hopefully the type that dies when it is killed!"
    d "There are monsters that don't die when you stab them?"
    $ bmood = "neutral"
    b "Yes, plenty of those! Undead, slimes..."
    $ zmood = "happy"
    z "Giant spiders!"
    $ bmood = "angry"
    b "Hey! That was just one time!"
    z "I'll always remember you dropping your sword when a spider emerged-"
    b "Everyone is scared of something!"
menu:
    set menuset
    "Ask about the history of the ruin":
        jump ch1_s3_2
    "Ask about the plentiful treasure":
        jump ch1_s3_3
    "Ask about the scary monsters":
        jump ch1_s3_4
jump ch1_s3_5

label ch1_s3_5:
    $ zmood = "happy"
    z "Let's leave for the ruin then! It's an hour walk through the forest!"
    $ dmood = "neutral"
    d "Wait... now?"
    z "Of course! We have to work to eat, after all. So let's get rich!"
    $ bmood = "happy"
    b "Let's go! Let's fight!"
    $ amood = "happy"
    a "And gain some valuable knowledge!"
    d "...Alright, let's go now then."
    jump ch1_s4

label ch1_s4:
    scene forest path
    show dobrava at farright
    with fade
    $ dmood = "neutral"
    $ amood = "annoyed"
    $ bmood = "surprised"
    $ zmood = "happy"
    "We've been on the road for half an hour now and I can't help but realise one thing about my party..."
    show bogdan at leftish
    show andia at farleft
    show zygmunt at rightish
    with dissolve
    b "I took off my pants and then she ran away from me screaming!"
    "...they never stop talking."
    b "My feelings were really hurt!"
    "Zygmunt laughs really loudly, holding his stomach and Andia facepalms."
menu:
    "Say you feel sorry for Bogdan":
        $ bogdan += 5
        jump ch1_s4_2
    "Laugh with Zygmunt":
        $ zygmunt += 5
        jump ch1_s4_3
    "Cringe with Andia":
        $ andia += 5
        jump ch1_s4_4

label ch1_s4_2:
    $ dmood = "sad"
    d "Bogdan... I'm so sorry... I hope you're not too devastated."
    $ bmood = "surprised"
    b "Devastated? Why would I be?"
    $ dmood = "surprised"
    d "It ruined your night, didn't it? You were hoping to \"score\"?"
    z "Ah, don't worry about that, Dobrava. Twenty minutes later he had another girl in his lap."
    "I'm puzzled by this. I'm pretty popular with all genders but even I don't find that many people who want to spend the night with me."
    d "I see..."
    $ bmood = "angry"
    if pronoun == "she":
        b "Stupid Zygmunt! Can you see the look on her face?"
    else:
        b "Stupid Zygmunt! Can you see the look on their face?"
    jump ch1_s4_5

label ch1_s4_3:
    $ dmood = "happy"
    d "Oh my gods, I think I'm gonna die from laughter."
    d "Just how scary must your \"thing\" be for someone to run away screaming."
    $ bmood = "surprised"
    b "Scary? I really hope not! Would you mind checking?"
    $ dmood = "surprised"
    $ amood = "surprised"
    $ zmood = "surprised"
    "He grabs his trousers but before he can pull them down, Zygmunt stops his hand."
    $ zmood = "angry"
    z "Stupid Bogdi! Don't do that, you dickhead!"
    b "Why not?!"
    z "Can't you see the look on Dobrava's face?"
    jump ch1_s4_5

label ch1_s4_4:
    $ dmood = "neutral"
    d "That is the cringiest thing I've heard today."
    a "I wholeheartedly agree."
    $ zmood = "happy"
    z "Let me add to it: twenty minutes later he had another girl in his lap."
    "I'm puzzled by this. I'm pretty popular with all genders but even I don't find that many people who want to spend the night with me."
    $ dmood = "surprised"
    d "I see..."
    $ bmood = "angry"
    if pronoun == "she":
        b "Stupid Zygmunt! Can you see the look on her face?"
    else:
        "Stupid Zygmunt! Can you see the look on their face?"
    jump ch1_s4_5

label ch1_s4_5:
    $ bmood = "surprised"
    if pronoun == "she":
        b "Oh no... she's disgusted with me!"
    else:
        b "Oh no... they're disgusted with me!"
menu:
    "Say that you are. You believe in one true love":
        jump ch1_s4_6
    "Deny it. You have to actively look for love":
        jump ch1_s4_7

label ch1_s4_6:
    $ dmood = "neutral"
    d "I am... but only a little. I don't want to sound like I'm judging you, Bogdan. You do you. But I don't like sleeping around all that much."
    $ dmood = "happy"
    d "I believe in one true love."
    $ zmood = "surprised"
    z "Huh?! A bard that doesn't sleep around?!"
    $ dmood = "angry"
    d "Believe it or not, bards are people too. We're a diverse group."
    $ zmood = "sad"
    z "I see, my apologies."
    $ bmood = "happy"
    $ zmood = "neutral"
    b "That's amazing though, Dobrava. I believe in helping love find me, but I respect your choice too."
    $ amood = "happy"
    a "And so do I. Finally a companion who thinks like me!"
    jump ch1_s4_8

label ch1_s4_7:
    $ dmood = "neutral"
    d "Of course I'm not! I'm a bard after all, I like flirting and getting to know people intimately."
    $ dmood = "happy"
    d "Love should be shared with as many people as possible!"
    $ zmood = "happy"
    z "A woman of my heart. I'm so moved!"
    $ amood = "annoyed"
    if pronoun == "she":
        a "You're just hoping to score with her."
    else:
        "You're just hoping to score with them."
    $ bmood = "happy"
    b "Even if he is, I'm glad you are comfortable with this way of living."
    d "If it makes you happy, why not do it?"
    z "Exactly."
    $ amood = 'neutral'
    a "Well, I believe in holding out in one true love. But I guess I'm the only one here."
    d "That's amazing too, Andia. You do you."
    a "I will. I don't plan on changing my ways anytime soon."
    jump ch1_s4_8

label ch1_s4_8:
    "We change the topic to something less dangerous than our views on sex and love."
    "I'm dragged along into their banter so easily and I can't help but enjoy being able to talk with others about whatever I want."
    "They were strangers a few hours ago, but they accepted me into their circle of friends so easily. I hope they don't change their mind."
    jump ch1_s5

label ch1_s5:
    $ dmood = "determined"
    $ amood = "neutral"
    $ bmood = "neutral"
    $ zmood = "determined"
    scene forest path
    show bogdan at rightish
    show zygmunt at farright
    show dobrava at leftish
    show andia at farleft
    with fade

    "As we get closer to the location of the ruin, the party grows more serious and the playful banter stops."
    "Zygmunt moves first on high alert, looking around carefully and everyone unsheathes their weapons. Bogdan is a few steps behind him. Andia and I are in the back."
    "I take my flute in hand. My spells manifest through song, so I need it to be useful."
    $ dmood = "angry"
    d "Are we expecting trouble?"
    a "Shh..."
    "Andia puts a finger to her lips. I should follow her advice and be quiet. After all, they are familiar with this adventuring thing. I should think they know what they are doing."
    $ dmood = "surprised"
    $ amood = "surprised"
    $ bmood = "surprised"
    $ zmood = "surprised"
    "Suddenly, from the bushes on the right, a man emerges. He's looking at the ground while walking a few steps in our direction."
    $ zmood = "angry"
    z "Stop right there!"
    "The man doesn't react to Zygmunt's words at all. He's wearing light armor, but no piece of his gear matches with the rest. It seems he's just wearing whatever he could find."
    "His arms are bare and there's an elaborate tattoo of a green Zmiy-a serpent-like dragon-coiled around his left arm."
    $ amood = "annoyed"
    a "A bandit of the Green Zmiy!"
    $ bmood = "angry"
    "Bogdan and Zygmunt look back at Andia and they seem to reach some kind of wordless agreement. Zygmunt aims his bow at the man."
    "They cannot seriously be thinking about killing him?! So far he's done nothing to us!"
    $ zmood = "neutral"
    z "Stop right there or I will shoot!"
    "...They are thinking of killing him. But that's murder in cold blood!"
    "The man doesn't respond and continues walking towards us."
    $ zmood = "sad"
    z "Alright. You leave me no choice."
menu:
    "Run up to Zygmunt and stop him from shooting":
        jump ch1_s5_2
    "Scream at Zygmunt that he shouldn't kill the man":
        jump ch1_s5_3
    "Don't stop the murder":
        jump ch1_s5_4

label ch1_s5_2:
    show dobrava at rightish
    show bogdan at leftish
    with move
    $ bmood = "surprised"
    $ zmood = "surprised"
    $ amood = "surprised"
    $ dmood = "angry"
    "I run past Andia and Bogdan up to Zygmunt and grab the hand he has on his bow, stopping him from firing an arrow at the man."
    d "No! Stop it! That's murder!"
    $ zmood = "angry"
    z "What are you doing, Dobrava!"
    "The bandit looks up at us and I see his eyes are glowing red. With inhuman speed, he closes the distance between us in an instant."
    show bogdan at farright
    show dobrava at leftish
    show zygmunt at rightish
    with move
    "But Bogdan is quicker.He beheads the man when he is mere inches away from us, poised to strike. The bandit's clawed hand barely misses me."
    jump ch1_s5_5

label ch1_s5_3:
    d "Don't kill him! That's a human man! He's done nothing to hurt us!"
    $ bmood = "sad"
    b "That's not a human..."
    "The bandit looks up at us and I see his eyes are glowing red. With inhuman speed he closes the distance between us in an instant."
    "Zygmunt fires an arrow. A headshot! The arrow embeds itself in the man's head but... he's still moving..."
    show bogdan at farright
    show zygmunt at rightish
    with move
    "Bogdan runs past Zygmunt and beheads the bandit when he is inches away from the half-elf, poised to strike. The bandit's clawed hand barely misses Zygmunt."
    jump ch1_s5_5

label ch1_s5_4:
    "I'm too terrified to say anything so I just stand there, frozen."
    "The bandit looks up at us and I see his eyes are glowing red. With inhuman speed he closes the distance between us in an instant."
    "Zygmunt fires an arrow. A headshot! The arrow embeds itself in the man's head but... he's still moving..."
    show bogdan at farright
    show zygmunt at rightish
    with move
    "Bogdan runs past Zygmunt and beheads the bandit when he is inches away from the half-elf, poised to strike. The bandit's clawed hand barely misses Zygmunt."
    jump ch1_s5_5

label ch1_s5_5:
    $ dmood = "surprised"
    "Wait... clawed hand?! Red eyes?! Inhuman speed?!"
    $ bmood = "angry"
    "Bogdan stabs the corpse of the bandit a few more times but, to my horror, its limbs are still moving despite the head being firmly removed from its body."
    d "What is this?!"
    $ bmood = "neutral"
    b "Andia, cast a ball of fire."
    $ amood = "annoyed"
    a "You know I loathe fire spells..."
    "Bogdan just glares at Andia."
    a "On it, on it."
    "A minute later, a small ball of fire incinerates the bandit's corpse, its limbs still writhing despite the flames. The smell of a burning body is disgusting. I move a bit away from the party and lose my lunch."
    $ zmood = "sad"
    z "Are you alright?"
    $ dmood = "sad"
    $ amood = "surprised"
    $ bmood = 'surprised'
    "Zygmunt is holding my hair back as I vomit until there's nothing left to throw up. I look up at him but can't see him through my tears."
    $ bmood = 'sad'
    $ amood = 'sad'
    "He hands me a canteen of water which I accept gratefully and use to clean my mouth. Then he wipes my tears off with a handkerchief."
    z "Dobrava... talk to me..."
    "Zygmunt looks like he is about to cry himself."
    a "We shouldn't have brought Dobrava..."
    $ dmood = 'angry'
    d "Whatever you say, just don't say that! I'm alright! It's just my first time being in a fight...my first time witnessing the death of something so human!"
    "They all go quiet as they look at me."
    $ bmood = 'neutral'
    $ dmood = 'sad'
    b "Each and every one of us has been through this..."
    a "Yes, it's not easy at first. But you get used to it... however horrible that sounds."
    z "I just wish you had told us that you're so inexperienced."
    a "There's nothing that could have prepared her for death though, Zygmunt."
    z "I suppose that's true..."
    d "I just... I think I need a hug."

menu:
    "Hug Zygmunt":
        $ zygmunt += 5
        show dobrava at center with move
        $ zmood = 'neutral'
        "Not giving Zygmunt anytime to process what I've just said, I hug him tightly. He looks surprised, but still hugs me back."
        $ zmood = 'shy'
        "A soft kiss is placed at the top of my head. This feels nice... he smells so nice too, like a forest after it's rained."
        $ bmood = 'happy'
        $ amood = 'happy'
        show dobrava at leftish with move
        "After a moment I let go of him and look at the rest of the party. Bogdan and Andia are smiling at me and Andia even winks. What's that about?"
        jump ch1_s5_6
    "Hug Bogdan":
        $ bogdan += 5
        show zygmunt at leftish
        show dobrava at right
        with move
        $ bmood = 'surprised'
        "I pass by Zygmunt and go to Bogdan. It's a bit awkward at first when I hug him, though he hugs me back regardless."
        $ bmood = 'shy'
        "But when I hide my face in his chest, he pats my head and I no longer feel like this is wrong. He smells so nice too, a very manly scent which I cannot quite describe."
        $ amood = 'happy'
        $ zmood = 'happy'
        show dobrava at rightish with move
        "It feels safe, like all is right in the world. After a moment I let go of him and look at the rest of the party. Zygmunt and Andia are smiling at me and Andia even winks. What's that about?"
        jump ch1_s5_6
    "Hug Andia":
        $ andia += 5
        show dobrava at left with move
        show andia behind dobrava
        $ amood = 'surprised'
        "I pass by Zygmunt and go to Andia. She is very surprised when I hug her and takes a moment to hug me back."
        $ amood = 'shy'
        "But when she does I feel warmth and calmness like I've never felt before. She smells so nice too, of spring flowers."
        $ zmood = 'happy'
        $ bmood = 'happy'
        show dobrava at leftish with move
        "Zygmunt and Bogdan are smiling at me and Zygmunt even winks. What's that about?"
        jump ch1_s5_6
    "Nevermind.":
        "No, this is too awkward. I put my hands around my waist and hug myself."
        "The others look sad that I haven't gone to any of them for comfort... but I don't know them well enough. It would just feel weird."
        jump ch1_s5_6

label ch1_s5_6:
    "There's something more pressing to ask about."
    $ dmood = 'sad'
    d "What was that... thing?"
    $ bmood = 'sad'
    $ amood = 'sad'
    $ zmood = 'sad'
    b "A type of undead..."
    a "A walking corpse..."
    z "A zombie."
    $ dmood = 'surprised'
    d "Oh my gods! Do you mean to say that thing wasn't alive... and yet it was walking?!"
    z "That would be correct."
    d "Have you met things like that before?!"
    $ bmood = 'neutral'
    b "Several times."
    a "And more often in this area than we would have liked."
    z "We should be on high alert as we proceed to the ruin."
    d "We're continuing?!"
    $ bmood = 'happy'
    b "Of course!"
    $ dmood = 'sad'
    d "But what if there are more of them?"
    b "Don't worry. We'll protect you. All you have to do is stay back and heal us after the fight if we get hurt."
    d "...ok."
    "I have some spells I could use during the fight, but am I strong enough to use them despite my fear?"
    $ amood = 'happy'
    a "You don't have to force yourself, Dobrava. The first few times are hard. So just take it easy. We're happy to have you here. Right, guys?"
    b "Of course!"
    $ zmood = 'happy'
    z "Always!"
    $ dmood = 'neutral'
    "I feel reassured, but I can't help but feel scared. I can't back away now."
    "I gave my word that I would help them. And giving a promise is the most important thing in the world. You can't go back on your word once it's given."
    $ dmood = 'determined'
    d "Alright, let's go!"
    "They all look relieved with my renewed confidence and smile at me as we go off the road into the forest proper."
    jump ch1_s6
