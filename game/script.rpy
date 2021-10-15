# CHARACTER DEFINITIONS
define a = Character("Andia")
default amood = "neutral"
image andia = ConditionSwitch(
    "_last_say_who == 'a'", "images/sprites/Andia/andia [amood] talk.png",
    "True", "images/sprites/Andia/andia [amood].png")

define b = Character("Bogdan")
default bmood = "neutral"
image bogdan = ConditionSwitch(
    "_last_say_who == 'b'", "images/sprites/Bogdan/bogdan [bmood] talk.png",
    "True", "images/sprites/Bogdan/bogdan [bmood].png")

define d = Character("Dobrava")
default dmood = "neutral"
image dobrava = ConditionSwitch(
    "_last_say_who == 'd'", "images/sprites/Dobrava/dobrava [dmood] talk.png",
    "True", "images/sprites/Dobrava/dobrava [dmood].png")

define y = Character("Yarlomila")
default ymood = "neutral"
image yarlomila = ConditionSwitch(
    "_last_say_who == 'y'", "images/sprites/Yarlomila/yarlomila [ymood] talk.png",
    "True", "images/sprites/Yarlomila/yarlomila [ymood].png")

define z = Character("Zygmunt")
default zmood = "neutral"
image zygmunt = ConditionSwitch(
    "_last_say_who == 'z'", "images/sprites/Zygmunt/zygmunt [zmood] talk.png",
    "True", "images/sprites/Zygmunt/zygmunt [zmood].png")

# SPRITE POSITIONS
transform left:
    xalign 0.15 yalign 1.0
transform right:
    xalign 0.85 yalign 1.0
transform leftish:
    xalign 0.3 yalign 1.0
transform rightish:
    xalign 0.65 yalign 1.0
transform farleft:
    xalign 0.0 yalign 1.0
transform farright:
    xalign 0.95 yalign 1.0

# CG IMAGES
image andiaCG = Image("images/cg/Andia_CG.png")
image bogdanCG = Image("images/cg/Bogdan_CG.png")
image yarlomilaCG = Image("images/cg/Yarlomila_CG.png")
image zygmuntCG = Image("images/cg/Zygmunt_CG.png")

init python:
    config.searchpath.extend(["game/audio", "game/audio/combat music", "game/audio/dark magic music", "game/images/backgrounds"])
    renpy.music.register_channel("music2")

    # SHAKE EFFECT : Shake(position, duration, max distance)
    import math
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            self.start = [self.anchors.get(i,i) for i in start] # central position
            self.dist = dist                                    # max distance from start in pixels
            self.child = child
        def __call__(self, t, sizes):
            # turns float to int
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [fti(a,b) for a,b in zip(self.start, sizes)]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)
    Shake = renpy.curry(_Shake)

    # FLASH EFFECTS
    sshake = Shake((0, 0, 0, 0), 0.5, dist=15)      # for getting hit
    flash = Fade(0.1, 0.0, 0.25, color="#fff")      # flashes white
    pain = ComposeTransition(sshake, after=flash)    # pain flash
    fade = Fade(0.25, 0.5, 0.25, color="000")

    # STORY TRACKERS
    pronoun = "they"    # the pronouns chosen in ch1 s2
    bogdan = 0
    zygmunt = 0
    andia = 0
    songbird = 0

    ch1s8_buddy = "andia"   # who they spent time with in ch1 s8
    kissZygmunt = False     # true if you kiss Zygmunt in ch1
    ch2_buddy = "self"      # who they spent time with in ch2
    ch2_thief = False       # true if you steal with Zygmunt in ch2
    ch2_holdZygmunt = False # true if you hold hands with Zygmunt in ch2
    end_friendship = True   # false if you decide to persue a romance with a character
    end_buddy = "self"      # who you get locked into in ch 3
    killYarlomila = True    # False if you save yarlomila in ch 4

label start:
     # DEBUGGING
    screen debug():
        frame:
            xalign 0.1 ypos 50
            hbox:
                spacing 50
                vbox:
                    text "Bogdan"
                    text "[bogdan]"
                    textbutton "Add" action SetVariable("bogdan", bogdan+5)
                    textbutton "Remove" action SetVariable("bogdan", bogdan-5)
                vbox:
                    text "Andia"
                    text "[andia]"
                    textbutton "Add" action SetVariable("andia", andia+5)
                    textbutton "Remove" action SetVariable("andia", andia-5)
                vbox:
                    text "Zygmunt"
                    text "[zygmunt]"
                    textbutton "Add" action SetVariable("zygmunt", zygmunt+5)
                    textbutton "Remove" action SetVariable("zygmunt", zygmunt-5)
                vbox:
                    text "Songbird"
                    text "[songbird]"
                    textbutton "Add" action SetVariable("songbird", songbird+5)
                    textbutton "Remove" action SetVariable("songbird", songbird-5)

    # HIDE THIS FOR FINAL PROJECT
    show screen debug
    jump ch1_s1
