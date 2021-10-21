label ch1_s6:
    stop music fadeout 1.0
    play music "Elven Ruin.ogg" fadein 1.0 loop

    $ dmood = 'neutral'
    $ zmood = 'neutral'
    $ bmood = 'neutral'
    $ amood = 'neutral'

    scene ruins with fade

    "After walking for a few minutes we reach the elven ruin. It feels like an ancient place, long abandoned. At the same time I feel somewhat uneasy. What if there are more of those creatures?"
    $ lightZ = True
    show zygmunt at center with dissolve
    "Zygmunt moves first on high alert. He is very handsome like this in his element."
    $ lightZ = False
    show zygmunt at farright with move
    "Come to think of it, they are all gorgeous, focused like that."
    "If I was not so terrified I would have admired Bogdan's prowess in combat and Andia's ability to recite such complex incantations."
    "I have to admit that despite their goofiness outside work, when they are actually serious they're quite capable."
    "We reach the remains of the wall and Zygmunt jumps over it. A few seconds pass and we hear a click."
    show zygmunt at farright with move
    show bogdan at rightish
    show andia at leftish
    show dobrava at farleft
    with dissolve
    $ zmood = 'happy'
    z "Another trap disarmed!"
    "Bogdan steps on top of the foundation and reaches out to us."
    "Andia ignores his hand and uses wind magic to levitate slightly. This allows her to pass to the other side on her own. I guess she is too prideful to take anyone's help."
    $ bmood = 'happy'
    "I take Bogdan's hand and he smiles at me."
    if pronoun == "they":
        b "And up you go, precious!"
    else:
        b "And up you go, Princess!"
    $ dmood = 'surprised'
    "He moves his other hand to my waist and raises me up."
    d "Whoa!"
    $ zmood = 'angry'
    $ amood = 'happy'
    "And puts me down gently on the other side. Zygmunt watches us. He looks annoyed and Andia snickers, covering her lips with her hand."
    $ dmood = 'neutral'
    $ zmood = 'neutral'
    a "But this ruin is amazing! It's definitely more than a few hundred years old. Do you see the engraving on that wall? It tells the history of..."
    "She continues blabbering but, as much as those things interest me normally, right now I don't feel safe enough to focus on stories."
    "We move deeper and deeper into the ruin, passing chambers with sarcophages and sculptures. Everything is covered by a thick layer of dust and cobwebs."
    "Luckily for Bogdan, we don't encounter any giant spiders."
    "Andia has taken out a scroll and is making sketches. I look over her shoulder."
    $ dmood = 'surprised'
    d "Wow, your drawings are amazing!"
    a "Thank you. Drawing and painting are my hobbies outside of adventuring and history."
    $ zmood = 'neutral'
    z "Shh..."
    "I want to talk about it more but Zygmunt tells us to be quiet."
    $ dmood = 'surprised'
    "Too late though, because suddenly from both of our sides skeletons emerge. There are six on the left side and two on the right."
    "Some come out from the open sarcophagi. Others join them from the corridors."
    $ bmood = 'angry'
    $ amood = 'angry'
    $ zmood = 'angry'
    "Bogdan curses under his breath and pulls out his sword. Zygmunt and Andia draw their weapons too."
    "They gesture to each other-a sign language I don't understand. Probably something they came up with for themselves in the years they've adventured together."
    $ dmood = 'neutral'
    "The skeletons are scary but I'm not as terrified as with that zombie. I know those things are dead after all, we just have to stop them from moving."
    stop music fadeout 1.0
    play music2 "combat music (level 0).ogg" fadein 1.0 loop
menu:
    "Buff the party":
        jump ch1_s6_2
    "Do nothing":
        jump ch1_s6_3

label ch1_s6_2:
    $ dmood = 'happy'
    play music "A Song of Hope and Heroism.ogg" fadein 1.0
    "I play a song of hope and heroism. My magic surrounds the other party members."
    $ bmood = 'happy'
    b "Wow, I feel so strong and confident now!"
    d "Just don't let it get to your head!"
    "Bogdan attacks the skeletons on the left with Zygmunt supporting him by shooting arrows at their feet to make them trip."
    "Meanwhile, Andia creates a strong blast of wind which shatters the skeletons on the right."
    $ amood = 'neutral'
    $ zmood = 'neutral'
    "The fight doesn't even last a minute, that's how capable my companions are."
    $ dmood = 'neutral'
    d "Anybody hurt?"
    $ zmood = 'happy'
    z "Of course not. Thanks to your buff we're stronger than ever!"
    "Was my song really so powerful? Huh. I guess my healing skills aren't needed after all!"
    jump ch1_s7

