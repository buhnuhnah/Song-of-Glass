label ch2_s1:
    stop music fadeout 1.0
    play music2 "Russian Polka.ogg" fadein 1.0 volume 0.5 loop

    $ amood = 'neutral'
    $ bmood ='neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene tavern
    show bogdan at farright
    show zygmunt at rightish
    show andia at farleft
    show dobrava at leftish
    with fade

    "We all sit in the tavern's dining hall eating eggs with bacon for breakfast."
    "The scepter's handle is lying in the middle of the table. We each look at it curiously."
    z "There are a few things we need to do today."
    $ bmood = 'sad'
    b "No adventuring today?"
    z "No, Bogdi. I think it will be most efficient if we split up."
    a "I want to study the handle. I'll take my books on ancient Elven and try to decipher the writing on it as best as I can."
    z "Alright. Then Bogdi and I will go into town. Bogdan you'll go to talk to the mayor about there being an undead infestation on the road."
    $ bmood = 'surprised'
    b "Me? Talking? Why not you?"
    $ zmood = 'happy'
    z "After the ruckus I've caused in town the past week, I doubt he'll want to see me."
    $ bmood = 'neutral'
    b "Ah... right."
    $ dmood = 'surprised'
    d "What did you do?"
    z "Let the past be the past. I will go to the market to acquire some supplies."
    $ dmood = 'neutral'
    z "Dobrava, you can decide what you want to do."
menu:
    "Stay with Andia":
        $ andia += 5
        $ ch2_buddy = "andia"
        $ dmood = 'happy'
        d "I'll stay with Andia."
        a "Alright. A second set of eyes will be useful."
        jump ch2_s2_andia
    "Go with Zygmunt and Bogdan into town":
        $ dmood = 'happy'
        d "I'll go with Zygmunt and Bogdan."
        $ bmood = 'happy'
        z "Excellent!"
        "We leave Andia in the tavern and go to the market square."
        jump ch2_s2_boys
    "Work as a bard at the tavern":
        d "I'd rather work a bit as a bard, if you don't mind."
        a "Of course, you're free to do whatever you want."
        hide bogdan
        hide zygmunt
        with dissolve
        show andia at left
        show dobrava at right
        with move
        "The guys leave for the town and I watch Andia perform a summoning spell which brings a lot of books to the table."
        "I spend the rest of my day singing and telling stories. A crowd quickly gathers around me and I enjoy their attention."
        jump ch2_s3

label ch2_s2_andia:
    hide bogdan
    hide zygmunt
    with dissolve
    show andia at left
    show dobrava at right
    with move

    "The guys leave for the town and I watch Andia cast a spell. Suddenly, piles of books appear on the table next to the scepter's handle."
    $ dmood = 'surprised'
    d "Whoa! Where did those come from?!"
    a "I have a pocket space for books so I don't have to carry all of them around myself. This is everything that I own that may be relevant to our scepter."
    a "This pile is in ancient Elven and modern Elven, so I'll be the one reading it. But that one is in the common tongue. Could you look through it and see if you find anything relevant?"
    $ dmood = 'determined'
    d "On it!"
    "There are three books: {i}History of Ostoya{/i}, {i}Of Elves and Men{/i}, and {i}The Great Exodus of Krasny Ludek{/i}... hmm, the last book sounds like it'll be the least useful, but I'll look through it regardless."
    $ dmood = 'neutral'
    "We spend the next few hours in silence. I take notes on what I think might be relevant to our cause."
    "Meanwhile, Andia focuses on translating the ancient Elven engravings on the scepter's handle. She bites her lip and mumbles to herself a lot while doing it."
    $ amood = 'annoyed'
    a "This is so frustrating."
    "Innkeeper Marysia" "Care for a lunch break, scholars?"
    a "No need, we-"
    $ dmood = 'happy'
    d "We would very much appreciate having a break with something warm to eat."
    a "But we-"
    d "The work isn't going to run away, Andia. There's still a lot left to do. We won't complete it today, anyways. Let's enjoy our time together a bit."
    $ amood = 'neutral'
    a "...Okay, I guess you're right."
    "Marysia serves us warm goulash - just vegetables for Andia and the complete meaty package for me. We dig in. Andia eats like a starving woman and I laugh to myself."
    a "What is it?"
    d "You've got some sauce on your chin."
    a "Ah, where..."
