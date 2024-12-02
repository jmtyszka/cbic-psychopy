﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on November 28, 2023, at 14:35
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.2.3')


from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '0'
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
    originPath='C:\\Users\\Adolphslab\\Desktop\\cbic-psychopy\\PacedFingerTapping\\PacedFingerTapping_lastrun.py',
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
    size=[1280, 960], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='hPrisma Projector', color=[0,0,0], colorSpace='rgb',
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
    text='This is a finger tapping task using two fingers on either hand.\n\nYou will see two white circles on the left and two on the right.\n\nWhen any of the circles turn ORANGE\nget ready to tap the buttons on that hand.\n\nWhen the circles flash GREEN\ntap the buttons on that side in time with the flashing.\n\nPlease keep your gaze on the central white cross.\n\nPRESS ANY BUTTON TO CONTINUE',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey = keyboard.Keyboard()

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()
TriggerKey = keyboard.Keyboard()
TriggerWaitText = visual.TextStim(win=win, name='TriggerWaitText',
    text='Waiting for scanner ...',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

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
t_rest = 15
t_ready = 2
t_tapping = 15

# Start of tapping within trial
t_tapstart = t_rest + t_ready

# Total trail duration
t_trial = t_tapstart + t_tapping

# Tap interval
t_tapint = 0.2
FixationCross = visual.TextStim(win=win, name='FixationCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
ButtonTaps = keyboard.Keyboard()

# Initialize components for Routine "FinalFixation"
FinalFixationClock = core.Clock()
FinalFixationCross = visual.TextStim(win=win, name='FinalFixationCross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.02, wrapWidth=None, ori=0.0, 
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

# ------Prepare to start Routine "WaitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
TriggerKey.keys = []
TriggerKey.rt = []
_TriggerKey_allKeys = []
# keep track of which components have finished
WaitForTriggerComponents = [TriggerKey, TriggerWaitText]
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
    
    # *TriggerKey* updates
    waitOnFlip = False
    if TriggerKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TriggerKey.frameNStart = frameN  # exact frame index
        TriggerKey.tStart = t  # local t and not account for scr refresh
        TriggerKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerKey, 'tStartRefresh')  # time at next scr refresh
        TriggerKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(TriggerKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(TriggerKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if TriggerKey.status == STARTED and not waitOnFlip:
        theseKeys = TriggerKey.getKeys(keyList=['5'], waitRelease=False)
        _TriggerKey_allKeys.extend(theseKeys)
        if len(_TriggerKey_allKeys):
            TriggerKey.keys = _TriggerKey_allKeys[-1].name  # just the last key pressed
            TriggerKey.rt = _TriggerKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *TriggerWaitText* updates
    if TriggerWaitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TriggerWaitText.frameNStart = frameN  # exact frame index
        TriggerWaitText.tStart = t  # local t and not account for scr refresh
        TriggerWaitText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerWaitText, 'tStartRefresh')  # time at next scr refresh
        TriggerWaitText.setAutoDraw(True)
    
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
if TriggerKey.keys in ['', [], None]:  # No response was made
    TriggerKey.keys = None
thisExp.addData('TriggerKey.keys',TriggerKey.keys)
if TriggerKey.keys != None:  # we had a response
    thisExp.addData('TriggerKey.rt', TriggerKey.rt)
thisExp.addData('TriggerKey.started', TriggerKey.tStartRefresh)
thisExp.addData('TriggerKey.stopped', TriggerKey.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('TriggerWaitText.started', TriggerWaitText.tStartRefresh)
thisExp.addData('TriggerWaitText.stopped', TriggerWaitText.tStopRefresh)
# the Routine "WaitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3.0, method='random', 
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
    ButtonTaps.keys = []
    ButtonTaps.rt = []
    _ButtonTaps_allKeys = []
    # keep track of which components have finished
    TappingComponents = [leftOut, leftIn, rightIn, rightOut, FixationCross, ButtonTaps]
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
            
            # Set buttons for next hand(s) to orange
            if 'Left' in Hand or 'Both' in Hand:
                leftOut.setFillColor('orange')
                leftIn.setFillColor('orange')
            
            if 'Right' in Hand or 'Both' in Hand:
                rightIn.setFillColor('orange')
                rightOut.setFillColor('orange')
        
        else:
            
            # Alternate colors
            in_color = bool(int((t - t_tapstart) / t_tapint) % 2)
        
            colors = ['black', 'black', 'black', 'black']
        
            if 'Right' in Hand or 'Both' in Hand:
                colors[2] = 'green' if in_color else 'black'
                colors[3] = 'black' if in_color else 'green'
                
            if 'Left' in Hand or 'Both' in Hand:
                colors[1] = 'green' if in_color else 'black'
                colors[0] = 'black' if in_color else 'green'
            
            # Set button colors
            leftOut.setFillColor(colors[0])
            leftIn.setFillColor(colors[1])
            rightIn.setFillColor(colors[2])
            rightOut.setFillColor(colors[3])
        
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
            if tThisFlipGlobal > FixationCross.tStartRefresh + t_trial-frameTolerance:
                # keep track of stop time/frame for later
                FixationCross.tStop = t  # not accounting for scr refresh
                FixationCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCross, 'tStopRefresh')  # time at next scr refresh
                FixationCross.setAutoDraw(False)
        
        # *ButtonTaps* updates
        waitOnFlip = False
        if ButtonTaps.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            ButtonTaps.frameNStart = frameN  # exact frame index
            ButtonTaps.tStart = t  # local t and not account for scr refresh
            ButtonTaps.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ButtonTaps, 'tStartRefresh')  # time at next scr refresh
            ButtonTaps.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(ButtonTaps.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(ButtonTaps.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if ButtonTaps.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ButtonTaps.tStartRefresh + t_trial-frameTolerance:
                # keep track of stop time/frame for later
                ButtonTaps.tStop = t  # not accounting for scr refresh
                ButtonTaps.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ButtonTaps, 'tStopRefresh')  # time at next scr refresh
                ButtonTaps.status = FINISHED
        if ButtonTaps.status == STARTED and not waitOnFlip:
            theseKeys = ButtonTaps.getKeys(keyList=['1', '2', '3', '4', '6', '7', '8', '9'], waitRelease=False)
            _ButtonTaps_allKeys.extend(theseKeys)
            if len(_ButtonTaps_allKeys):
                ButtonTaps.keys = _ButtonTaps_allKeys[-1].name  # just the last key pressed
                ButtonTaps.rt = _ButtonTaps_allKeys[-1].rt
        
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
    trials.addData('FixationCross.started', FixationCross.tStartRefresh)
    trials.addData('FixationCross.stopped', FixationCross.tStopRefresh)
    # check responses
    if ButtonTaps.keys in ['', [], None]:  # No response was made
        ButtonTaps.keys = None
    trials.addData('ButtonTaps.keys',ButtonTaps.keys)
    if ButtonTaps.keys != None:  # we had a response
        trials.addData('ButtonTaps.rt', ButtonTaps.rt)
    trials.addData('ButtonTaps.started', ButtonTaps.tStartRefresh)
    trials.addData('ButtonTaps.stopped', ButtonTaps.tStopRefresh)
    # the Routine "Tapping" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials'


# ------Prepare to start Routine "FinalFixation"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinalFixationComponents = [FinalFixationCross]
for thisComponent in FinalFixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinalFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FinalFixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinalFixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinalFixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FinalFixationCross* updates
    if FinalFixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FinalFixationCross.frameNStart = frameN  # exact frame index
        FinalFixationCross.tStart = t  # local t and not account for scr refresh
        FinalFixationCross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FinalFixationCross, 'tStartRefresh')  # time at next scr refresh
        FinalFixationCross.setAutoDraw(True)
    if FinalFixationCross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > FinalFixationCross.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            FinalFixationCross.tStop = t  # not accounting for scr refresh
            FinalFixationCross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FinalFixationCross, 'tStopRefresh')  # time at next scr refresh
            FinalFixationCross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalFixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FinalFixation"-------
for thisComponent in FinalFixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FinalFixationCross.started', FinalFixationCross.tStartRefresh)
thisExp.addData('FinalFixationCross.stopped', FinalFixationCross.tStopRefresh)

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
