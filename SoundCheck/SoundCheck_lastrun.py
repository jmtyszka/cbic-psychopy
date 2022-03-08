#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 08, 2022, at 13:37
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

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

# Preload sound clip



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SoundCheck'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Adolphslab\\Desktop\\cbic-psychopy\\SoundCheck\\SoundCheck_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=1, 
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
instructions_text = visual.TextStim(win=win, name='instructions_text',
    text='--- Sound Level Check ---\n\nAdjust the volume of the soundtrack until\nyou can hear it clearly above the scanner noise.\n\n1 : Quieter   2 : Louder   4 : Exit\n\nPress 1 to continue',
    font='Open Sans',
    units='cm', pos=(0, 0), height=1.5, wrapWidth=36.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instructions_continue = keyboard.Keyboard()

# Initialize components for Routine "WaitForTrigger"
WaitForTriggerClock = core.Clock()
trigger_key = keyboard.Keyboard()

# Initialize components for Routine "PlayAndAdjust"
PlayAndAdjustClock = core.Clock()
sound_clip = sound.Sound('budapest_soundcheck.wav', secs=-1, stereo=True, hamming=False,
    name='sound_clip')
sound_clip.setVolume(1.0)
volume = visual.Slider(win=win, name='volume',
    startValue=50, size=(1.0, 0.1), pos=(0, -0.1), units=None,
    labels=("0%", "50%", "100%"), ticks=(0, 50, 100), granularity=0.1,
    style='rating', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
adjust = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
instructions_continue.keys = []
instructions_continue.rt = []
_instructions_continue_allKeys = []
# keep track of which components have finished
InstructionsComponents = [instructions_text, instructions_continue]
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
    
    # *instructions_text* updates
    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.tStart = t  # local t and not account for scr refresh
        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
        instructions_text.setAutoDraw(True)
    
    # *instructions_continue* updates
    waitOnFlip = False
    if instructions_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_continue.frameNStart = frameN  # exact frame index
        instructions_continue.tStart = t  # local t and not account for scr refresh
        instructions_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_continue, 'tStartRefresh')  # time at next scr refresh
        instructions_continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructions_continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructions_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructions_continue.status == STARTED and not waitOnFlip:
        theseKeys = instructions_continue.getKeys(keyList=['1'], waitRelease=False)
        _instructions_continue_allKeys.extend(theseKeys)
        if len(_instructions_continue_allKeys):
            instructions_continue.keys = _instructions_continue_allKeys[-1].name  # just the last key pressed
            instructions_continue.rt = _instructions_continue_allKeys[-1].rt
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
thisExp.addData('instructions_text.started', instructions_text.tStartRefresh)
thisExp.addData('instructions_text.stopped', instructions_text.tStopRefresh)
# check responses
if instructions_continue.keys in ['', [], None]:  # No response was made
    instructions_continue.keys = None
thisExp.addData('instructions_continue.keys',instructions_continue.keys)
if instructions_continue.keys != None:  # we had a response
    thisExp.addData('instructions_continue.rt', instructions_continue.rt)
thisExp.addData('instructions_continue.started', instructions_continue.tStartRefresh)
thisExp.addData('instructions_continue.stopped', instructions_continue.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "WaitForTrigger"-------
continueRoutine = True
# update component parameters for each repeat
trigger_key.keys = []
trigger_key.rt = []
_trigger_key_allKeys = []
# keep track of which components have finished
WaitForTriggerComponents = [trigger_key]
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
    
    # *trigger_key* updates
    waitOnFlip = False
    if trigger_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_key.frameNStart = frameN  # exact frame index
        trigger_key.tStart = t  # local t and not account for scr refresh
        trigger_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_key, 'tStartRefresh')  # time at next scr refresh
        trigger_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_key.status == STARTED and not waitOnFlip:
        theseKeys = trigger_key.getKeys(keyList=['5'], waitRelease=False)
        _trigger_key_allKeys.extend(theseKeys)
        if len(_trigger_key_allKeys):
            trigger_key.keys = _trigger_key_allKeys[-1].name  # just the last key pressed
            trigger_key.rt = _trigger_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
if trigger_key.keys in ['', [], None]:  # No response was made
    trigger_key.keys = None
thisExp.addData('trigger_key.keys',trigger_key.keys)
if trigger_key.keys != None:  # we had a response
    thisExp.addData('trigger_key.rt', trigger_key.rt)
thisExp.addData('trigger_key.started', trigger_key.tStartRefresh)
thisExp.addData('trigger_key.stopped', trigger_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "WaitForTrigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PlayAndAdjust"-------
continueRoutine = True
# update component parameters for each repeat
sound_clip.setSound('budapest_soundcheck.wav', hamming=False)
sound_clip.setVolume(volume.getRating()/100.0, log=False)
volume.reset()
adjust.keys = []
adjust.rt = []
_adjust_allKeys = []
last_rt = -1.0
# keep track of which components have finished
PlayAndAdjustComponents = [sound_clip, volume, adjust]
for thisComponent in PlayAndAdjustComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PlayAndAdjustClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PlayAndAdjust"-------
while continueRoutine:
    # get current time
    t = PlayAndAdjustClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PlayAndAdjustClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop sound_clip
    sound_clip.setVolume(volume.getRating()/100.0, log=False)
    if sound_clip.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_clip.frameNStart = frameN  # exact frame index
        sound_clip.tStart = t  # local t and not account for scr refresh
        sound_clip.tStartRefresh = tThisFlipGlobal  # on global time
        sound_clip.play()  # start the sound (it finishes automatically)
    
    # *volume* updates
    if volume.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        volume.frameNStart = frameN  # exact frame index
        volume.tStart = t  # local t and not account for scr refresh
        volume.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(volume, 'tStartRefresh')  # time at next scr refresh
        volume.setAutoDraw(True)
    
    # *adjust* updates
    waitOnFlip = False
    if adjust.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        adjust.frameNStart = frameN  # exact frame index
        adjust.tStart = t  # local t and not account for scr refresh
        adjust.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(adjust, 'tStartRefresh')  # time at next scr refresh
        adjust.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(adjust.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(adjust.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if adjust.status == STARTED and not waitOnFlip:
        theseKeys = adjust.getKeys(keyList=['1', '2', '4'], waitRelease=False)
        _adjust_allKeys.extend(theseKeys)
        if len(_adjust_allKeys):
            adjust.keys = _adjust_allKeys[-1].name  # just the last key pressed
            adjust.rt = _adjust_allKeys[-1].rt
    if adjust.rt:
    
        this_rt = adjust.rt
    
        if this_rt - last_rt > 0.1:
    
            if adjust.keys == '1':
                volume.rating = volume.rating - 10
                if volume.rating < 0:
                    volume.rating = 0
                volume.draw()
                
            if adjust.keys == '2':
                volume.rating = volume.rating + 10
                if volume.rating > 100:
                    volume.rating = 100
                volume.draw()
                
            if adjust.keys == '4':
                continueRoutine = False
    
        last_rt = this_rt
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PlayAndAdjustComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PlayAndAdjust"-------
for thisComponent in PlayAndAdjustComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
sound_clip.stop()  # ensure sound has stopped at end of routine
thisExp.addData('sound_clip.started', sound_clip.tStart)
thisExp.addData('sound_clip.stopped', sound_clip.tStop)
thisExp.addData('volume.response', volume.getRating())
# the Routine "PlayAndAdjust" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