menu:
    "Wipe it off for her":
        $ andia += 5
        d "Here we go!"
        "I wipe it off Andia's face and my fingers linger on her skin a moment longer."
        $ amood = 'shy'
        a "Thank you..."
        jump ch2_s2_andia2
    "Tell her where it is":
        d "A bit more to the right!"
        "Andia wipes it off, finding the correct spot."
        a "Thank you!"
        jump ch2_s2_andia2
    "Ignore it":
        $ songbird += 5
        $ dmood = 'neutral'
        "I don't care that Andia's face is smeared with sauce, perhaps it'll humble her uptight attitude."
        "As I don't tell Andia where it is, her wiping only makes it worse. The Innkeeper Marysia laughs as she passes by our table."
        $ amood = 'annoyed'
        a "Thank you, Dobrava. Would it have killed you to tell me where the sauce was?"
        "I just shrug in response."
        jump ch2_s2_andia2

label ch2_s2_andia2:
    "After we finish eating, we compile the information we found that might be related to the scepter."
    "Unfortunately, there isn't much that's relevant. We sigh and return to work."
    jump ch2_s3

label ch2_s2_boys:
    stop music2 fadeout 1.0
    play music "market music.ogg" fadein 1.0 loop

    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene marketplace
    show bogdan at right
    show zygmunt at left
    show dobrava at center
    with fade

    "The market square is bustling with activity. Today is a market day, so folk from nearby villages have come to sell their produce and crafts."
    b "I'm going to visit the mayor then."
menu:
    "Go with Bogdan to the mayor":
        $ bogdan += 5
        $ ch2_buddy = "bogdan"
        d "I'll go with Bogdan to the mayor's."
        $ bmood = 'happy'
        "I can't help but feel worried about Bogdan speaking to authorities alone. He's not exactly the best conversationalist."
        "I doubt he even knows that word. The best \"talker\"."
        "Bogdan looks relieved and I can't help but think I made the best decision I could in this situation."
        jump ch2_s2_bogdan
    "Stay at the market with Zygmunt":
        $ zygmunt += 5
        $ ch2_buddy = "zygmunt"
        $ dmood = 'happy'
        d "I'll shop with Zygmunt then."
        $ zmood = 'happy'
        z "Great!"
        jump ch2_s2_zygmunt

