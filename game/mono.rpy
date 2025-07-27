define monoko = Character(_('Mono Kuroko'), color="#969696", ctc="ctc_blink", ctc_position="fixed", callback=bleep_mono)

image ctc_blink:
    "gui/ctc.png"
    subpixel True
    alpha 0.0 xalign 0.815 yalign 0.980
    linear 0.25 alpha 1.0 xalign 0.825 yalign 0.980

image mono idle:
    "images/char/mono idle_1.png"
    pause(1.85)
    "images/char/mono idle_2.png"
    pause(0.15)
    repeat

image mono talk:
    "images/char/mono talk_1.png"
    pause(1.85)
    "images/char/mono talk_2.png"
    pause(0.15)
    repeat

image mono talk2:
    "images/char/mono talk2_1.png"
    pause(1.85)
    "images/char/mono talk2_2.png"
    pause(0.15)
    repeat

image chocolamc:
    "images/char/kuroshoko1.png"
    pause(1.85)
    "images/char/kuroshoko2.png"
    pause(0.15)
    repeat