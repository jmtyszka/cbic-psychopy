#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on December 19, 2021, at 10:30
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
expName = 'WaitForTrigger'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\miket\\OneDrive\\Documents\\GitHub\\cbic-psychopy\\WaitForTrigger\\WaitForTrigger_lastrun.py',
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

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()
TriggerDetect = keyboard.Keyboard()
WaitText = visual.TextStim(win=win, name='WaitText',
    text='Waiting for trigger …',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
Fixation_Cross = visual.ShapeStim(
    win=win, name='Fixation_Cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='lightgray', fillColor='lightgray',
    opacity=1.0, depth=0.0, interpolate=False)
TriggerDetectedText = visual.TextStim(win=win, name='TriggerDetectedText',
    text='Trigger detected!',
    font='Arial',
    pos=(0, 0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WaitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
TriggerDetect.keys = []
TriggerDetect.rt = []
_TriggerDetect_allKeys = []
# keep track of which components have finished
WaitForTriggerComponents = [TriggerDetect, WaitText]
for thisComponent in WaitForTriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitForTriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WaitForTrigger"-------
while continueRoutine:
    # get current time
    t = WaitForTriggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitForTriggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TriggerDetect* updates
    waitOnFlip = False
    if TriggerDetect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TriggerDetect.frameNStart = frameN  # exact frame index
        TriggerDetect.tStart = t  # local t and not account for scr refresh
        TriggerDetect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerDetect, 'tStartRefresh')  # time at next scr refresh
        TriggerDetect.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(TriggerDetect.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(TriggerDetect.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if TriggerDetect.status == STARTED and not waitOnFlip:
        theseKeys = TriggerDetect.getKeys(keyList=['5'], waitRelease=False)
        _TriggerDetect_allKeys.extend(theseKeys)
        if len(_TriggerDetect_allKeys):
            TriggerDetect.keys = _TriggerDetect_allKeys[-1].name  # just the last key pressed
            TriggerDetect.rt = _TriggerDetect_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *WaitText* updates
    if WaitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WaitText.frameNStart = frameN  # exact frame index
        WaitText.tStart = t  # local t and not account for scr refresh
        WaitText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WaitText, 'tStartRefresh')  # time at next scr refresh
        WaitText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitForTriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitForTrigger"-------
for thisComponent in WaitForTriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if TriggerDetect.keys in ['', [], None]:  # No response was made
    TriggerDetect.keys = None
thisExp.addData('TriggerDetect.keys',TriggerDetect.keys)
if TriggerDetect.keys != None:  # we had a response
    thisExp.addData('TriggerDetect.rt', TriggerDetect.rt)
thisExp.addData('TriggerDetect.started', TriggerDetect.tStartRefresh)
thisExp.addData('TriggerDetect.stopped', TriggerDetect.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('WaitText.started', WaitText.tStartRefresh)
thisExp.addData('WaitText.stopped', WaitText.tStopRefresh)
# the Routine "WaitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Fixation"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
FixationComponents = [Fixation_Cross, TriggerDetectedText]
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
    
    # *Fixation_Cross* updates
    if Fixation_Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_Cross.frameNStart = frameN  # exact frame index
        Fixation_Cross.tStart = t  # local t and not account for scr refresh
        Fixation_Cross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_Cross, 'tStartRefresh')  # time at next scr refresh
        Fixation_Cross.setAutoDraw(True)
    if Fixation_Cross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Fixation_Cross.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Fixation_Cross.tStop = t  # not accounting for scr refresh
            Fixation_Cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Fixation_Cross, 'tStopRefresh')  # time at next scr refresh
            Fixation_Cross.setAutoDraw(False)
    
    # *TriggerDetectedText* updates
    if TriggerDetectedText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TriggerDetectedText.frameNStart = frameN  # exact frame index
        TriggerDetectedText.tStart = t  # local t and not account for scr refresh
        TriggerDetectedText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerDetectedText, 'tStartRefresh')  # time at next scr refresh
        TriggerDetectedText.setAutoDraw(True)
    if TriggerDetectedText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > TriggerDetectedText.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            TriggerDetectedText.tStop = t  # not accounting for scr refresh
            TriggerDetectedText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(TriggerDetectedText, 'tStopRefresh')  # time at next scr refresh
            TriggerDetectedText.setAutoDraw(False)
    
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
thisExp.addData('Fixation_Cross.started', Fixation_Cross.tStartRefresh)
thisExp.addData('Fixation_Cross.stopped', Fixation_Cross.tStopRefresh)
thisExp.addData('TriggerDetectedText.started', TriggerDetectedText.tStartRefresh)
thisExp.addData('TriggerDetectedText.stopped', TriggerDetectedText.tStopRefresh)

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