label ch2_s2_bogdan:
    $ dmood = 'neutral'
    $ bmood = 'neutral'
    hide zygmunt with dissolve
    show dobrava at left with move

    "We leave Zygmunt and make our way through the market to the townhouse where the mayor resides."
    d "Why didn't Zygmunt go to the mayor instead? Isn't he the face of your group?"
    b "{i}Our{/i} group. And yes, he is."
    $ bmood = 'sad'
    b "But the other day, Zygmunt tried to seduce the mayor's daughter and the mayor got very upset for some reason."
    d "I can't imagine why."
    $ bmood = 'neutral'
    b "I can't either. The daughter was very willing to go with Zygmunt to the forest and..."
    $ dmood = 'shy'
    d "That's too much detail!"
    $ bmood = 'shy'
    b "Ahh... what I was trying to say is that it was consensual but the mayor didn't approve. He said something about marriage and now Zygmunt is avoiding him."
    $ dmood = 'happy'
    d "I see.. none of that is very surprising."
    $ dmood = 'neutral'
    $ bmood = 'neutral'
    d "I guess the conversation with the mayor is on us then."
    b "About that... I wouldn't mind if you were the one talking."
    $ bmood = 'happy'
    b "I'll treat you to something good later, ok?"
    "I wanted to be the one talking to the mayor anyways, but I don't mind being bribed either."
    $ dmood = 'happy'
    d "Sure!"

    $ bmood = 'neutral'
    $ dmood = 'neutral'
    scene office
    show dobrava at right
    show bogdan at left
    with fade
    stop music fadeout 1.0
    play music2 "polonaise (hpsd).ogg" fadein 1.0 loop

    "We enter the townhouse. There is a stern-looking elven woman with big glasses sitting at a desk before us."
    "Behind her are numerous bookshelves carrying heavy tomes - probably all the accounting one has to do for a town this large. I don't envy this person at all."
    $ dmood = 'happy'
    d "We'd like to see the mayor, please!"
    "The secretary adjusts her glasses and looks at me."
    "Secretary" "An adventurer, yes?"
    d "That's correct!"
    "Then she looks at Bogdan for a while. I start fidgeting a bit, thinking she might have seen Zygmunt with Bogdan at some point, but she doesn't seem to recognise him."
    "Secretary" "You're lucky. The mayor is free right now. Please enter the room on the left."
    d "Thank you!"
    "We enter the indicated room and introduce ourselves. The mayor is an old dwarf in expensive but not overly extravagant clothes."
    "He looks tired, likely from the worry and stress that comes with managing a town."
    $ dmood = 'neutral'
    d "We're here to let you know about a problem we've encountered while adventuring."
    "Mayor" "Problems, oh, how I love them... What is it this time?"
    $ dmood = 'sad'
    d "On the road we encountered one of the Green Zmiy..."
    "Mayor" "So they're active in the area again. Great."
    d "...But he wasn't actually alive. He was a zombie."
    "Mayor" "What? A zombie?! What manner of nonsense are you talking about?!"
    $ dmood = 'surprised'
    $ bmood = 'angry'
    d "A zombie is a type of undead which..."
    "Mayor" "I know very well what a zombie is! And I know there wouldn't be one without a necromancer around!"
    d "That's why we..."
    "Mayor" "And we don't have any necromancers in our region! No, we don't! Hiring a group of adventurers capable enough to take care of one would cost the town too much money!"
    b "So it's better if you ignore the problem?!"
    "Mayor" "You insolent youngling...! What are you implying?!"
    b "That you are a-"

menu:
    "Calm Bogdan down":
        $ bmood = 'surprised'
        "I put a hand on Bogdan's arm and squeeze firmly, stopping him from speaking."
        $ dmood = 'happy'
        d "Now, now, let's just leave. We've reported the incident to the mayor, so we've done our citizenly obligation."
        $ dmood = 'neutral'
        d "What he does with that information is up to him."
        jump ch2_s2_bogdan2
    "Give the mayor a piece of your mind":
        $ dmood = 'angry'
        d "I think you are the insolent one - ignoring good citizens who come to you with real problems!"
        b "I couldn't have said it better myself!"
        "Mayor" "You rude adventurers! Leave my office this instant!"
        jump ch2_s2_bogdan2
    "Let Bogdan insult the mayor":
        b "-dirty pig!"
        $ dmood = 'happy'
        "I can't help but laugh. That was a... creative way to insult the mayor..."
        "Mayor" "What did you call me?!"
        $ dmood = 'neutral'
        d "Now, now - there's no need for any of this. We've given our report, let's just leave."
        jump ch2_s2_bogdan2

label ch2_s2_bogdan2:
    $ bmood = 'angry'
    $ dmood = 'neutral'
    scene marketplace
    show bogdan at left
    show dobrava at right
    with fade
    stop music2 fadeout 1.0
    play music "market music.ogg" fadein 1.0 loop

    "We take our leave. Back in the market, I can see Bogdan fuming."
    b "Damn! What a piece of shit!"
    $ dmood = 'sad'
    d "I admit, he's too stingy to take care of the town as he should."
    d "What are we going to do?"
    b "As strong as the party's become after you joined Dobrava, I'm not confident we can defeat a necromancer with just the four of us."
    b "I could ask my mother for help but... I've never done that. I don't want to show weakness."
    $ dmood = 'surprised'
    d "It's not a weakness to ask for the help of others!"
    $ bmood = 'sad'
    b "I guess... it will take mother two weeks to come here from the border anyways. Do we have that much time?"
    $ dmood = 'sad'
    d "We might not. I guess it's on us to protect the town then?"
    $ bmood = 'neutral'
    b "It might as well be! And we will protect it!"
    $ dmood = 'neutral'
    "I look around for something to cheer Bogdan up. There's a stall with fried chicken, one with cotton candy, and one with healthy vegetables."
    $ dmood = 'happy'
    d "Bogdi!"
    $ bmood = 'surprised'
    b "What is it, Dobrava?"
    "What should we eat?"
