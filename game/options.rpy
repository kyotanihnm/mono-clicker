﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("mono clicker dx")
# i'm using this name to look like a Japanese game, but it's not >:(


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False
# this config pmo (it's ugly anyways)


## The version of the game.

define config.version = "1.0"
# 1.0 when


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.



define gui.about = _p("""Developed by kyonezumi (aka kyotani) at The Hananezumi Project. Visit hananezumi.itch.io for more.""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "monoclicker"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "audio/menu.ogg"
define config.main_menu_music_fadein = 0.25


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = Dissolve(.1)
define config.exit_transition = Dissolve(.2)
define config.game_main_transition = Dissolve(.15)


## Between screens of the game menu.

define config.intra_transition = Dissolve(.1)


## A transition that is used after a game has been loaded.

define config.after_load_transition = Dissolve(.1)


## Used when entering the main menu after the game has ended.

define config.end_game_transition = Dissolve(.15)

## Confirmation transits.

define config.enter_yesno_transition = Dissolve(.1)
define config.exit_yesno_transition = Dissolve(.1)


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.15)
define config.window_hide_transition = Dissolve(.15)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 25


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 3


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "monoclicker-57290305928"
# i just typed what random numbers i can think of :)


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"
# jarate star on the top-left


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.



    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('cache/**', None)
    build.classify('saves/**', None)
    build.classify('game/**.rpy', None) # sorry, no peeking at the source code


    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')



## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

define build.itch_project = "hananezumi/monoclickerdx"
# i wonder what this thing do if i insta-publish it with a single button on the Build Distributions menu




## Custom defines/defaults here. (just to make sure everything i modified is here because i'm stupid
## to find everything)
define config.has_autosave = False ## unnecessary as Mono Clicker DX has an auto-save on quit feature
define config.developer = True ## disabled after i finished a update, don't switch this if you don't want to break the damn game
define config.end_splash_transition = Dissolve(0.15) ## used to transit after splash.rpy, do not even touch this >:(
define config.rollback_enabled = False ## something to prevent cheating, i guess

init -10 python:
    gui.init(1280, 720) # resizes into it's actual size when wiping data, all that shizz
define config.check_conflicting_properties = True # idk what this means, but i guess this is checking conflict crap on configs
define config.default_textshader = "typewriter" # do not remove, the game will be mad if no textshader is used on default like a typewriter