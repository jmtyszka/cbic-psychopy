#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue Mar  8 11:12:14 2022
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
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'MovieWithEyetracking'  # from the Builder filename that created this script
expInfo = {'participant': 'Damy001', 'movie': 'Gump0.mp4'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expInfo['participant'], expInfo['movie'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jmt/GitHub/cbic-psychopy/MovieWithEyetracking/MovieWithEyetracking_lastrun.py',
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
    size=[2560, 1080], fullscr=True, screen=0, 
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
ioDevice = 'eyetracker.hw.mouse.EyeTracker'
ioConfig = {
    ioDevice: {
        'name': 'tracker',
        'controls': {
            'move': [],
            'blink':('MIDDLE_BUTTON',),
            'saccade_threshold': 0.5,
        }
    }
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instructions = visual.TextBox2(
     win, text="This experiment shows off the eyetracking capabilities of Builder.\n\nIn each trial, to move on, look at the dark circle for 5 seconds. The bar at the bottom will show how long you've been looking at it for, the cross will move with your eyes and will turn green when you're looking in the circle.\n\nPress SPACE to begin.", font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(0.8, 0.8), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instructions',
     autoLog=True,
)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
etRecord = hardware.eyetracker.EyetrackerControl(
    server=ioServer,
    tracker=eyetracker
)
roi = visual.ROI(win, name='roi', tracker=eyetracker,
    debug=False,
    shape='circle',
    pos=[0,0], size=(0.2, 0.2), ori=0.0)
progress = visual.ShapeStim(
    win=win, name='progress', vertices=[[0, 0.5],[0, -0.5],[1, -0.5],[1, 0.5]],
    size=[1.0, 1.0],
    ori=0.0, pos=(-0.5, -0.4),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
target = visual.ShapeStim(
    win=win, name='target',
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=10.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=0.2, depth=-3.0, interpolate=True)
gazeCursor = visual.ShapeStim(
    win=win, name='gazeCursor', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# -------Run Routine 'calibration'-------

# define target for calibration
calibrationTarget = visual.TargetStim(win, 
    name='calibrationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for calibration
calibration = hardware.eyetracker.EyetrackerCalibration(win, 
    eyetracker, calibrationTarget,
    units=None, colorSpace='rgb',
    progressMode='time', targetDur=1.5, expandScale=1.25,
    targetLayout='NINE_POINTS', randomisePos=True,
    movementAnimation=True, targetDelay=1.0
)
# run calibration
calibration.run()
# clear any keypresses from during calibration so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# -------Run Routine 'validation'-------

# define target for validation
validationTarget = visual.TargetStim(win, 
    name='validationTarget',
    radius=0.01, fillColor='', borderColor='black', lineWidth=2.0,
    innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
    colorSpace='rgb', units=None
)
# define parameters for validation
validation = iohub.ValidationProcedure(win,
    target=validationTarget,
    gaze_cursor='green', 
    positions='NINE_POINTS', randomize_positions=True,
    expand_scale=1.25, target_duration=1.5,
    enable_position_animation=True, target_delay=1.0,
    progress_on_key=None,
    show_results_screen=True, save_results_screen=False,
    color_space='rgb', unit_type=None
)
# run validation
validation.run()
# clear any keypresses from during validation so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "validation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
instructions.reset()
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instrComponents = [instructions, key_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    roi.setPos((random()/2, random()/2))
    # clear any previous roi data
    roi.reset()
    target.setPos([roi.pos])
    target.setSize([roi.size])
    # keep track of which components have finished
    trialComponents = [etRecord, roi, progress, target, gazeCursor]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRecord* updates
        if etRecord.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord.frameNStart = frameN  # exact frame index
            etRecord.tStart = t  # local t and not account for scr refresh
            etRecord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord, 'tStartRefresh')  # time at next scr refresh
            etRecord.status = STARTED
        if etRecord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                etRecord.tStop = t  # not accounting for scr refresh
                etRecord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(etRecord, 'tStopRefresh')  # time at next scr refresh
                etRecord.status = FINISHED
        
        # *roi* updates
        if roi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            roi.frameNStart = frameN  # exact frame index
            roi.tStart = t  # local t and not account for scr refresh
            roi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(roi, 'tStartRefresh')  # time at next scr refresh
            roi.setAutoDraw(True)
            roi.status = STARTED
        if roi.status == STARTED:
            # check whether roi has been looked in
            if roi.isLookedIn:
                if not roi.wasLookedIn:
                    roi.timesOn.append(roi.clock.getTime()) # store time of first look
                    roi.timesOff.append(roi.clock.getTime()) # store time looked until
                else:
                    roi.timesOff[-1] = roi.clock.getTime() # update time looked until
                    if roi.currentLookTime > 5.0: # check if they've been looking long enough
                        continueRoutine = False # end routine on sufficiently long look
                roi.wasLookedIn = True  # if roi is still looked at next frame, it is not a new look
            else:
                if roi.wasLookedIn:
                    roi.timesOff[-1] = roi.clock.getTime() # update time looked until
                roi.wasLookedIn = False  # if roi is looked at next frame, it is a new look
        else:
            roi.clock.reset() # keep clock at 0 if roi hasn't started / has finished
            roi.wasLookedIn = False  # if roi is looked at next frame, it is a new look
        
        # *progress* updates
        if progress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progress.frameNStart = frameN  # exact frame index
            progress.tStart = t  # local t and not account for scr refresh
            progress.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progress, 'tStartRefresh')  # time at next scr refresh
            progress.setAutoDraw(True)
        if progress.status == STARTED:  # only update if drawing
            progress.setSize((roi.currentLookTime/5, 0.1), log=False)
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        
        # *gazeCursor* updates
        if gazeCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            gazeCursor.frameNStart = frameN  # exact frame index
            gazeCursor.tStart = t  # local t and not account for scr refresh
            gazeCursor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(gazeCursor, 'tStartRefresh')  # time at next scr refresh
            gazeCursor.setAutoDraw(True)
        if gazeCursor.status == STARTED:  # only update if drawing
            gazeCursor.setFillColor(("lightgreen" if roi.isLookedIn else "white"), log=False)
            gazeCursor.setPos([etRecord.getPos()], log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # make sure the eyetracker recording stops
    if etRecord.status != FINISHED:
        etRecord.status = FINISHED
    trials.addData('roi.started', roi.tStartRefresh)
    trials.addData('roi.stopped', roi.tStopRefresh)
    trials.addData('roi.numLooks', roi.numLooks)
    if roi.numLooks:
       trials.addData('roi.timesOn', roi.timesOn)
       trials.addData('roi.timesOff', roi.timesOff)
    else:
       trials.addData('roi.timesOn', "")
       trials.addData('roi.timesOff', "")
    trials.addData('progress.started', progress.tStartRefresh)
    trials.addData('progress.stopped', progress.tStopRefresh)
    trials.addData('target.started', target.tStartRefresh)
    trials.addData('target.stopped', target.tStopRefresh)
    trials.addData('gazeCursor.started', gazeCursor.tStartRefresh)
    trials.addData('gazeCursor.stopped', gazeCursor.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'trials'


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