menu:
    "Chicken is a meal suitable for a warrior":
        $ bogdan += 5
        d "You said you would treat me to something good after the meeting! Let's eat some chicken wings!"
        $ bmood = 'happy'
        b "Oh... chicken! I love chicken! Except for kurolishek, the undead kind!"
        "Well, undead chickens are definitely problematic, as is everything else that's undead."
        "We buy one chicken wing for me and way too many for Bogdan before we sit by the fountain."
        jump ch2_s2_bogdan3
    "I bet Bogdi likes cotton candy":
        $ bogdan += 5
        "I bet Bogdi likes cotton candy."
        d "You said you would treat me to something good after the meeting! Let's get some cotton candy!"
        $ bmood = 'happy'
        b "Oh... cotton candy! I love sweet things! kittens, doggies, baby chickens..."
        d "But you don't eat those, do you?"
        b "Of course not! But cotton candy? Give me some of that!"
        "We buy one cotton candy for each of us and sit by the fountain."
        jump ch2_s2_bogdan3
    "Healthy vegetables for a healthy warrior":
        $ songbird += 5
        d "You said you would treat me to something good after the meeting! Let's eat some healthy vegetables!"
        $ bmood = 'sad'
        b "Is that broccoli...?"
        d "Yes! Broccoli is a gift from the gods!"
        b "I will eat it with you... I guess..."
        "We buy some fried vegetables for both of us and sit by the fountain."
        jump ch2_s2_bogdan3

label ch2_s2_bogdan3:
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    "We spend the next hour eating and commenting on the well-to-do townspeoples' weird manner of dress."
    $ dmood = 'surprised'
    d "What does she have on her head? Is that a peacock feather?!"
    $ bmood = 'happy'
    b "Look at that man's breaches! They're so low they are about to fall down!"
    $ dmood = 'happy'
    "It's really comfortable being around Bogdan. I can't help but enjoy our time together."
    jump ch2_s3

label ch2_s2_zygmunt:
    $ zmood = 'happy'
    $ dmood = 'neutral'
    hide bogdan with dissolve
    show zygmunt at left
    show dobrava at right
    with move

    "Bogdan leaves for the mayor's house located in one of the corners of the square. He quickly disappears from our sight."
    d "There really are a lot of people here. We could get separated easily."
    z "About that... I have a proposal for you. We can either do this the proper way or the fun way."
    $ dmood = 'surprised'
    d "What do you mean?"
    $ zmood = 'neutral'
    z "For the proper way, we can hold hands, going from stall to stall and buying everything we need."
    $ zmood = 'happy'
    z "Or, the fun way, I can show you a few tricks and we can save some money."
    d "Wait, you don't mean... stealing?"
    $ zmood = 'surprised'
    z "Stealing? Gods no! I call it \"acquiring things\"."
    d "It's still stealing, no matter what you call it."
    $ zmood = 'happy'
    z "Tomato, tomato. Which will it be?"
menu:
    "The proper way":
        $ zygmunt += 5
        $ holdZygmunt = True
        jump ch2_s2_zygmunt2
    "The \"fun\" way":
        $ zygmunt += 5
        $ ch2_thief = True
        jump ch2_s2_zygmunt3
    "It will be more efficient if you shop separately":
        $ songbird += 5
        jump ch2_s2_zygmunt4

label ch2_s2_zygmunt2:
    $ dmood = 'neutral'
    d "The proper way of course. I'm no thief."
    $ zmood = 'neutral'
    z "Ah... the boring way then. At least I get to hold hands with you."
    "Should we? I guess it {i}would{/i} be a pain in the ass if we end up separated..."
    show zygmunt at leftish
    show dobrava at rightish
    with move
    "I grab Zygmunt's hand and he intertwines his fingers with mine. His hand is bigger than mine and feels strong - rough and calloused from years plucking a bowstring."
    "Zygmunt pulls out a list from his pocket. I look at it and I see very proper Elven handwriting. Andia probably wrote this while I was still sleeping."
    z "Alright first... exchanging the old Elven coin at the antiquities shop."
    "We spend over an hour moving from shop to shop, trying to negotiate the best prices. Between the two of us-both well-spoken and articulate-we manage to get good deals. All while we hold hands."
    $ zmood = 'happy'
    z "Good job, partner!"
    $ dmood = 'happy'
    d "You too!"
    "After a job well done, we go back to the tavern."
    jump ch2_s3

