#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on February 24, 2022, at 17:16
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
expName = 'PacedBreathHolding'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Adolphslab\\Desktop\\cbic-psychopy\\PacedBreathHolding\\PacedBreathHolding_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=-1, 
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
    text='BREATHOLDING INSTRUCTIONS\n\nFollow the size of the green circle with your breathing\n\nHold your breath when the circle turns RED\n\nThe circle will fade slowly from RED back to GREEN\n\nYou will be told when you can breath normally again\n\nThis will repeat five times\n\nPRESS ANY BUTTON TO CONTINUE',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstructionsEndKey = keyboard.Keyboard()

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()
TriggerKey = keyboard.Keyboard()
TriggerWaitText = visual.TextStim(win=win, name='TriggerWaitText',
    text='Breath normally',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "GetReady"
GetReadyClock = core.Clock()
GetReadyText = visual.TextStim(win=win, name='GetReadyText',
    text='Get ready to breath with the circle',
    font='Open Sans',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PacedBreathing"
PacedBreathingClock = core.Clock()
BreathCircle = visual.ShapeStim(
    win=win, name='BreathCircle',units='cm', 
    size=(20, 20), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=0.0,     colorSpace='hsv',  lineColor='white', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "HoldBreath"
HoldBreathClock = core.Clock()
HoldCircle = visual.ShapeStim(
    win=win, name='HoldCircle',units='cm', 
    size=(10, 10), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=0.0,     colorSpace='hsv',  lineColor='white', fillColor='green',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "FreeBreath"
FreeBreathClock = core.Clock()
FreeBreathText = visual.TextStim(win=win, name='FreeBreathText',
    text='Breath normally again',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thanks305"
Thanks305Clock = core.Clock()
ThanksText = visual.TextStim(win=win, name='ThanksText',
    text='Breath hold task complete!',
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
InstructionsEndKey.keys = []
InstructionsEndKey.rt = []
_InstructionsEndKey_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsText, InstructionsEndKey]
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
    
    # *InstructionsEndKey* updates
    waitOnFlip = False
    if InstructionsEndKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsEndKey.frameNStart = frameN  # exact frame index
        InstructionsEndKey.tStart = t  # local t and not account for scr refresh
        InstructionsEndKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsEndKey, 'tStartRefresh')  # time at next scr refresh
        InstructionsEndKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstructionsEndKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(InstructionsEndKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if InstructionsEndKey.status == STARTED and not waitOnFlip:
        theseKeys = InstructionsEndKey.getKeys(keyList=None, waitRelease=False)
        _InstructionsEndKey_allKeys.extend(theseKeys)
        if len(_InstructionsEndKey_allKeys):
            InstructionsEndKey.keys = _InstructionsEndKey_allKeys[-1].name  # just the last key pressed
            InstructionsEndKey.rt = _InstructionsEndKey_allKeys[-1].rt
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
if InstructionsEndKey.keys in ['', [], None]:  # No response was made
    InstructionsEndKey.keys = None
thisExp.addData('InstructionsEndKey.keys',InstructionsEndKey.keys)
if InstructionsEndKey.keys != None:  # we had a response
    thisExp.addData('InstructionsEndKey.rt', InstructionsEndKey.rt)
thisExp.addData('InstructionsEndKey.started', InstructionsEndKey.tStartRefresh)
thisExp.addData('InstructionsEndKey.stopped', InstructionsEndKey.tStopRefresh)
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
    if TriggerWaitText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
BreathHoldTrials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='BreathHoldTrials')
thisExp.addLoop(BreathHoldTrials)  # add the loop to the experiment
thisBreathHoldTrial = BreathHoldTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBreathHoldTrial.rgb)
if thisBreathHoldTrial != None:
    for paramName in thisBreathHoldTrial:
        exec('{} = thisBreathHoldTrial[paramName]'.format(paramName))

for thisBreathHoldTrial in BreathHoldTrials:
    currentLoop = BreathHoldTrials
    # abbreviate parameter names if possible (e.g. rgb = thisBreathHoldTrial.rgb)
    if thisBreathHoldTrial != None:
        for paramName in thisBreathHoldTrial:
            exec('{} = thisBreathHoldTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "GetReady"-------
    continueRoutine = True
    routineTimer.add(5.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    GetReadyComponents = [GetReadyText]
    for thisComponent in GetReadyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GetReadyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GetReady"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = GetReadyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GetReadyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GetReadyText* updates
        if GetReadyText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            GetReadyText.frameNStart = frameN  # exact frame index
            GetReadyText.tStart = t  # local t and not account for scr refresh
            GetReadyText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GetReadyText, 'tStartRefresh')  # time at next scr refresh
            GetReadyText.setAutoDraw(True)
        if GetReadyText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GetReadyText.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                GetReadyText.tStop = t  # not accounting for scr refresh
                GetReadyText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(GetReadyText, 'tStopRefresh')  # time at next scr refresh
                GetReadyText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GetReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GetReady"-------
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BreathHoldTrials.addData('GetReadyText.started', GetReadyText.tStartRefresh)
    BreathHoldTrials.addData('GetReadyText.stopped', GetReadyText.tStopRefresh)
    
    # ------Prepare to start Routine "PacedBreathing"-------
    continueRoutine = True
    routineTimer.add(22.500000)
    # update component parameters for each repeat
    # Breathing circle scaling
    breath_amp = 0.25 # Sinusoid scaling amplitude
    breath_off = 0.75 # Sinusoid scaling offset
    breath_t = 6.0 # Resp cycle in seconds
    phi_0 = 0.0 # Initial phase offset
    orig_size = BreathCircle.size
    # keep track of which components have finished
    PacedBreathingComponents = [BreathCircle]
    for thisComponent in PacedBreathingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PacedBreathingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PacedBreathing"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PacedBreathingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PacedBreathingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BreathCircle* updates
        if BreathCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BreathCircle.frameNStart = frameN  # exact frame index
            BreathCircle.tStart = t  # local t and not account for scr refresh
            BreathCircle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BreathCircle, 'tStartRefresh')  # time at next scr refresh
            BreathCircle.setAutoDraw(True)
        if BreathCircle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BreathCircle.tStartRefresh + 22.5-frameTolerance:
                # keep track of stop time/frame for later
                BreathCircle.tStop = t  # not accounting for scr refresh
                BreathCircle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BreathCircle, 'tStopRefresh')  # time at next scr refresh
                BreathCircle.setAutoDraw(False)
        # Update circle radius
        sf = breath_off + (breath_amp * np.sin(2.0 * np.pi * (t / breath_t + phi_0)))
        BreathCircle.size = orig_size * sf
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PacedBreathingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PacedBreathing"-------
    for thisComponent in PacedBreathingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BreathHoldTrials.addData('BreathCircle.started', BreathCircle.tStartRefresh)
    BreathHoldTrials.addData('BreathCircle.stopped', BreathCircle.tStopRefresh)
    BreathCircle.size = orig_size
    
    # ------Prepare to start Routine "HoldBreath"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    HoldBreathComponents = [HoldCircle]
    for thisComponent in HoldBreathComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HoldBreathClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HoldBreath"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = HoldBreathClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HoldBreathClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HoldCircle* updates
        if HoldCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HoldCircle.frameNStart = frameN  # exact frame index
            HoldCircle.tStart = t  # local t and not account for scr refresh
            HoldCircle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HoldCircle, 'tStartRefresh')  # time at next scr refresh
            HoldCircle.setAutoDraw(True)
        if HoldCircle.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HoldCircle.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                HoldCircle.tStop = t  # not accounting for scr refresh
                HoldCircle.frameNStop = frameN  # exact frame index
                win.timeOnFlip(HoldCircle, 'tStopRefresh')  # time at next scr refresh
                HoldCircle.setAutoDraw(False)
        tt = t/60
        
        # Hue in range 0 (red) to 120 (green)
        # Stop color slide at 80 (green-yellow)
        h = int(tt * 90.0)
        
        s = 1 # Fully saturated
        v = 1 # Fully bright
        HoldCircle.color = (h, s, v)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HoldBreathComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HoldBreath"-------
    for thisComponent in HoldBreathComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BreathHoldTrials.addData('HoldCircle.started', HoldCircle.tStartRefresh)
    BreathHoldTrials.addData('HoldCircle.stopped', HoldCircle.tStopRefresh)
    
    # ------Prepare to start Routine "FreeBreath"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FreeBreathComponents = [FreeBreathText]
    for thisComponent in FreeBreathComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FreeBreathClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FreeBreath"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FreeBreathClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FreeBreathClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FreeBreathText* updates
        if FreeBreathText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            FreeBreathText.frameNStart = frameN  # exact frame index
            FreeBreathText.tStart = t  # local t and not account for scr refresh
            FreeBreathText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FreeBreathText, 'tStartRefresh')  # time at next scr refresh
            FreeBreathText.setAutoDraw(True)
        if FreeBreathText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FreeBreathText.tStartRefresh + 29.5-frameTolerance:
                # keep track of stop time/frame for later
                FreeBreathText.tStop = t  # not accounting for scr refresh
                FreeBreathText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FreeBreathText, 'tStopRefresh')  # time at next scr refresh
                FreeBreathText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FreeBreathComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FreeBreath"-------
    for thisComponent in FreeBreathComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BreathHoldTrials.addData('FreeBreathText.started', FreeBreathText.tStartRefresh)
    BreathHoldTrials.addData('FreeBreathText.stopped', FreeBreathText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'BreathHoldTrials'


# ------Prepare to start Routine "Thanks305"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
Thanks305Components = [ThanksText]
for thisComponent in Thanks305Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Thanks305Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thanks305"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Thanks305Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Thanks305Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThanksText* updates
    if ThanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    for thisComponent in Thanks305Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks305"-------
for thisComponent in Thanks305Components:
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
