# Ran before the discord namespace init present inside rich_presence.rpy on -950.
init offset = -960

# Application Id - This is gotten from Discord's Developer Portal. 
# Process of setting up everything on the Portal is described on this project's GitHub page under the Wiki tab, or locally in discord_developer_portal.md
define discord.application_id = ""
# (github exclusive) hmmm, i wonder where did that app id went (put it yourself, i removed it for the public lol)

#####################################################################################################################################

# State of the Presence upon the game's launch and return to the main menu..
define discord.main_menu_state = {"state" : "not in mono clicker dx",
                                "large_image" : "state0",
                                "details" : "i'm not clickin' it",
                                "large_text" : "in-game"}

# State of the Presence when the game is started.
define discord.start_state = {"state" : "in mono clicker dx",
                                "large_image" : "state1",
                                "details" : "i'm clickin' it",
                                "large_text" : "in-game"}
define discord.start_label = "start"
define discord.main_menu_label = "splashscreen"
# The state is a Dict with all the properties of the presence state displayed when the game is launched.
# keys correspond not to Presence Fields, but to pypresence arguments! 
# They are all well described in Readme, but here is a cheat sheet from pypresence documentation:
#
# state (str) – the user’s current status
# details (str) – what the player is currently doing
# start (int) – epoch time for game start or None to hide Time Elapsed ## In this code can also be "start_time" (default) or "new_time"
# end (int) – epoch time for game end
# large_image (str) – name of the uploaded image for the large profile artwork
# large_text (str) – tooltip for the large image
# small_image (str) – name of the uploaded image for the small profile artwork
# small_text (str) – tootltip for the small image
# party_size (list) – current size of the player’s party, lobby, or group, and the max in this format: [1,4]
# buttons (list) – list of up to two dicts for buttons, in the format {"label": "My Website", "url": "https://qtqt.cf"}

# Name of the label that should update Presence to `start_state` when entered.
# Can also be a list label names, if you have multiple start labels. 

#####################################################################################################################################

# These variables control the print functions across this script. They work if True, they're ignored if False.
# Prints are shown inside game's console (if turned on in the Ren'Py Launcher) and in the game's log.txt file.
define discord.log_important = True # Shows whether the Presence was initialized and closed correctly.
define discord.log_properties = True # Records properties whenever they change with set or update methods.
define discord.log_restore = True # Notes whenever the properties get rolled back or loaded from a save file, and what they were restored into.