label ch2_s2_zygmunt3:
    $ dmood = 'neutral'
    d "Alright. I hope I won't regret this. Let's do it the fun way."
    $ zmood = 'happy'
    z "Yay! I knew you didn't have a stick up your ass! Let's go, partner!"
    "First, Zygmunt shows me how to pickpocket people. I watch him move around the crowd fluidly and cut off people's coin pouches without them noticing anything."
    "Then he tells me to try it myself. He picks what he calls an easy target for me-an old, sweating merchant. As I get close to him I almost faint from the foul smell. But I succeed. His pouch is mine."
    $ dmood = 'happy'
    d "I did it!"
    "I exclaim in a back alley, showing my spoils to Zygmunt."
    z "Indeed you did."
    "He looks happy and proud of me. I feel a sense of accomplishment."
    z "Next is stealing things from stalls. Let's start with the classic: apples."
    "But as we move closer to the apple stalls, we hear yelling from the crowd."
    "Merchant" "Thief! I've been robbed!"
    "It's the merchant I pickpocketed earlier. Zygmunt grabs my hand."
    $ zmood = 'neutral'
    z "They haven't realised it's us yet so let's get out of here. Walk like a normal person leaving a market and don't look so frightened."
    "I school in my expression as best as I can and we leave the market before the guards come out to close it and interrogate everyone."
    jump ch2_s2_zygmunt5

label ch2_s2_zygmunt4:
    $ dmood = 'neutral'
    d "It will be more efficient if we each take half the items on the list and shop separately."
    $ zmood = 'surprised'
    z "Efficient? Maybe... but will it be fun? No."
    d "It's just shopping. It doesn't need to be fun."
    $ zmood = 'sad'
    z "Shopping can be fun too. But as you wish."
    "We go our separate ways and I buy the things I have on my half of the list. But as I move closer to the produce stalls, I hear yelling from the crowd."
    "Merchant" "Thief! I've been robbed!"
    $ zmood = 'neutral'
    "What is going on? I see Zygmunt walking out of the plaza like nothing happened. No one is looking at him, everyone is focused on the man screaming."
    "Did he... oh, I hope he didn't!"
    "I school my expression as best I can and leave the market in the same direction as Zygmunt  before the guards come to interrogate everyone."
    "I catch up with Zygmunt on the road to the tavern."
    z "Is everything alright, Dobrava?"
    "I say nothing to him."
    jump ch2_s2_zygmunt5

label ch2_s2_zygmunt5:
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene forest path
    show bogdan at left
    show dobrava at center
    show zygmunt at right
    with fade
    stop music fadeout 1.0
    play music2 "mazurka (accompanied).ogg" fadein 1.0 loop

    "We meet with Bogdan outside of town, just down the road from the tavern where we have been staying."
    $ bmood = 'surprised'
    b "Is everything okay? Where are the supplies?"
    z "Ah... we'll have to ask you to go buy things in our stead... with this money."
    $ bmood = 'angry'
    if ch2_thief == False:
        $ dmood = 'angry'
        d "So you've bought nothing?"
        "He throws the pouches he's \"acquired\" at Bogdan. Bogdan catches them but looks as displeased as I do."
    else:
        "He throws the pouches we've \"acquired\" at Bogdan. Bogdan catches them but looks displeased."
    $ dmood = 'neutral'
    b "You've stolen again, Zygmunt!"
    $ zmood = 'surprised'
    z "Not so loud, Bogdan!"
    b "You said you would stop with your thieving ways. And you! Dobrava! Why did you not stop him?!"
    $ dmood = 'sad'
    d "I..."
    b "Or did you help too?"
    if ch2_thief:
        d "I did but..."
    else:
        d "I didn't, we were shopping separately. I would have stopped him if I suspected this would happen."
    b "Oh gods, Zygmunt, you stupid bastard!"
    $ dmood = 'surprised'
    show dobrava at left
    show bogdan at center
    with move
    "Bogdan grabs Zygmunt by the collar and punches him in the face. Zygmunt doesn't even try to dodge." with sshake
    $ zmood = 'sad'
    z "I deserved that."
    b "Good. Now don't do it again."
    $ bmood = 'neutral'
    b "I'm going to town to do your job. Just go back to the tavern."
    "He takes the money and the Elven coin we have to exchange and goes back to town."
    if ch2_thief:
        "I feel guilty about what we did and from the look on his face, so does Zygmunt. We return to the tavern."
    else:
        "I feel angry at Zygmunt for what he did but I see he regrets it, so I calm down. We return to the tavern."
    jump ch2_s3


