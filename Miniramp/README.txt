MINI RAMP - a tiny pixel-art skate game (works fully offline)
=============================================================

HOW TO PLAY LOCALLY
  1. Unzip this folder anywhere (keep the folders together).
  2. Double-click index.html (Chrome, Edge, Firefox or Safari).
  No internet, server or install needed: the game code, your character sprite
  and the pixel font are all inside this folder.

MENUS
  Space / START ... title -> level select -> gear menu -> start the run
  Esc / MENU ...... back to the main menu from anywhere
  Level select: left/right.  Gear menu: up/down pick a row, left/right change it.

RIDING
  Left / Right ..... pump on the ramp
  Up / Down ........ ride toward the back / front (while rolling fast or in the air)

AIR TRICKS
  A ........ kickflip      (A+Right heelflip, A+Down shove-it, A+Up FS shove-it)
             hold A or tap again for double / triple / quad flips and 360, 540...
             shove-its
  D ........ grab          (D+Down indy, D+Up melon, D+Right nose, D+Left tail)
  S ........ spin          hold S to keep spinning (every 180 counts, up to 1440),
                           release to finish the turn; each tap also adds 180
  Landing mid-trick = wipeout.

COPING (press W near the top of the wall)
  Moving toward the back/front of the ramp (up/down held):
     W = 50-50 grind, W+Right = nose slide, W+Left = tail slide (they slide along the coping)
  Not moving that way (e.g. hovering above the coping):
     W = rock stall, W+Right = nose stall, W+Left = tail stall
     (keep the balance marker off the far end with left/right)
  Release W to drop back into the ramp. Stalls and grinds need enough speed to
  reach the coping, and each wall allows one until you ride across the flat bottom.

FILES
  index.html ................ the whole game
  assets/fonts/ ............. Press Start 2P pixel font (SIL Open Font License, see OFL.txt)
  assets/Player.png ......... your original character sprite (reference / editing)
  assets/Player_Idle.png .... your original idle animation (APNG)

NOTES
  - Your gear, level and a custom background (BG IMAGE button) are saved in the
    browser's local storage on that computer.
  - The character frames are embedded in index.html (the B64 list). To use a new
    sprite, replace those frames with your own 24x24 PNGs, or ask me to do it.
