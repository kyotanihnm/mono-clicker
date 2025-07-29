# defines here for Mono Clicker's functions
default persistent.mclick_firstrun = True
default mclick_points = 0
define starcookie = Image("gui/window_icon.png")

# saving persistents here
default persistent.mclickppcP = 0
default persistent.mclick_pointsP = 0
default persistent.mclickupgrade1costP = 100
default persistent.mclickupgrade1countP = 0


# quick mafs here
default mclickppc = 1  # how many added points per click



# shop functions here
default mclickupgrade1cost = 100
default mclickupgrade1count = 0

# label triggers here

label mclicksave:
    $ persistent.mclickppcP = mclickppc
    $ persistent.mclickupgrade1costP = mclickupgrade1cost
    $ persistent.mclickupgrade1countP = mclickupgrade1count
    return

label mclickload:
    $ mclickppc = persistent.mclickppcP
    $ mclickupgrade1cost = persistent.mclickupgrade1costP
    $ mclickupgrade1count = persistent.mclickupgrade1countP
    jump monoclicker

label mclickwipe:
    $ persistent.mclickppcP = 0
    $ persistent.mclick_pointsP = 0
    $ persistent.mclickupgrade1costP = 100
    $ persistent.mclickupgrade1countP = 0
    return


label mclicked:
    $ mclick_clicked(1 * mclickmult)
    return


label upgrade1lb:
    $ upgrade1()
    return



# Mono Clicker overlays here
screen monoclickeroverlay:
    key "skip" action NotifyALT("Skipping here is not possible in Mono Clicker.")
    key "toggle_skip" action NotifyALT("Skipping here is not possible in Mono Clicker.")
    key "fast_skip" action NotifyALT("Skipping here is not possible in Mono Clicker.")

    vbox:
        align (0.5, 0.5)
        imagebutton:
            idle starcookie
            hover starcookie
            hover_sound "audio/hover.wav"
            activate_sound "audio/buttonon.ogg"
            action Call("mclicked")
    vbox:
        align (0.5, 0.25)
        frame:
            text "Mono Points: [mclick_points]"
    
    vbox:
        align (0.5, 0.20)
        frame:
            text "Current Points per Clicks: [mclickppc]"

    hbox:
        align (0.5, 0.75)
        textbutton "Save Progress" action Call("mclicksave")
        textbutton "Nuke Progress" action [CConfirm("Are you sure you want to wipe your Mono Clicker progress?", yes=Jump("mclickwipe"))]
    hbox:
        align (0.5, 0.82)
        textbutton "Review First Time Message" action NotifyALT("Welcome to Mono Clicker! \n\nIn this minigame, you need to click on the star in order to get Mono Points. \nMore upgrades means more Mono Points, but they get expensive overtime. \nAuto-saving is possible here, but you might need to press the Save Progress button if the progress isn't saved. \nTo unlock more upgrades, all of the upgrades must be upgraded to a specific high level.")

    hbox:
        align (0.5, 1.0)
        if persistent.gm == True:
            textbutton "Infinite MP" action SetVariable("mclick_points", 999999999999999999)
            textbutton "Reset MP" action SetVariable("mclick_points", 0)
            textbutton "Reset 4th Star" action SetVariable("persistent.star4unlocked", False)
    


# upgrade overlay
screen monoclickeroverlay2:

    frame:
        align (0.0, 0.5)
        xysize (350, 500)
        vbox:
            viewport:
                mousewheel True draggable True pagekeys True
                scrollbars "vertical"
                has vbox
                textbutton "MPPC+ (+1) \nCost: [mclickupgrade1cost] MP" action Call("upgrade1lb")
    frame:
        align (1.0, 0.5)
        xysize (350, 500)
        vbox:
            text "--- One-time Upgrades Bought ---"
            text "--- Multi-upgrade Levels ---"
            text "MPPC+ Level: [mclickupgrade1count]"
        



# inits here
init python:
    

    def mclick_clicked(points):
        global mclickppc
        global mclick_points

        mclickppctrig = mclickppc

        

    def upgrade1():
        global mclickupgrade1cost
        global mclickppc
        global mclick_points
        global mclickupgrade1count

        if mclickupgrade1count >= 100:
                renpy.sound.play("audio/systemerr.ogg", channel = "audio")
                renpy.notify("MPPC+ is on max level.")
                mclickupgrade1count = 100

        elif mclick_points >= mclickupgrade1cost:
            renpy.sound.play("audio/karmaup.ogg", channel = "audio")
            mclick_points -= mclickupgrade1cost
            mclickupgrade1count += 1
            mclickppc += 1
            mclickupgrade1cost += 10

        else:
            renpy.notify("Insufficient Mono Points.")
