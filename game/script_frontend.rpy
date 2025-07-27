# defines here for Mono Clicker's functions
default persistent.mclick_firstrun = True
default mclick_points = 0
define starcookie = Image("gui/window_icon.png")

# saving persistents here
default persistent.mclickppcP = 0
default persistent.mclick_pointsP = 0
default persistent.mclickupgrade1costP = 100
default persistent.mclickupgrade1countP = 0
default persistent.mclickupgrade2costP = 1000
default persistent.mclickupgrade2countP = 0
default persistent.mclickupgrade3costP = 1000000
default persistent.mclickupgrade3countP = 0
default persistent.mclickupgrade4costP = 1000000
default persistent.mclickupgrade4countP = 0
default persistent.mclickupgradecc_costP = 10000000
default persistent.mclickupgradecc_countP = 0
default persistent.mclickupgrade5costP = 15000000
default persistent.mclickupgrade5countP = 0
default persistent.mclickupgrade1multcostP = 1000
default persistent.mclickupgrade1multcountP = 0
default persistent.mclickmultP = 1


# quick mafs here
default mclickppc = 1  # how many added points per click
define mclickmult = 1



# shop functions here
default mclickupgrade1cost = 100
default mclickupgrade1count = 0
default mclickupgrade2cost = 1000
default mclickupgrade2count = 0
default mclickupgrade3cost = 10000000
default mclickupgrade3count = 0
default mclickupgrade4cost = 10000000
default mclickupgrade4count = 0
default mclickupgrade5cost = 15000000
default mclickupgrade5count = 0
default mclickupgradecc_cost = 10000000
default mclickupgradecc_count = 0

# label triggers here

label mclicksave:
    $ persistent.mclickppcP = mclickppc
    $ persistent.mclickupgrade1costP = mclickupgrade1cost
    $ persistent.mclickupgrade1countP = mclickupgrade1count
    $ persistent.mclickupgrade2costP = mclickupgrade2cost
    $ persistent.mclickupgrade2countP = mclickupgrade2count
    $ persistent.mclickupgrade3costP = mclickupgrade3cost
    $ persistent.mclickupgrade3countP = mclickupgrade3count
    $ persistent.mclickupgrade4costP = mclickupgrade4cost
    $ persistent.mclickupgrade4countP = mclickupgrade4count
    $ persistent.mclickupgrade5costP = mclickupgrade5cost
    $ persistent.mclickupgrade5countP = mclickupgrade5count
    $ persistent.mclickupgradecc_costP = mclickupgradecc_cost
    $ persistent.mclickupgradecc_countP = mclickupgradecc_count
    $ persistent.mclick_pointsP = mclick_points
    $ renpy.notify("Save complete.")
    return

label mclickload:
    $ mclickppc = persistent.mclickppcP
    $ mclickupgrade1cost = persistent.mclickupgrade1costP
    $ mclickupgrade1count = persistent.mclickupgrade1countP
    $ mclickupgrade2cost = persistent.mclickupgrade2costP
    $ mclickupgrade2count = persistent.mclickupgrade2countP
    $ mclickupgrade3cost = persistent.mclickupgrade3costP
    $ mclickupgrade3count = persistent.mclickupgrade3countP
    $ mclickupgrade4cost = persistent.mclickupgrade4costP
    $ mclickupgrade4count = persistent.mclickupgrade4countP
    $ mclickupgrade5cost = persistent.mclickupgrade5costP
    $ mclickupgrade5count = persistent.mclickupgrade5countP
    $ mclickupgradecc_cost = persistent.mclickupgradecc_costP
    $ mclickupgradecc_count = persistent.mclickupgradecc_countP
    $ mclick_points = persistent.mclick_pointsP
    $ renpy.notify("Load complete.")
    jump monoclicker

