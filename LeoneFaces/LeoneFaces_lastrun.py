#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Jan 26 12:23:09 2022
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
expName = 'LeoneFaces'  # from the Builder filename that created this script
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
    originPath='/Users/jmt/GitHub/cbic-pyschopy/LeoneFaces/LeoneFaces_lastrun.py',
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
    text='Stay awake and still.\nEnjoy the movie!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()
TriggerKey = keyboard.Keyboard()
WaitText = visual.TextStim(win=win, name='WaitText',
    text='Waiting for scanner ...',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "PreFixation"
PreFixationClock = core.Clock()
PreFixationCross = visual.ShapeStim(
    win=win, name='PreFixationCross',
    size=(0.1, 0.1), vertices='triangle',
    ori=0.0, pos=(0, 0),
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='lightgray',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "PlayMovie"
PlayMovieClock = core.Clock()
MovieObject = visual.MovieStim3(
    win=win, name='MovieObject',units='pix', 
    noAudio = False,
    filename='LeoneFaces.mp4',
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    size=(1920, 1080),
    depth=0.0,
    )

# Initialize components for Routine "PostFixation495"
PostFixation495Clock = core.Clock()
PostFixationCross = visual.ShapeStim(
    win=win, name='PostFixationCross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.0,     colorSpace='rgb',  lineColor='white', fillColor='lightgray',
    opacity=None, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
InstructionsComponents = [InstructionsText]
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if InstructionsText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > InstructionsText.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            InstructionsText.tStop = t  # not accounting for scr refresh
            InstructionsText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(InstructionsText, 'tStopRefresh')  # time at next scr refresh
            InstructionsText.setAutoDraw(False)
    
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

# ------Prepare to start Routine "WaitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
TriggerKey.keys = []
TriggerKey.rt = []
_TriggerKey_allKeys = []
# keep track of which components have finished
WaitForTriggerComponents = [TriggerKey, WaitText]
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
if TriggerKey.keys in ['', [], None]:  # No response was made
    TriggerKey.keys = None
thisExp.addData('TriggerKey.keys',TriggerKey.keys)
if TriggerKey.keys != None:  # we had a response
    thisExp.addData('TriggerKey.rt', TriggerKey.rt)
thisExp.addData('TriggerKey.started', TriggerKey.tStartRefresh)
thisExp.addData('TriggerKey.stopped', TriggerKey.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('WaitText.started', WaitText.tStartRefresh)
thisExp.addData('WaitText.stopped', WaitText.tStopRefresh)
# the Routine "WaitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PreFixation"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
PreFixationComponents = [PreFixationCross]
for thisComponent in PreFixationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PreFixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PreFixation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PreFixationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PreFixationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PreFixationCross* updates
    if PreFixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PreFixationCross.frameNStart = frameN  # exact frame index
        PreFixationCross.tStart = t  # local t and not account for scr refresh
        PreFixationCross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PreFixationCross, 'tStartRefresh')  # time at next scr refresh
        PreFixationCross.setAutoDraw(True)
    if PreFixationCross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PreFixationCross.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            PreFixationCross.tStop = t  # not accounting for scr refresh
            PreFixationCross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PreFixationCross, 'tStopRefresh')  # time at next scr refresh
            PreFixationCross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreFixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreFixation"-------
for thisComponent in PreFixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PreFixationCross.started', PreFixationCross.tStartRefresh)
thisExp.addData('PreFixationCross.stopped', PreFixationCross.tStopRefresh)

# ------Prepare to start Routine "PlayMovie"-------
continueRoutine = True
routineTimer.add(455.000000)
# update component parameters for each repeat
# keep track of which components have finished
PlayMovieComponents = [MovieObject]
for thisComponent in PlayMovieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PlayMovieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PlayMovie"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PlayMovieClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PlayMovieClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *MovieObject* updates
    if MovieObject.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MovieObject.frameNStart = frameN  # exact frame index
        MovieObject.tStart = t  # local t and not account for scr refresh
        MovieObject.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MovieObject, 'tStartRefresh')  # time at next scr refresh
        MovieObject.setAutoDraw(True)
    if MovieObject.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > MovieObject.tStartRefresh + 455-frameTolerance:
            # keep track of stop time/frame for later
            MovieObject.tStop = t  # not accounting for scr refresh
            MovieObject.frameNStop = frameN  # exact frame index
            win.timeOnFlip(MovieObject, 'tStopRefresh')  # time at next scr refresh
            MovieObject.setAutoDraw(False)
    if MovieObject.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PlayMovieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PlayMovie"-------
for thisComponent in PlayMovieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
MovieObject.stop()

# ------Prepare to start Routine "PostFixation495"-------
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
# keep track of which components have finished
PostFixation495Components = [PostFixationCross]
for thisComponent in PostFixation495Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PostFixation495Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PostFixation495"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PostFixation495Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PostFixation495Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PostFixationCross* updates
    if PostFixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PostFixationCross.frameNStart = frameN  # exact frame index
        PostFixationCross.tStart = t  # local t and not account for scr refresh
        PostFixationCross.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PostFixationCross, 'tStartRefresh')  # time at next scr refresh
        PostFixationCross.setAutoDraw(True)
    if PostFixationCross.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > PostFixationCross.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            PostFixationCross.tStop = t  # not accounting for scr refresh
            PostFixationCross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PostFixationCross, 'tStopRefresh')  # time at next scr refresh
            PostFixationCross.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PostFixation495Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PostFixation495"-------
for thisComponent in PostFixation495Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PostFixationCross.started', PostFixationCross.tStartRefresh)
thisExp.addData('PostFixationCross.stopped', PostFixationCross.tStopRefresh)

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
