transform trans_blur:
    blur 0.5

transform com_appear:
    on show:
        alpha 0
        linear .15 alpha 1.0

transform errblink:
    on show:
        matrixcolor TintMatrix("#ff0000") alpha 1
        pause(.5)
        matrixcolor TintMatrix("#ff0000") alpha 0
        pause(.5)
        repeat

transform textblink:
    on show:
        alpha 1
        pause(.5)
        alpha 0
        pause(.5)
        repeat

transform livesbtntransform:
    matrixcolor TintMatrix("#09b200")
    linear 0.75 matrixcolor TintMatrix("#067500")
    repeat
    # fine hp shader

transform livesbtntransform2:
    matrixcolor TintMatrix("#b4ae00")
    linear 0.5 matrixcolor TintMatrix("#2d2c00")
    repeat
    # caution hp shader

transform livesbtntransform3:
    matrixcolor TintMatrix("#b40000")
    linear 0.25 matrixcolor TintMatrix("#2d0000")
    repeat
    # crit hp shader

transform livesbtntransform4:
    matrixcolor TintMatrix("#ffffff")
    # ded

transform leftdissolve:
    on show:
        align (0, 1.0) alpha 0.0
        linear 0.15 align (0.025, 1.0) alpha 1
    on hide:
        align (0.025, 1.0) alpha 1
        linear 0.15 align (0.035, 1.0) alpha 0
        # alternative to the Dissolve() transform, that pmo because it delays between dialogue >:(

transform leftimmediatehide:
    on hide:
        align (0.025, 1.0) alpha 1
        linear 0.001 align (0.025, 1.0) alpha 0.0

transform shimondissolve:
    on hide:
        align (0.025, 1.0) alpha 1
        linear 0.15 align (0.025, 1.0) alpha 0
        # Shimon's dissolve for choosing No after death where this mysterious guy asks you to continue or not

transform expression_shake:
    xpos (0.015)
    linear 0.05 xpos (0.035)
    linear 0.05 xpos (0.015)
    linear 0.05 xpos (0.035)
    linear 0.05 xpos (0.015)
    linear 0.05 xpos (0.035)
    align (0.025, 1.0)
    on hide:
        align (0.025, 1.0) alpha 1
        linear 0.15 align (0.035, 1.0) alpha 0
    # replication of the blue archive shaking, but i tried

transform expression_jump:
    linear 0.05 ypos (0.99)
    linear 0.05 ypos (0.95)
    linear 0.05 ypos (0.99)
    align (0.025, 1.0)
    on hide:
        align (0.025, 1.0) alpha 1
        linear 0.15 align (0.035, 1.0) alpha 0
    # 2nd blue archive image anim replication


transform expression_slidedown:
    ypos (1.01)
    linear 0.15 ypos (1.05)
    pause (0.50)
    linear 0.15 ypos 1.0
    on hide:
        align (0.025, 1.0) alpha 1
        linear 0.15 align (0.035, 1.0) alpha 0
    # 3rd blue archive image anim replication, used for picking up stuff or laying down for a while, idk :o

transform expression_dashright:
    xalign 0.025
    linear 0.15 xalign 1.75
    # slide to the right, then cris cross (possibly cha cha real smooth on these transforms)

transform expression_dashleft:
    xalign 0.025
    linear 0.15 xalign -0.75
    # slide to the left

transform expression_leaveright:
    alpha 1.0 xalign 0.025
    linear 0.15 alpha 0.0 xalign 0.50
    # alternative to the expression_dashright, indicated for leaving the room

transform lowhpframeflash:
        alpha 1.0
        linear 0.75 alpha 0.1
        repeat
    # :MYEYES:

transform leftdissolvesplash:
    on show:
        align (0, 1.0) alpha 0.0
        linear 0.15 align (0.005, 1.0) alpha 1
    on hide:
        align (0.005, 1.0) alpha 1
        linear 0.15 align (0.020, 1.0) alpha 0
        # alternative to leftdissolve, Kanashi just pmo that he collides with the TWT splash title :(

