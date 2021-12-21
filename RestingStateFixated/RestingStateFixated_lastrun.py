#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on December 21, 2021, at 11:52
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'RestingStateFixated'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jmt\\Documents\\GitHub\\cbic-psychopy\\RestingStateFixated\\RestingStateFixated_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionsText = visual.TextStim(win=win, name='InstructionsText',
    text='Stay awake and look at the cross\nTry to keep as still as possible\nThis scan lasts about eight minutes.\n\nPRESS ANY KEY TO CONTINUE',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey = keyboard.Keyboard()

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
FixationCross = visual.ShapeStim(
    win=win, name='FixationCross', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
QuitKey = keyboard.Keyboard()

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
ThanksText = visual.TextStim(win=win, name='ThanksText',
    text='The scan is complete!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
ContinueKey.keys = []
ContinueKey.rt = []
_ContinueKey_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsText, ContinueKey]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsText* updates
    if InstructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsText.frameNStart = frameN  # exact frame index
        InstructionsText.tStart = t  # local t and not account for scr refresh
        InstructionsText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsText, 'tStartRefresh')  # time at next scr refresh
        InstructionsText.setAutoDraw(True)
    
    # *ContinueKey* updates
    waitOnFlip = False
    if ContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueKey.frameNStart = frameN  # exact frame index
        ContinueKey.tStart = t  # local t and not account for scr refresh
        ContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueKey, 'tStartRefresh')  # time at next scr refresh
        ContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = ContinueKey.getKeys(keyList=None, waitRelease=False)
        _ContinueKey_allKeys.extend(theseKeys)
        if len(_ContinueKey_allKeys):
            ContinueKey.keys = _ContinueKey_allKeys[-1].name  # just the last key pressed
            ContinueKey.rt = _ContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionsText.started', InstructionsText.tStartRefresh)
thisExp.addData('InstructionsText.stopped', InstructionsText.tStopRefresh)
# check responses
if ContinueKey.keys in ['', [], None]:  # No response was made
    ContinueKey.keys = None
thisExp.addData('ContinueKey.keys',ContinueKey.keys)
if ContinueKey.keys != None:  # we had a response
    thisExp.addData('ContinueKey.rt', ContinueKey.rt)
thisExp.addData('ContinueKey.started', ContinueKey.tStartRefresh)
thisExp.addData('ContinueKey.stopped', ContinueKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation"-------
continueRoutine = True
routineTimer.add(480.000000)
# update component parameters for each repeat
QuitKey.keys = []
QuitKey.rt = []
_QuitKey_allKeys = []
# keep track of which components have finished
FixationComponents = [FixationCross, QuitKey]
for thisComponent in FixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Fixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FixationCross* updates
    if FixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FixationCross.frameNStart = frameN  # exact frame index
        FixationCross.tStart = t  # local t and not account for scr refresh
        FixationCross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FixationCross, 'tStartRefresh')  # time at next scr refresh
        FixationCross.setAutoDraw(True)
    if FixationCross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > FixationCross.tStartRefresh + 480-frameTolerance:
            # keep track of stop time/frame for later
            FixationCross.tStop = t  # not accounting for scr refresh
            FixationCross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FixationCross, 'tStopRefresh')  # time at next scr refresh
            FixationCross.setAutoDraw(False)
    
    # *QuitKey* updates
    waitOnFlip = False
    if QuitKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        QuitKey.frameNStart = frameN  # exact frame index
        QuitKey.tStart = t  # local t and not account for scr refresh
        QuitKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(QuitKey, 'tStartRefresh')  # time at next scr refresh
        QuitKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(QuitKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(QuitKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if QuitKey.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > QuitKey.tStartRefresh + 480-frameTolerance:
            # keep track of stop time/frame for later
            QuitKey.tStop = t  # not accounting for scr refresh
            QuitKey.frameNStop = frameN  # exact frame index
            win.timeOnFlip(QuitKey, 'tStopRefresh')  # time at next scr refresh
            QuitKey.status = FINISHED
    if QuitKey.status == STARTED and not waitOnFlip:
        theseKeys = QuitKey.getKeys(keyList=['q'], waitRelease=False)
        _QuitKey_allKeys.extend(theseKeys)
        if len(_QuitKey_allKeys):
            QuitKey.keys = _QuitKey_allKeys[-1].name  # just the last key pressed
            QuitKey.rt = _QuitKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fixation"-------
for thisComponent in FixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FixationCross.started', FixationCross.tStartRefresh)
thisExp.addData('FixationCross.stopped', FixationCross.tStopRefresh)
# check responses
if QuitKey.keys in ['', [], None]:  # No response was made
    QuitKey.keys = None
thisExp.addData('QuitKey.keys',QuitKey.keys)
if QuitKey.keys != None:  # we had a response
    thisExp.addData('QuitKey.rt', QuitKey.rt)
thisExp.addData('QuitKey.started', QuitKey.tStartRefresh)
thisExp.addData('QuitKey.stopped', QuitKey.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "Thanks"-------
continueRoutine = True
routineTimer.add(5.500000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [ThanksText]
for thisComponent in ThanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThanksText* updates
    if ThanksText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        ThanksText.frameNStart = frameN  # exact frame index
        ThanksText.tStart = t  # local t and not account for scr refresh
        ThanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThanksText, 'tStartRefresh')  # time at next scr refresh
        ThanksText.setAutoDraw(True)
    if ThanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ThanksText.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            ThanksText.tStop = t  # not accounting for scr refresh
            ThanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ThanksText, 'tStopRefresh')  # time at next scr refresh
            ThanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ThanksText.started', ThanksText.tStartRefresh)
thisExp.addData('ThanksText.stopped', ThanksText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