label mclickwipe:
    $ persistent.mclickppcP = 0
    $ persistent.mclick_pointsP = 0
    $ persistent.mclickupgrade1costP = 100
    $ persistent.mclickupgrade1countP = 0
    $ persistent.mclickupgrade2costP = 1000
    $ persistent.mclickupgrade2countP = 0
    $ persistent.mclickupgrade3costP = 1000000
    $ persistent.mclickupgrade3countP = 0
    $ persistent.mclickupgrade4costP = 1000000
    $ persistent.mclickupgrade4countP = 0
    $ persistent.mclickupgradecc_costP = 10000000
    $ persistent.mclickupgradecc_countP = 0
    $ persistent.mclickupgrade5costP = 15000000
    $ persistent.mclickupgrade5countP = 0
    $ persistent.mclick_firstrun = True
    return


label mclicked:
    $ mclick_clicked(1 * mclickmult)
    return

label upgrade1multlb:
    $ upgrade1mult()
    return

label upgrade1lb:
    $ upgrade1()
    return

label upgrade2lb:
    $ upgrade2()
    return

label upgrade3lb:
    $ upgrade3()
    return

label upgrade4lb:
    $ upgrade4()
    return

label upgrade5lb:
    $ upgrade5()
    return

label upgradecclb:
    $ upgradecc()
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
            text "Current Points per Clicks: [mclickppc] ([mclickmult]x)"

    hbox:
        align (0.5, 0.75)
        textbutton "Save Progress" action Call("mclicksave")
        textbutton "Nuke Progress" action [CConfirm("Are you sure you want to wipe your Mono Clicker progress?", yes=Jump("mclickwipe"))]
    hbox:
        align (0.5, 0.82)
        textbutton "Review First Time Message" action NotifyALT("Welcome to Mono Clicker! \n\nIn this minigame, you need to click on the star in order to get Mono Points. \nMore upgrades means more Mono Points, but they get expensive overtime. \nAuto-saving is possible here, but you might need to press the Save Progress button if the progress isn't saved. \nTo unlock more upgrades, all of the upgrades must be upgraded to a specific high level. \nCan you reach 100 million for an achievement? \nCheers to you if you reached 100 billion for a star. \n{color=#ff0000}BE WARNED; THIS MINIGAME IS HARD, THUS REQUIRING A LOT OF TIME.{/color}")

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
                if mclickupgrade1count >= 20:
                    textbutton "MPPC++ (+10) \nCost: [mclickupgrade2cost] MP" action Call("upgrade2lb")
                if mclickupgrade1count >= 100 and mclickupgrade2count >= 50:
                    textbutton "MPPC+++ (+100) \nCost: [mclickupgrade3cost] MP" action Call("upgrade3lb")
                    textbutton "Clear Clouds \nCost: [mclickupgradecc_cost] MP" action Call("upgradecclb")
                if mclickupgrade1count >= 100 and mclickupgrade2count >= 100 and mclickupgrade3count >= 10:
                    textbutton "MPPC+++ Pro Max (+500) \nCost: [mclickupgrade4cost] MP" action Call("upgrade4lb")
                    textbutton "Kuroshoko Plushies (+1250) \nCost: [mclickupgrade5cost] MP" action Call("upgrade5lb")
    frame:
        align (1.0, 0.5)
        xysize (350, 500)
        vbox:
            text "--- One-time Upgrades Bought ---"
            if mclickupgradecc_count >= 1:
                text "Clear Clouds ACTIVE"
            text "--- Multi-upgrade Levels ---"
            text "MPPC+ Level: [mclickupgrade1count]"
            if mclickupgrade1count >= 20:
                text "MPPC++ Level: [mclickupgrade2count]"
            if mclickupgrade1count >= 100 and mclickupgrade2count >= 50:
                text "MPPC+++ Level: [mclickupgrade3count]"
            if mclickupgrade1count >= 100 and mclickupgrade2count >= 100 and mclickupgrade3count >= 10:
                text "MPPC+++ Pro Max Level: [mclickupgrade4count]"
                text "Kuroshoko Plushies Level: [mclickupgrade5count]"
        