transform rightdissolvesplash:
    on show:
        align (1.0, 1.0) alpha 0.0
        linear 0.15 align (0.995, 1.0) alpha 1
    on hide:
        align (0.995, 1.0) alpha 1
        linear 0.15 align (0.980, 1.0) alpha 0
        # for Green Kensei, rightdissolve doesn't exist in gameplay :)

transform dissolve2:
    on show:
        xalign 0.45 alpha 0.0
        linear 0.25 xalign 0.50 alpha 1
    on hide:
        xalign 0.50 alpha 1 zoom 1.0
        linear 0.25 alpha 0 zoom 1.25

transform dissolve2alt:
    on show:
        xalign 0.515 alpha 0.0
        linear 0.25 xalign 0.50 alpha 1
    on hide:
        xalign 0.50 alpha 1
        linear 0.25 xalign 0.515 alpha 0

transform menubuttontransform:
    alpha 0.0
    linear 0.25 alpha 1


transform dissolve2alt2:
    on show:
        alpha 0.0
        pause(0.15)
        linear 0.05 alpha 1
    on hide:
        alpha 1
        linear 0.05 alpha 0

transform dissolve2alt3:
    on show:
        alpha 0.0
        pause(0.15)
        linear 0.05 alpha 1
    on hide:
        alpha 1 zoom 1.0
        linear 0.10 alpha 0 zoom 1.10
        

transform pausetext:
    on show:
        align (0.0, 0.05) alpha 0
        linear 0.25 align (0.05, 0.05) alpha 1

    on hide:
        align (0.05, 0.05) alpha 1
        linear 0.25 align (0.10, 0.05) alpha 0

transform pbtdissolve:
    on show:
        alpha 0
        linear 0.25 alpha 1

    on hide:
        alpha 1
        linear 0.25  alpha 0


transform dissolvezoom:
    on show:
        zoom 0.0
        linear 0.25 zoom 1

    on hide:
        zoom 1
        linear 0.25  zoom 0

transform fastzoom:
    on show:
        zoom 0.0
        linear 0.10 zoom 1

    on hide:
        zoom 1
        linear 0.10 zoom 0

transform menuhoverdissolve:
    on show:
        alpha 0.0
        linear 0.15 alpha 1
    on hide:
        alpha 1 zoom 1.0
        linear 0.25 alpha 0 zoom 1.15

transform qmhdissolve:
    on show:
        yalign 0.985 alpha 0.0
        linear 0.15 yalign 0.975 alpha 1

transform menuicondissolve:
    on show:
        align (0.75, 0.5) alpha 0.0
        linear 0.15 align (0.85, 0.5) alpha 1

transform choicetrans:
    on show:
        alpha 0.0
        linear 0.15 alpha 1.0


transform psfade():
    on show:
        alpha 0
        linear 0.25 alpha 1
    on hide:
        alpha 1
        linear 0.25 alpha 0

transform delayed_blink2(delay, cycle):
    on show:
        zoom 0.0
        pause(0.015)
        zoom 0.40
        pause(0.015)
        zoom 0.60
        pause(0.015)
        zoom 0.75
        pause(0.015)
        zoom 0.80
        pause(0.015)
        zoom 0.90
        pause(0.015)
        zoom 0.92
        pause(0.015)
        zoom 0.96
        pause(0.015)
        zoom 0.98
        pause(0.015)
        zoom 1

    on hide:
        zoom 1
        pause(0.025)
        zoom 0.98
        pause(0.025)
        zoom 0.96
        pause(0.025)
        zoom 0.94
        pause(0.025)
        zoom 0.92
        pause(0.025)
        zoom 0.90
        pause(0.025)
        zoom 0.85
        pause(0.025)
        zoom 0.80
        pause(0.025)
        zoom 0.75
        pause(0.025)
        zoom 0.70
        pause(0.025)
        zoom 0.60
        pause(0.025)
        zoom 0.40
        pause(0.025)
        zoom 0.20
        pause(0.025)
        zoom 0
    
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat