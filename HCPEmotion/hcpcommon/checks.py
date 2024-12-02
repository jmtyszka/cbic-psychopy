import pyglet
from psychopy import gui, logging, core

def checkScreenCount():
    '''Present a dialog if there are less than 2 screens present.'''
    display = pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    if len(screens) < 2:
        dlg = buildScreenCountWarning()
        dlg.show()
        if not dlg.OK:
            logging.exp('User Cancelled')
            core.quit()  # user pressed cancel
        else:
            logging.exp('User continued anyway')


def buildScreenCountWarning():
    '''Build a Screen Count Warning Dialog'''
    dlg = gui.Dlg(title='Monitor Count Warning')
    dlg.addText('WARNING: Only 1 screen was found.')
    dlg.addText('This task is meant to be run with two screens.')
    dlg.addText('We recommend you hit "Cancel" to stop the task and plug' +
                ' in an external monitor.')
    dlg.addText('If you really want to continue with just 1 screen, hit "OK".')
    return dlg


def frameRateWarning():
    dlg = gui.Dlg(title='Frame Rate Warning')
    dlg.addText('WARNING: Frame rate seems too high or too low.')
    dlg.addText('Press "OK" to continue or "Cancel" to stop.')
    dlg.addFixedField('Measured Frame Rate', expInfo['frameRate'])
    dlg.addText('#'*40)
    dlg.addText('This may be caused by background processes or')
    dlg.addText('incorrect screen settings.')
    dlg.addText('')
    dlg.addText('If this is the first time seeing this message, you should:')
    dlg.addText('1. Cancel this run')
    dlg.addText('2. Close anything running in the background.')
    dlg.addText('3. Check that the screen refresh rate is correct.')
    dlg.addText('4. Re-run the script and try again.')
    dlg.addText('')
    return dlg