label ch2_s3:
    stop music fadeout 1.0
    stop music2 fadeout 1.0
    play music "Quiet Moments.ogg" fadein 1.0 loop

    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene tavern
    show bogdan at farright
    show zygmunt at rightish
    show dobrava at leftish
    show andia at farleft
    with fade

    "By the time each of our tasks are complete, it's evening. We gather together at our table where the scepter's handle lays in the middle on the blessed cloth."
    z "Have you made any progress, Andia?"
    a "...no, I hate to say it but I have not. I managed to decipher some of the words on the handle, but the rest remain a mystery."
    if ch2_buddy == "andia":
        $ zmood = 'happy'
        z "What do you have to say for yourself, Dobrava? You distracted her."
        $ dmood = 'surprised'
        d "What? I did not! I was helping!"
        $ amood = 'annoyed'
        a "She was. Leave her alone."
        z "I was just kidding. It's all good."
        "Andia sighs."
    $ zmood = 'neutral'
    $ dmood = 'neutral'
    $ amood = 'neutral'
    a "'Light', 'darkness', 'defeat'. Those words don't form a coherent narrative for me. I don't know what the creators of this artifact were trying to say."
    $ amood = 'annoyed'
    a "I need more time, but I'm sure I will figure this out."
    z "Take all the time you need."
    $ zmood = 'neutral'
    z "Well, it's been a long day. We've spent enough time together I think. Time to go to your rooms and sleep. I want you all well-rested for tomorrow!"
    $ dmood = 'happy'
    d "Yes, momma bear!"
    $ zmood = 'surprised'
    z "What did you call your leader?"
    "Zygmunt smacks me playfully on the hand as I get up and run upstairs."
    "Indeed, I'm very tired after today. But the most important thing is that it was fun."
    jump ch2_s4

label ch2_s4:
    stop music fadeout 1.0
    play music2 "dark magic music (level 2).ogg" fadein 1.0 loop
    $ dmood = 'neutral'
    scene inn room with fade
    "I fall asleep much easier tonight."
    scene throne room
    show dobrava at center
    with fade
    "However, I'm surprised to see the same castle as the night before."
    "I walk its hallways and look in the empty rooms. Eventually, I reach the throne room again."
    "This time around everything is more detailed, more decorated. As if the dream is a little more real."
    "It's still a bit hazy, as if I'm walking in fog, but it looks like a proper castle now."
    $ ymood = 'neutral'
    show yarlomila at left with dissolve
    show dobrava at right with move
    "However, it's still devoid of life, barring the beautiful raven-haired woman sitting on the throne. She looks so bored there. I guess I would be too if I had no one to talk to and nothing to do."
    d "Hello?"
menu:
    "Walk closer to her":
        "I walk closer to her and call out, but I don't expect an answer. I'm surprised when I get one."
        jump ch2_s4_2
    "Stay where you are":
        "I don't approach her, but call out. I don't expect an answer. I'm surprised when I get one."
        jump ch2_s4_2

label ch2_s4_2:
    "???" "Songbird."
    $ dmood = 'surprised'
    d "Songbird?"
    "I look around but see no birds here."
    d "Do you mean me? Because I'm a bard?"
    $ ymood = 'smirk'
    "She nods and smiles. Again, she smiles but her eyes remain cold."
    $ ymood = 'smirk'
    "I'm seriously creeped out here. When I try to ask her to stop smiling like that, I wake up, covered in cold sweat again."
    scene inn room with fade
    "It's morning. Time to wash up, get dressed, and start the day."
    jump ch3_s1
