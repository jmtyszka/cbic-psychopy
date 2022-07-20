#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on July 19, 2022, at 16:17
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
expName = 'PacedFingerTapping'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\jmt\\Documents\\GitHub\\cbic-psychopy\\PacedFingerTapping\\PacedFingerTapping.py',
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

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()

# Initialize components for Routine "Tapping"
TappingClock = core.Clock()
leftOut = visual.ShapeStim(
    win=win, name='leftOut',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(-0.2, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
leftIn = visual.ShapeStim(
    win=win, name='leftIn',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(-0.1, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
rightIn = visual.ShapeStim(
    win=win, name='rightIn',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0.1, 0.0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-2.0, interpolate=True)
rightOut = visual.ShapeStim(
    win=win, name='rightOut',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0.2, 0.0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)
# Trial timings
t_rest = 3
t_ready = 1
t_tapping = 5

# Start of tapping within trial
t_tapstart = t_rest + t_ready

# Total trail duration
t_trial = t_tapstart + t_tapping

# Tap interval
t_tapint = 0.2

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = []
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
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WaitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
WaitForTriggerComponents = []
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
# the Routine "WaitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('handLoop.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Tapping"-------
    continueRoutine = True
    # update component parameters for each repeat
    leftOut.setFillColor('black')
    # keep track of which components have finished
    TappingComponents = [leftOut, leftIn, rightIn, rightOut]
    for thisComponent in TappingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TappingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Tapping"-------
    while continueRoutine:
        # get current time
        t = TappingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TappingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *leftOut* updates
        if leftOut.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            leftOut.frameNStart = frameN  # exact frame index
            leftOut.tStart = t  # local t and not account for scr refresh
            leftOut.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftOut, 'tStartRefresh')  # time at next scr refresh
            leftOut.setAutoDraw(True)
        if leftOut.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leftOut.tStartRefresh + t_trial-frameTolerance:
                # keep track of stop time/frame for later
                leftOut.tStop = t  # not accounting for scr refresh
                leftOut.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftOut, 'tStopRefresh')  # time at next scr refresh
                leftOut.setAutoDraw(False)
        
        # *leftIn* updates
        if leftIn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            leftIn.frameNStart = frameN  # exact frame index
            leftIn.tStart = t  # local t and not account for scr refresh
            leftIn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(leftIn, 'tStartRefresh')  # time at next scr refresh
            leftIn.setAutoDraw(True)
        if leftIn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > leftIn.tStartRefresh + t_trial-frameTolerance:
                # keep track of stop time/frame for later
                leftIn.tStop = t  # not accounting for scr refresh
                leftIn.frameNStop = frameN  # exact frame index
                win.timeOnFlip(leftIn, 'tStopRefresh')  # time at next scr refresh
                leftIn.setAutoDraw(False)
        
        # *rightIn* updates
        if rightIn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightIn.frameNStart = frameN  # exact frame index
            rightIn.tStart = t  # local t and not account for scr refresh
            rightIn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightIn, 'tStartRefresh')  # time at next scr refresh
            rightIn.setAutoDraw(True)
        if rightIn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rightIn.tStartRefresh + t_trial-frameTolerance:
                # keep track of stop time/frame for later
                rightIn.tStop = t  # not accounting for scr refresh
                rightIn.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightIn, 'tStopRefresh')  # time at next scr refresh
                rightIn.setAutoDraw(False)
        
        # *rightOut* updates
        if rightOut.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightOut.frameNStart = frameN  # exact frame index
            rightOut.tStart = t  # local t and not account for scr refresh
            rightOut.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightOut, 'tStartRefresh')  # time at next scr refresh
            rightOut.setAutoDraw(True)
        if rightOut.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rightOut.tStartRefresh + t_trial-frameTolerance:
                # keep track of stop time/frame for later
                rightOut.tStop = t  # not accounting for scr refresh
                rightOut.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rightOut, 'tStopRefresh')  # time at next scr refresh
                rightOut.setAutoDraw(False)
        if t < t_rest:
            
            # All buttons black during rest
            leftOut.setFillColor('black')
            leftIn.setFillColor('black')
            rightIn.setFillColor('black')
            rightOut.setFillColor('black')
        
        elif t < t_rest + t_ready:
            
            # All buttons orange during ready
            leftOut.setFillColor('orange')
            leftIn.setFillColor('orange')
            rightIn.setFillColor('orange')
            rightOut.setFillColor('orange')
        
        else:
            
            # Alternative colors on correct hand
            in_on = bool(int((t - t_tapstart) / t_tapint) % 2)
            
            if in_on:
                if 'Right' in Hand:
                left_in = 'green'
                
                leftIn.setFillColor('green')
                rightIn.setFillColor('green')
                leftOut.setFillColor('black')
                rightOut.setFillColor('black')
            else:
                leftIn.setFillColor('black')
                rightIn.setFillColor('black')
                leftOut.setFillColor('green')
                rightOut.setFillColor('green')
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TappingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Tapping"-------
    for thisComponent in TappingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('leftOut.started', leftOut.tStartRefresh)
    trials.addData('leftOut.stopped', leftOut.tStopRefresh)
    trials.addData('leftIn.started', leftIn.tStartRefresh)
    trials.addData('leftIn.stopped', leftIn.tStopRefresh)
    trials.addData('rightIn.started', rightIn.tStartRefresh)
    trials.addData('rightIn.stopped', rightIn.tStopRefresh)
    trials.addData('rightOut.started', rightOut.tStartRefresh)
    trials.addData('rightOut.stopped', rightOut.tStopRefresh)
    # the Routine "Tapping" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 6.0 repeats of 'trials'


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
