#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on September 27, 2022, at 22:02
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
expName = 'RFF_final'  # from the Builder filename that created this script
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
    originPath='D:\\Adolphslab\\psychopy\\cbic-psychopy\\RepetitiveFaceFamiliarization\\RFF_final_lastrun.py',
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

# Initialize components for Routine "Introduction_Screen_Memory"
Introduction_Screen_MemoryClock = core.Clock()
introduction_memory = visual.TextStim(win=win, name='introduction_memory',
    text='This is the start of  session '+str(expInfo['session'])+' out of a total of 4 face memory task. In this session, 96 pictures of different faces will be presented to you. Some of the pictures have occurred in previous scanning sessions, and some are completely new. \n Please use the numbers on the keyboard to indicate whether a face is OLD (key mappings will be shown on the next screen), and how confident you are of the choice. Please respond as fast as possible, as for each new/old judgement, the maximal response time allowed is 2 seconds.\n Please press key \'1\' to continue when you are ready and understand the instructions',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_memory = keyboard.Keyboard()

# Initialize components for Routine "button_scheme"
button_schemeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Shown above is the button press scheme to be used for this task. For each image, you will be asked whether it is an OLD image that has appeared during previous sessions.\nOnce you are familiarized with the scheme, pleas press key '6' (left index finger) to start the test.",
    font='Open Sans',
    pos=(0, -0.35), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_confirmation = keyboard.Keyboard()
scheme_image = visual.ImageStim(
    win=win,
    name='scheme_image', 
    image='icons\\newold buttons even.bmp' if int(expInfo['session']) %2==0 else 'icons\\newold buttons odd.bmp', mask=None,
    ori=0.0, pos=(0, 0.1), size=(1.5, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Wait_for_Trigger"
Wait_for_TriggerClock = core.Clock()
TriggerText = visual.TextStim(win=win, name='TriggerText',
    text='Waiting for trigger...',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
TriggerCatcher = keyboard.Keyboard()

# Initialize components for Routine "ITI_2"
ITI_2Clock = core.Clock()
ITI_2_text = visual.TextStim(win=win, name='ITI_2_text',
    text='+  ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Face_Presentation"
Face_PresentationClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
ITI_1_text = visual.TextStim(win=win, name='ITI_1_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "New_Old_Question"
New_Old_QuestionClock = core.Clock()
new_old_question = visual.TextStim(win=win, name='new_old_question',
    text='Have you seen this person before (during past sessions)?',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
new_old_prompt = visual.ImageStim(
    win=win,
    name='new_old_prompt', 
    image='icons\\newold buttons even.bmp' if int(expInfo['session']) %2==0 else 'icons\\newold buttons odd.bmp', mask=None,
    ori=0.0, pos=(0, -0.1), size=(1.5, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
key_resp_2 = keyboard.Keyboard()
time_holder = visual.TextStim(win=win, name='time_holder',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "End_Screen_Memory"
End_Screen_MemoryClock = core.Clock()
end_memory = visual.TextStim(win=win, name='end_memory',
    text='Thank you for completing session ' +str(expInfo['session'])+ ' out of the total of 4 face memory sessions!! \n If you need a break, please press \'1\'. Otherwise, please wait for 10 seconds, and the task will exit on its own. We will move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_needed = keyboard.Keyboard()

# Initialize components for Routine "break_time"
break_timeClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text="We will be pausing for a short break before moving on to the next session :)\n\nPress '1' to exit the program\n",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_task = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Introduction_Screen_Memory"-------
continueRoutine = True
# update component parameters for each repeat
start_memory.keys = []
start_memory.rt = []
_start_memory_allKeys = []
# keep track of which components have finished
Introduction_Screen_MemoryComponents = [introduction_memory, start_memory]
for thisComponent in Introduction_Screen_MemoryComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Introduction_Screen_MemoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Introduction_Screen_Memory"-------
while continueRoutine:
    # get current time
    t = Introduction_Screen_MemoryClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Introduction_Screen_MemoryClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *introduction_memory* updates
    if introduction_memory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction_memory.frameNStart = frameN  # exact frame index
        introduction_memory.tStart = t  # local t and not account for scr refresh
        introduction_memory.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction_memory, 'tStartRefresh')  # time at next scr refresh
        introduction_memory.setAutoDraw(True)
    
    # *start_memory* updates
    waitOnFlip = False
    if start_memory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_memory.frameNStart = frameN  # exact frame index
        start_memory.tStart = t  # local t and not account for scr refresh
        start_memory.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_memory, 'tStartRefresh')  # time at next scr refresh
        start_memory.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_memory.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_memory.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_memory.status == STARTED and not waitOnFlip:
        theseKeys = start_memory.getKeys(keyList=['1'], waitRelease=False)
        _start_memory_allKeys.extend(theseKeys)
        if len(_start_memory_allKeys):
            start_memory.keys = _start_memory_allKeys[0].name  # just the first key pressed
            start_memory.rt = _start_memory_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_Screen_MemoryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Introduction_Screen_Memory"-------
for thisComponent in Introduction_Screen_MemoryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('introduction_memory.started', introduction_memory.tStartRefresh)
thisExp.addData('introduction_memory.stopped', introduction_memory.tStopRefresh)
# check responses
if start_memory.keys in ['', [], None]:  # No response was made
    start_memory.keys = None
thisExp.addData('start_memory.keys',start_memory.keys)
if start_memory.keys != None:  # we had a response
    thisExp.addData('start_memory.rt', start_memory.rt)
thisExp.addData('start_memory.started', start_memory.tStartRefresh)
thisExp.addData('start_memory.stopped', start_memory.tStopRefresh)
thisExp.nextEntry()
# the Routine "Introduction_Screen_Memory" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "button_scheme"-------
continueRoutine = True
# update component parameters for each repeat
button_confirmation.keys = []
button_confirmation.rt = []
_button_confirmation_allKeys = []
# keep track of which components have finished
button_schemeComponents = [text, button_confirmation, scheme_image]
for thisComponent in button_schemeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
button_schemeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "button_scheme"-------
while continueRoutine:
    # get current time
    t = button_schemeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=button_schemeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *button_confirmation* updates
    waitOnFlip = False
    if button_confirmation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_confirmation.frameNStart = frameN  # exact frame index
        button_confirmation.tStart = t  # local t and not account for scr refresh
        button_confirmation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_confirmation, 'tStartRefresh')  # time at next scr refresh
        button_confirmation.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(button_confirmation.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(button_confirmation.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if button_confirmation.status == STARTED and not waitOnFlip:
        theseKeys = button_confirmation.getKeys(keyList=['6'], waitRelease=False)
        _button_confirmation_allKeys.extend(theseKeys)
        if len(_button_confirmation_allKeys):
            button_confirmation.keys = _button_confirmation_allKeys[-1].name  # just the last key pressed
            button_confirmation.rt = _button_confirmation_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *scheme_image* updates
    if scheme_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scheme_image.frameNStart = frameN  # exact frame index
        scheme_image.tStart = t  # local t and not account for scr refresh
        scheme_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scheme_image, 'tStartRefresh')  # time at next scr refresh
        scheme_image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in button_schemeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "button_scheme"-------
for thisComponent in button_schemeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if button_confirmation.keys in ['', [], None]:  # No response was made
    button_confirmation.keys = None
thisExp.addData('button_confirmation.keys',button_confirmation.keys)
if button_confirmation.keys != None:  # we had a response
    thisExp.addData('button_confirmation.rt', button_confirmation.rt)
thisExp.addData('button_confirmation.started', button_confirmation.tStartRefresh)
thisExp.addData('button_confirmation.stopped', button_confirmation.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('scheme_image.started', scheme_image.tStartRefresh)
thisExp.addData('scheme_image.stopped', scheme_image.tStopRefresh)
# the Routine "button_scheme" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Wait_for_Trigger"-------
continueRoutine = True
# update component parameters for each repeat
TriggerCatcher.keys = []
TriggerCatcher.rt = []
_TriggerCatcher_allKeys = []
# keep track of which components have finished
Wait_for_TriggerComponents = [TriggerText, TriggerCatcher]
for thisComponent in Wait_for_TriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Wait_for_TriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait_for_Trigger"-------
while continueRoutine:
    # get current time
    t = Wait_for_TriggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Wait_for_TriggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TriggerText* updates
    if TriggerText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        TriggerText.frameNStart = frameN  # exact frame index
        TriggerText.tStart = t  # local t and not account for scr refresh
        TriggerText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerText, 'tStartRefresh')  # time at next scr refresh
        TriggerText.setAutoDraw(True)
    
    # *TriggerCatcher* updates
    waitOnFlip = False
    if TriggerCatcher.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TriggerCatcher.frameNStart = frameN  # exact frame index
        TriggerCatcher.tStart = t  # local t and not account for scr refresh
        TriggerCatcher.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerCatcher, 'tStartRefresh')  # time at next scr refresh
        TriggerCatcher.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(TriggerCatcher.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(TriggerCatcher.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if TriggerCatcher.status == STARTED and not waitOnFlip:
        theseKeys = TriggerCatcher.getKeys(keyList=['5'], waitRelease=False)
        _TriggerCatcher_allKeys.extend(theseKeys)
        if len(_TriggerCatcher_allKeys):
            TriggerCatcher.keys = [key.name for key in _TriggerCatcher_allKeys]  # storing all keys
            TriggerCatcher.rt = [key.rt for key in _TriggerCatcher_allKeys]
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_for_TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait_for_Trigger"-------
for thisComponent in Wait_for_TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TriggerText.started', TriggerText.tStartRefresh)
thisExp.addData('TriggerText.stopped', TriggerText.tStopRefresh)
# check responses
if TriggerCatcher.keys in ['', [], None]:  # No response was made
    TriggerCatcher.keys = None
thisExp.addData('TriggerCatcher.keys',TriggerCatcher.keys)
if TriggerCatcher.keys != None:  # we had a response
    thisExp.addData('TriggerCatcher.rt', TriggerCatcher.rt)
thisExp.addData('TriggerCatcher.started', TriggerCatcher.tStartRefresh)
thisExp.addData('TriggerCatcher.stopped', TriggerCatcher.tStopRefresh)
thisExp.nextEntry()
# the Routine "Wait_for_Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
repeat = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimfiles/stimfiles_final_'+str(expInfo['session'])+'.csv'),
    seed=None, name='repeat')
thisExp.addLoop(repeat)  # add the loop to the experiment
thisRepeat = repeat.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
if thisRepeat != None:
    for paramName in thisRepeat:
        exec('{} = thisRepeat[paramName]'.format(paramName))

for thisRepeat in repeat:
    currentLoop = repeat
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ITI_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_2Components = [ITI_2_text]
    for thisComponent in ITI_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI_2"-------
    while continueRoutine:
        # get current time
        t = ITI_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_2_text* updates
        if ITI_2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_2_text.frameNStart = frameN  # exact frame index
            ITI_2_text.tStart = t  # local t and not account for scr refresh
            ITI_2_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_2_text, 'tStartRefresh')  # time at next scr refresh
            ITI_2_text.setAutoDraw(True)
        if ITI_2_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_2_text.tStartRefresh + ITI_2-frameTolerance:
                # keep track of stop time/frame for later
                ITI_2_text.tStop = t  # not accounting for scr refresh
                ITI_2_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI_2_text, 'tStopRefresh')  # time at next scr refresh
                ITI_2_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_2"-------
    for thisComponent in ITI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeat.addData('ITI_2_text.started', ITI_2_text.tStartRefresh)
    repeat.addData('ITI_2_text.stopped', ITI_2_text.tStopRefresh)
    # the Routine "ITI_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Face_Presentation"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(stimFile)
    # keep track of which components have finished
    Face_PresentationComponents = [image]
    for thisComponent in Face_PresentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Face_PresentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Face_Presentation"-------
    while continueRoutine:
        # get current time
        t = Face_PresentationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Face_PresentationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            if frameN >= (image.frameNStart + 90):
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Face_PresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Face_Presentation"-------
    for thisComponent in Face_PresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeat.addData('image.started', image.tStartRefresh)
    repeat.addData('image.stopped', image.tStopRefresh)
    # the Routine "Face_Presentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [ITI_1_text]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ITI_1_text* updates
        if ITI_1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ITI_1_text.frameNStart = frameN  # exact frame index
            ITI_1_text.tStart = t  # local t and not account for scr refresh
            ITI_1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ITI_1_text, 'tStartRefresh')  # time at next scr refresh
            ITI_1_text.setAutoDraw(True)
        if ITI_1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_1_text.tStartRefresh + ITI_1-frameTolerance:
                # keep track of stop time/frame for later
                ITI_1_text.tStop = t  # not accounting for scr refresh
                ITI_1_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ITI_1_text, 'tStopRefresh')  # time at next scr refresh
                ITI_1_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeat.addData('ITI_1_text.started', ITI_1_text.tStartRefresh)
    repeat.addData('ITI_1_text.stopped', ITI_1_text.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "New_Old_Question"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    New_Old_QuestionComponents = [new_old_question, new_old_prompt, key_resp_2, time_holder]
    for thisComponent in New_Old_QuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    New_Old_QuestionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "New_Old_Question"-------
    while continueRoutine:
        # get current time
        t = New_Old_QuestionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=New_Old_QuestionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *new_old_question* updates
        if new_old_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_old_question.frameNStart = frameN  # exact frame index
            new_old_question.tStart = t  # local t and not account for scr refresh
            new_old_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_old_question, 'tStartRefresh')  # time at next scr refresh
            new_old_question.setAutoDraw(True)
        if new_old_question.status == STARTED:
            if bool(len(key_resp_2.keys) != 0 or tThisFlipGlobal > new_old_question.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                new_old_question.tStop = t  # not accounting for scr refresh
                new_old_question.frameNStop = frameN  # exact frame index
                win.timeOnFlip(new_old_question, 'tStopRefresh')  # time at next scr refresh
                new_old_question.setAutoDraw(False)
        
        # *new_old_prompt* updates
        if new_old_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_old_prompt.frameNStart = frameN  # exact frame index
            new_old_prompt.tStart = t  # local t and not account for scr refresh
            new_old_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_old_prompt, 'tStartRefresh')  # time at next scr refresh
            new_old_prompt.setAutoDraw(True)
        if new_old_prompt.status == STARTED:
            if bool(len(key_resp_2.keys) != 0  or tThisFlipGlobal > new_old_prompt.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                new_old_prompt.tStop = t  # not accounting for scr refresh
                new_old_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(new_old_prompt, 'tStopRefresh')  # time at next scr refresh
                new_old_prompt.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            if bool(len(key_resp_2.keys) != 0 or tThisFlipGlobal > key_resp_2.tStartRefresh + 2-frameTolerance):
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3', '4', '6', '7', '8', '9'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
        
        # *time_holder* updates
        if time_holder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            time_holder.frameNStart = frameN  # exact frame index
            time_holder.tStart = t  # local t and not account for scr refresh
            time_holder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(time_holder, 'tStartRefresh')  # time at next scr refresh
            time_holder.setAutoDraw(True)
        if time_holder.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > time_holder.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                time_holder.tStop = t  # not accounting for scr refresh
                time_holder.frameNStop = frameN  # exact frame index
                win.timeOnFlip(time_holder, 'tStopRefresh')  # time at next scr refresh
                time_holder.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in New_Old_QuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "New_Old_Question"-------
    for thisComponent in New_Old_QuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    repeat.addData('new_old_question.started', new_old_question.tStartRefresh)
    repeat.addData('new_old_question.stopped', new_old_question.tStopRefresh)
    repeat.addData('new_old_prompt.started', new_old_prompt.tStartRefresh)
    repeat.addData('new_old_prompt.stopped', new_old_prompt.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    repeat.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        repeat.addData('key_resp_2.rt', key_resp_2.rt)
    repeat.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    repeat.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    repeat.addData('time_holder.started', time_holder.tStartRefresh)
    repeat.addData('time_holder.stopped', time_holder.tStopRefresh)
    # the Routine "New_Old_Question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'repeat'


# set up handler to look after randomisation of conditions etc
break_catcher = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='break_catcher')
thisExp.addLoop(break_catcher)  # add the loop to the experiment
thisBreak_catcher = break_catcher.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBreak_catcher.rgb)
if thisBreak_catcher != None:
    for paramName in thisBreak_catcher:
        exec('{} = thisBreak_catcher[paramName]'.format(paramName))

for thisBreak_catcher in break_catcher:
    currentLoop = break_catcher
    # abbreviate parameter names if possible (e.g. rgb = thisBreak_catcher.rgb)
    if thisBreak_catcher != None:
        for paramName in thisBreak_catcher:
            exec('{} = thisBreak_catcher[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "End_Screen_Memory"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    break_needed.keys = []
    break_needed.rt = []
    _break_needed_allKeys = []
    # keep track of which components have finished
    End_Screen_MemoryComponents = [end_memory, break_needed]
    for thisComponent in End_Screen_MemoryComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    End_Screen_MemoryClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "End_Screen_Memory"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = End_Screen_MemoryClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=End_Screen_MemoryClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_memory* updates
        if end_memory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_memory.frameNStart = frameN  # exact frame index
            end_memory.tStart = t  # local t and not account for scr refresh
            end_memory.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_memory, 'tStartRefresh')  # time at next scr refresh
            end_memory.setAutoDraw(True)
        if end_memory.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_memory.tStartRefresh + 10.0-frameTolerance:
                # keep track of stop time/frame for later
                end_memory.tStop = t  # not accounting for scr refresh
                end_memory.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_memory, 'tStopRefresh')  # time at next scr refresh
                end_memory.setAutoDraw(False)
        
        # *break_needed* updates
        waitOnFlip = False
        if break_needed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_needed.frameNStart = frameN  # exact frame index
            break_needed.tStart = t  # local t and not account for scr refresh
            break_needed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_needed, 'tStartRefresh')  # time at next scr refresh
            break_needed.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_needed.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_needed.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_needed.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > break_needed.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                break_needed.tStop = t  # not accounting for scr refresh
                break_needed.frameNStop = frameN  # exact frame index
                win.timeOnFlip(break_needed, 'tStopRefresh')  # time at next scr refresh
                break_needed.status = FINISHED
        if break_needed.status == STARTED and not waitOnFlip:
            theseKeys = break_needed.getKeys(keyList=['1'], waitRelease=False)
            _break_needed_allKeys.extend(theseKeys)
            if len(_break_needed_allKeys):
                break_needed.keys = _break_needed_allKeys[-1].name  # just the last key pressed
                break_needed.rt = _break_needed_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_Screen_MemoryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "End_Screen_Memory"-------
    for thisComponent in End_Screen_MemoryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    break_catcher.addData('end_memory.started', end_memory.tStartRefresh)
    break_catcher.addData('end_memory.stopped', end_memory.tStopRefresh)
    # check responses
    if break_needed.keys in ['', [], None]:  # No response was made
        break_needed.keys = None
    break_catcher.addData('break_needed.keys',break_needed.keys)
    if break_needed.keys != None:  # we had a response
        break_catcher.addData('break_needed.rt', break_needed.rt)
    break_catcher.addData('break_needed.started', break_needed.tStartRefresh)
    break_catcher.addData('break_needed.stopped', break_needed.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'break_catcher'


# ------Prepare to start Routine "break_time"-------
continueRoutine = True
# update component parameters for each repeat
end_task.keys = []
end_task.rt = []
_end_task_allKeys = []
# keep track of which components have finished
break_timeComponents = [text_3, end_task]
for thisComponent in break_timeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_timeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_time"-------
while continueRoutine:
    # get current time
    t = break_timeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_timeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        if bool(break_catcher.data['break_needed.keys'] !='1'):
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # *end_task* updates
    waitOnFlip = False
    if end_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_task.frameNStart = frameN  # exact frame index
        end_task.tStart = t  # local t and not account for scr refresh
        end_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_task, 'tStartRefresh')  # time at next scr refresh
        end_task.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_task.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_task.status == STARTED and not waitOnFlip:
        theseKeys = end_task.getKeys(keyList=['1'], waitRelease=False)
        _end_task_allKeys.extend(theseKeys)
        if len(_end_task_allKeys):
            end_task.keys = _end_task_allKeys[-1].name  # just the last key pressed
            end_task.rt = _end_task_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_timeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_time"-------
for thisComponent in break_timeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if end_task.keys in ['', [], None]:  # No response was made
    end_task.keys = None
thisExp.addData('end_task.keys',end_task.keys)
if end_task.keys != None:  # we had a response
    thisExp.addData('end_task.rt', end_task.rt)
thisExp.addData('end_task.started', end_task.tStartRefresh)
thisExp.addData('end_task.stopped', end_task.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_time" was not non-slip safe, so reset the non-slip timer
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