label ch1_s6_3:
    "It's better if I sit this out and conserve my energy for healing."
    $ dmood = 'neutral'
    "Bogdan attacks the skeletons on the left with Zygmunt supporting him by shooting arrows at their feet to make them trip."
    "Meanwhile, Andia creates a strong blast of wind which shatters the skeletons on the right."
    $ dmood = 'neutral'
    $ amood = 'neutral'
    $ bmood = 'neutral'
    "The fight doesn't even last a minute, that's how capable my companions are."
    d "Anybody hurt?"
    b "Yes, one of them scratched me."
    d "Let me heal that."
    play music "A Song of Healing (excerpt).ogg" fadein 1.0
    "I play a song of healing for Bogdan and his wound closes."
    $ bmood = 'happy'
    b "Thank you!"
    $ dmood = 'happy'
    d "That's what I'm here for!"
    jump ch1_s7

label ch1_s7:
    stop music2 fadeout 1.0
    play music "combat music (level 2).ogg" fadein 1.0 loop

    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    $ zmood = 'neutral'

    scene throne room
    show zygmunt at farright
    show bogdan at rightish
    show andia at leftish
    show dobrava at farleft
    with fade

    "As we move even deeper into the ruin we find some ancient Elven gold coins and minor jewels. Nothing awfully exciting, but it should pay for a comfortable life for the four of us for a week."
    "Eventually, after dispatching two more hordes of skeletons, we enter what looks like a throne room... well, what was a throne room eons ago."
    "It's a beautiful place with many columns and sculptures. The roof is missing and we can see the sky. There is a skeleton in front of the throne wearing robes."
    "It's quite far away from us, on the other side of the long, cathedral-like room. At least 50 feet away from us. It doesn't immediately attack us, so we take some time to assess the situation."
    "A skeleton wearing robes is probably an undead warlock or another magician of sorts. The right thing to do is to prevent it from using magic somehow."
    $ bmood = 'happy'
    b "I guess we're at the boss fight!"
    $ amood = 'annoyed'
    a "Ugh..."
    $ zmood = 'happy'
    z "Look at that shiny thing behind it! I wonder what it is!"
    $ dmood = 'happy'
    d "Looks like some sort of scepter to me! And it looks beautiful... what a find!"
    z "I wonder how much it's worth..."
    $ amood = 'surprised'
    $ bmood = 'surprised'
    $ dmood = 'surprised'
    $ zmood = 'surprised'
    "Our excited talk is interrupted by the skeleton firing a bolt of dark energy at our feet. We all jump away just in time to avoid injury."
    $ dmood = 'angry'
    d "You piece of shit! Those were my favourite shoes!"
    "Why would I wear my favourite shoes to elven ruins? Well, I have not shared this information with anyone yet... but I'm actually a shoe collector and all of my shoes are my favourites."
    "Shoes are serious business. They are a gift from gods. They should be worshipped, not scorched by dark energy."
    play music2 "A Song of Silence.ogg" fadein 1.0
    "Fueling my anger into my song, I play the Silent Song, creating a field that seals the use of magic in the back half of the cathedral for those standing in it."
    d "Try casting any spells now, you bastard!"
    $ zmood = 'happy'
    $ amood = 'neutral'
    $ bmood = 'happy'
    z "Wow, that's amazing!"
    "Zygmunt shoots an arrow after arrow at the skeleton that is now confused. The enemy is unable to cast any spells while Andia is outside of the field of silence, so she casts a blast of wind."
    "Meanwhile Bogdan runs up to the skeleton warlock and whacks it with his big sword."
    stop music fadeout 1.0
    "After a few attacks from everyone, the skeleton begins to turn to dust, defeated. I know this sounds like an easy boss fight, but it was only this simple thanks to it being unable to cast spells."
    "Still, as I look at my companions they all look tired. Fighting takes a toll on the body after all. That's why it is best for fights to be brief and to the point."
    $ dmood = 'happy'
    d "This was actually fun!"
    $ amood = 'happy'
    a "I'm glad you thought so!"
    z "It would not have been so easy without you."
    b "Thank you, Dobrava."
    d "My pleasure."
    play music "Elven Ruin.ogg" fadein 1.0 loop
    "We move closer to the artifact on the throne."
    $ zmood = 'neutral'
    $ amood = 'neutral'
    $ bmood = 'neutral'
    $ dmood = 'neutral'
    z "Oh no... how disappointing. It's just the handle of a scepter..."
    d "It's still beautiful though. Might be worth something."
    a "There are inscriptions in Elven on the handle... but they are so small..."
    "She reaches out to take the handle and look at it more closely but Bogdan grabs her hand and stops her."
    $ bmood = 'surprised'
    b "Wait! What if it's cursed?"
    d "We should take it regardless. Better for it to be with us than in these musty old ruins."
    $ bmood = 'neutral'
    "We all look at each other. After a few moments, Zygmunt takes the handle through a piece of blessed cloth and wraps it in it."
    "The cloth {i}should{/i} stop any curse from spreading to us, but when you're working with items this old? Who knows."
    "For now though, nothing happens. Hopefully it stays that way."
    "With our loot acquired and the ruin explored we make our way back to the tavern."
    jump ch1_s8