# inits here
init python:
    

    def mclick_clicked(points):
        global mclickppc
        global mclick_points

        mclickppctrig = mclickppc * mclickmult


        mclick_points += points + mclickppctrig

        

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

    def upgrade1mult():
        global mclickupgrade1multcost
        global mclickmult
        global mclick_points
        global mclickupgrade1multcount

        if mclickupgrade1multcount >= 100:
                renpy.sound.play("audio/systemerr.ogg", channel = "audio")
                renpy.notify("Dupe I is on max level.")
                mclickupgrade1count = 100

        elif mclick_points >= mclickupgrade1multcost:
            renpy.sound.play("audio/karmaup.ogg", channel = "audio")
            mclick_points -= mclickupgrade1multcost
            mclickupgrade1multcount += 1
            mclickmult += 1
            mclickupgrade1multcost += 1000

        else:
            renpy.notify("Insufficient Mono Points.")

    def upgrade2():
        global mclickupgrade2cost
        global mclickppc
        global mclick_points
        global mclickupgrade2count

        if mclickupgrade2count >= 100:
                renpy.sound.play("audio/systemerr.ogg", channel = "audio")
                renpy.notify("MPPC++ is on max level.")
                mclickupgrade2count = 100

        elif mclick_points >= mclickupgrade2cost:
            renpy.sound.play("audio/karmaup.ogg", channel = "audio")
            mclick_points -= mclickupgrade2cost
            mclickupgrade2count += 1
            mclickppc += 10
            mclickupgrade2cost += 100

        else:
            renpy.notify("Insufficient Mono Points.")

    def upgrade3():
        global mclickupgrade3cost
        global mclickppc
        global mclick_points
        global mclickupgrade3count

        if mclickupgrade3count >= 100:
                renpy.sound.play("audio/systemerr.ogg", channel = "audio")
                renpy.notify("MPPC+++ is on max level.")
                mclickupgrade3count = 100

        elif mclick_points >= mclickupgrade3cost:
            renpy.sound.play("audio/karmaup.ogg", channel = "audio")
            mclick_points -= mclickupgrade3cost
            mclickupgrade3count += 1
            mclickppc += 100
            mclickupgrade3cost += 100000

        else:
            renpy.notify("Insufficient Mono Points.")

    def upgrade4():
        global mclickupgrade4cost
        global mclickppc
        global mclick_points
        global mclickupgrade4count
        

        if mclickupgrade4count >= 100:
                renpy.sound.play("audio/systemerr.ogg", channel = "audio")
                renpy.notify("MPPC+++ Pro Max is on max level.")
                mclickupgrade4count = 100

        elif mclick_points >= mclickupgrade4cost:
            renpy.sound.play("audio/karmaup.ogg", channel = "audio")
            mclick_points -= mclickupgrade4cost
            mclickupgrade4count += 1
            mclickppc += 500
            mclickupgrade4cost += 500000

        else:
            renpy.notify("Insufficient Mono Points.")

    def upgrade5():
        global mclickupgrade5cost
        global mclickppc
        global mclick_points
        global mclickupgrade5count
        

        if mclickupgrade5count >= 100:
                renpy.sound.play("audio/makka.ogg", channel = "audio")
                renpy.notify("Kuroshoko Plushies is on max level, nya! o~o")
                mclickupgrade5count = 100
        elif mclick_points >= mclickupgrade5cost:
            renpy.sound.play("audio/makka.ogg", channel = "audio")
            mclick_points -= mclickupgrade5cost
            mclickupgrade5count += 1
            mclickppc += 1250
            mclickupgrade5cost += 1000000

        else:
            renpy.sound.play("audio/karmadown.ogg", channel = "audio")
            renpy.notify("Inshyaficient Monyao Points... d-_-b")

    def upgradecc():
        global mclickupgradecc_cost
        global mclickppc
        global mclick_points
        global mclickupgradecc_count

        if mclickupgradecc_count is not 0:
            renpy.sound.play("audio/systemerr.ogg", channel = "audio")
            renpy.notify("Clear Clouds is on max level.")

        elif mclick_points >= mclickupgradecc_cost:
            renpy.sound.play("audio/karmaup.ogg", channel = "audio")
            mclick_points -= mclickupgradecc_cost
            mclickupgradecc_count += 1
            mclickppc += 1000

        else:
            renpy.notify("Insufficient Mono Points.")