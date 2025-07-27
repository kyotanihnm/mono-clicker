label start:
    if persistent.mclick_firstrun == True:
        jump mclickload
    else:
        jump mclickload


label monoclicker:
    show screen monoclickeroverlay
    show screen monoclickeroverlay2
    if mclickupgradecc_count == 1:
        scene monotemple2
    else:
        scene monotemple
    pause
    jump monoclicker