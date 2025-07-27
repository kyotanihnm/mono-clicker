init python:
    def bleep_mono(event, **kwargs):
            if event == "show_done":
                renpy.music.play("audio/bleep_mono.ogg", channel="sound", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound", fadeout=1)
