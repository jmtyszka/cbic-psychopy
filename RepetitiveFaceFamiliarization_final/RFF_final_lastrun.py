#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.3),
    on October 04, 2022, at 10:53
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('latest')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
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
psychopyVersion = '2022.2.3'
expName = 'RFF_final'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='D:\\Adolphslab\\psychopy\\cbic-psychopy\\RepetitiveFaceFamiliarization_final\\RFF_final_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='hPrisma Projector', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.sr_research.eyelink.EyeTracker'] = {
    'name': 'tracker',
    'model_name': 'EYELINK 1000 LONG RANGE',
    'simulation_mode': False,
    'network_settings': '100.1.1.1',
    'default_native_data_file_name': 'EXPFILE',
    'runtime_settings': {
        'sampling_rate': 500.0,
        'track_eyes': 'RIGHT_EYE',
        'sample_filtering': {
            'sample_filtering': 'FILTER_LEVEL_2',
            'elLiveFiltering': 'FILTER_LEVEL_OFF',
        },
        'vog_settings': {
            'pupil_measure_types': 'PUPIL_AREA',
            'tracking_mode': 'PUPIL_CR_TRACKING',
            'pupil_center_algorithm': 'ELLIPSE_FIT',
        }
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "et_setup" ---
et_prompt = visual.TextStim(win=win, name='et_prompt',
    text='EYE TRACKER SETUP\n\nPlease stare at the moving dots when they appear\n\nPRESS BUTTON 1 TO CONTINUE\n\nPRESS BUTTON 6 TO SKIP',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
et_needed = keyboard.Keyboard()

# --- Initialize components for Routine "Introduction_Screen_Memory" ---
introduction_memory = visual.TextStim(win=win, name='introduction_memory',
    text='This is the start of  session '+str(expInfo['session'])+' out of a total of 3 face memory task. In this session, 124 pictures of different faces will be presented to you. Some of the pictures have occurred in previous scanning sessions, and some are completely new. \n Please use the numbers on the keyboard to indicate whether a face is OLD (key mappings will be shown on the next screen), and how confident you are of the choice. Please respond as fast as possible, as for each new/old judgement, the maximal response time allowed is 2 seconds.\n Please press key \'1\' to continue when you are ready and understand the instructions',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_memory = keyboard.Keyboard()

# --- Initialize components for Routine "button_scheme" ---
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
    image='icons/newold buttons odd.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.1), size=(1.5, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# --- Initialize components for Routine "Wait_for_Trigger" ---
TriggerText = visual.TextStim(win=win, name='TriggerText',
    text='Waiting for trigger...',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
TriggerCatcher = keyboard.Keyboard()

# --- Initialize components for Routine "Face_Presentation" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "ITI" ---
ITI_1_text = visual.TextStim(win=win, name='ITI_1_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "New_Old_Question" ---
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
    image='icons/newold buttons odd.bmp', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.1), size=(1.5, 0.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-1.0)
key_resp_2 = keyboard.Keyboard()
time_holder = visual.TextStim(win=win, name='time_holder',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "ITI_2" ---
ITI_2_text = visual.TextStim(win=win, name='ITI_2_text',
    text='+  ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "End_Screen_Memory" ---
end_memory = visual.TextStim(win=win, name='end_memory',
    text='Thank you for completing session ' +str(expInfo['session'])+ ' out of the total of 4 face memory sessions!! \n If you need a break, please press \'1\'. Otherwise, the task will exit in 10 seconds. We will move on to the next block.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break_needed = keyboard.Keyboard()
etRecord_2 = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Stop Only'
)

# --- Initialize components for Routine "break_time" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='We will be pausing for a short break before moving on to the next session :)',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_task = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
et_catcher = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='et_catcher')
thisExp.addLoop(et_catcher)  # add the loop to the experiment
thisEt_catcher = et_catcher.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEt_catcher.rgb)
if thisEt_catcher != None:
    for paramName in thisEt_catcher:
        exec('{} = thisEt_catcher[paramName]'.format(paramName))

for thisEt_catcher in et_catcher:
    currentLoop = et_catcher
    # abbreviate parameter names if possible (e.g. rgb = thisEt_catcher.rgb)
    if thisEt_catcher != None:
        for paramName in thisEt_catcher:
            exec('{} = thisEt_catcher[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "et_setup" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    et_needed.keys = []
    et_needed.rt = []
    _et_needed_allKeys = []
    # keep track of which components have finished
    et_setupComponents = [et_prompt, et_needed]
    for thisComponent in et_setupComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "et_setup" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *et_prompt* updates
        if et_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            et_prompt.frameNStart = frameN  # exact frame index
            et_prompt.tStart = t  # local t and not account for scr refresh
            et_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(et_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'et_prompt.started')
            et_prompt.setAutoDraw(True)
        
        # *et_needed* updates
        waitOnFlip = False
        if et_needed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            et_needed.frameNStart = frameN  # exact frame index
            et_needed.tStart = t  # local t and not account for scr refresh
            et_needed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(et_needed, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'et_needed.started')
            et_needed.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(et_needed.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(et_needed.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if et_needed.status == STARTED and not waitOnFlip:
            theseKeys = et_needed.getKeys(keyList=['1', '6'], waitRelease=False)
            _et_needed_allKeys.extend(theseKeys)
            if len(_et_needed_allKeys):
                et_needed.keys = _et_needed_allKeys[-1].name  # just the last key pressed
                et_needed.rt = _et_needed_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in et_setupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "et_setup" ---
    for thisComponent in et_setupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if et_needed.keys in ['', [], None]:  # No response was made
        et_needed.keys = None
    et_catcher.addData('et_needed.keys',et_needed.keys)
    if et_needed.keys != None:  # we had a response
        et_catcher.addData('et_needed.rt', et_needed.rt)
    # the Routine "et_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'et_catcher'


# set up handler to look after randomisation of conditions etc
eyetracking_enabled = data.TrialHandler(nReps=et_catcher.data['et_needed.keys'] =='1', method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='eyetracking_enabled')
thisExp.addLoop(eyetracking_enabled)  # add the loop to the experiment
thisEyetracking_enabled = eyetracking_enabled.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEyetracking_enabled.rgb)
if thisEyetracking_enabled != None:
    for paramName in thisEyetracking_enabled:
        exec('{} = thisEyetracking_enabled[paramName]'.format(paramName))

for thisEyetracking_enabled in eyetracking_enabled:
    currentLoop = eyetracking_enabled
    # abbreviate parameter names if possible (e.g. rgb = thisEyetracking_enabled.rgb)
    if thisEyetracking_enabled != None:
        for paramName in thisEyetracking_enabled:
            exec('{} = thisEyetracking_enabled[paramName]'.format(paramName))
    # define target for calibration
    calibrationTarget = visual.TargetStim(win, 
        name='calibrationTarget',
        radius=0.07, fillColor='', borderColor='black', lineWidth=2.0,
        innerRadius=0.025, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for calibration
    calibration = hardware.eyetracker.EyetrackerCalibration(win, 
        eyetracker, calibrationTarget,
        units=None, colorSpace='rgb',
        progressMode='time', targetDur=1.0, expandScale=1.25,
        targetLayout='NINE_POINTS', randomisePos=True, textColor='white',
        movementAnimation=False, targetDelay=1.0
    )
    # run calibration
    calibration.run()
    # clear any keypresses from during calibration so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # define target for validation
    validationTarget = visual.TargetStim(win, 
        name='validationTarget',
        radius=0.07, fillColor='', borderColor='black', lineWidth=2.0,
        innerRadius=0.025, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for validation
    validation = iohub.ValidationProcedure(win,
        target=validationTarget,
        gaze_cursor='green', 
        positions='NINE_POINTS', randomize_positions=False,
        expand_scale=1.25, target_duration=1.0,
        enable_position_animation=False, target_delay=1.0,
        progress_on_key=None, text_color='auto',
        show_results_screen=True, save_results_screen=True,
        color_space='rgb', unit_type=None
    )
    # run validation
    validation.run()
    # clear any keypresses from during validation so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "validation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed et_catcher.data['et_needed.keys'] =='1' repeats of 'eyetracking_enabled'


# --- Prepare to start Routine "Introduction_Screen_Memory" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "Introduction_Screen_Memory" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'introduction_memory.started')
        introduction_memory.setAutoDraw(True)
    
    # *start_memory* updates
    waitOnFlip = False
    if start_memory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_memory.frameNStart = frameN  # exact frame index
        start_memory.tStart = t  # local t and not account for scr refresh
        start_memory.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_memory, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'start_memory.started')
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Introduction_Screen_MemoryComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Introduction_Screen_Memory" ---
for thisComponent in Introduction_Screen_MemoryComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start_memory.keys in ['', [], None]:  # No response was made
    start_memory.keys = None
thisExp.addData('start_memory.keys',start_memory.keys)
if start_memory.keys != None:  # we had a response
    thisExp.addData('start_memory.rt', start_memory.rt)
thisExp.nextEntry()
# the Routine "Introduction_Screen_Memory" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "button_scheme" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "button_scheme" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *button_confirmation* updates
    waitOnFlip = False
    if button_confirmation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_confirmation.frameNStart = frameN  # exact frame index
        button_confirmation.tStart = t  # local t and not account for scr refresh
        button_confirmation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_confirmation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'button_confirmation.started')
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'scheme_image.started')
        scheme_image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in button_schemeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "button_scheme" ---
for thisComponent in button_schemeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if button_confirmation.keys in ['', [], None]:  # No response was made
    button_confirmation.keys = None
thisExp.addData('button_confirmation.keys',button_confirmation.keys)
if button_confirmation.keys != None:  # we had a response
    thisExp.addData('button_confirmation.rt', button_confirmation.rt)
thisExp.nextEntry()
# the Routine "button_scheme" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Wait_for_Trigger" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "Wait_for_Trigger" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TriggerText.started')
        TriggerText.setAutoDraw(True)
    
    # *TriggerCatcher* updates
    waitOnFlip = False
    if TriggerCatcher.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TriggerCatcher.frameNStart = frameN  # exact frame index
        TriggerCatcher.tStart = t  # local t and not account for scr refresh
        TriggerCatcher.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TriggerCatcher, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'TriggerCatcher.started')
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_for_TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Wait_for_Trigger" ---
for thisComponent in Wait_for_TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if TriggerCatcher.keys in ['', [], None]:  # No response was made
    TriggerCatcher.keys = None
thisExp.addData('TriggerCatcher.keys',TriggerCatcher.keys)
if TriggerCatcher.keys != None:  # we had a response
    thisExp.addData('TriggerCatcher.rt', TriggerCatcher.rt)
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
    
    # --- Prepare to start Routine "Face_Presentation" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "Face_Presentation" ---
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 1.5-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Face_PresentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Face_Presentation" ---
    for thisComponent in Face_PresentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "ITI" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_1_text.started')
            ITI_1_text.setAutoDraw(True)
        if ITI_1_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_1_text.tStartRefresh + ITI_1-frameTolerance:
                # keep track of stop time/frame for later
                ITI_1_text.tStop = t  # not accounting for scr refresh
                ITI_1_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_1_text.stopped')
                ITI_1_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI" ---
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "New_Old_Question" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "New_Old_Question" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_old_question.started')
            new_old_question.setAutoDraw(True)
        if new_old_question.status == STARTED:
            if bool(len(key_resp_2.keys) != 0 or tThisFlipGlobal > new_old_question.tStartRefresh + 2-frameTolerance*8):
                # keep track of stop time/frame for later
                new_old_question.tStop = t  # not accounting for scr refresh
                new_old_question.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'new_old_question.stopped')
                new_old_question.setAutoDraw(False)
        
        # *new_old_prompt* updates
        if new_old_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_old_prompt.frameNStart = frameN  # exact frame index
            new_old_prompt.tStart = t  # local t and not account for scr refresh
            new_old_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_old_prompt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_old_prompt.started')
            new_old_prompt.setAutoDraw(True)
        if new_old_prompt.status == STARTED:
            if bool(len(key_resp_2.keys) != 0 or tThisFlipGlobal > new_old_question.tStartRefresh + 2-frameTolerance*8):
                # keep track of stop time/frame for later
                new_old_prompt.tStop = t  # not accounting for scr refresh
                new_old_prompt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'new_old_prompt.stopped')
                new_old_prompt.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            if bool(len(key_resp_2.keys) != 0 or tThisFlipGlobal > new_old_question.tStartRefresh + 2-frameTolerance*8):
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['1','2','3','6','7','8'], waitRelease=False)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'time_holder.started')
            time_holder.setAutoDraw(True)
        if time_holder.status == STARTED:
            if bool(tThisFlipGlobal > new_old_question.tStartRefresh + 2-frameTolerance*8):
                # keep track of stop time/frame for later
                time_holder.tStop = t  # not accounting for scr refresh
                time_holder.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'time_holder.stopped')
                time_holder.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in New_Old_QuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "New_Old_Question" ---
    for thisComponent in New_Old_QuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    repeat.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        repeat.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "New_Old_Question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI_2" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "ITI_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ITI_2_text.started')
            ITI_2_text.setAutoDraw(True)
        if ITI_2_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ITI_2_text.tStartRefresh + ITI_2-frameTolerance:
                # keep track of stop time/frame for later
                ITI_2_text.tStop = t  # not accounting for scr refresh
                ITI_2_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ITI_2_text.stopped')
                ITI_2_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ITI_2" ---
    for thisComponent in ITI_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "ITI_2" was not non-slip safe, so reset the non-slip timer
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
    
    # --- Prepare to start Routine "End_Screen_Memory" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    break_needed.keys = []
    break_needed.rt = []
    _break_needed_allKeys = []
    # keep track of which components have finished
    End_Screen_MemoryComponents = [end_memory, break_needed, etRecord_2]
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
    frameN = -1
    
    # --- Run Routine "End_Screen_Memory" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_memory.started')
            end_memory.setAutoDraw(True)
        if end_memory.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_memory.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                end_memory.tStop = t  # not accounting for scr refresh
                end_memory.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'end_memory.stopped')
                end_memory.setAutoDraw(False)
        
        # *break_needed* updates
        waitOnFlip = False
        if break_needed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_needed.frameNStart = frameN  # exact frame index
            break_needed.tStart = t  # local t and not account for scr refresh
            break_needed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_needed, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break_needed.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_needed.stopped')
                break_needed.status = FINISHED
        if break_needed.status == STARTED and not waitOnFlip:
            theseKeys = break_needed.getKeys(keyList=['1', '6'], waitRelease=False)
            _break_needed_allKeys.extend(theseKeys)
            if len(_break_needed_allKeys):
                break_needed.keys = _break_needed_allKeys[-1].name  # just the last key pressed
                break_needed.rt = _break_needed_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *etRecord_2* updates
        if etRecord_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            etRecord_2.frameNStart = frameN  # exact frame index
            etRecord_2.tStart = t  # local t and not account for scr refresh
            etRecord_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRecord_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('etRecord_2.started', t)
            etRecord_2.status = STARTED
        if etRecord_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > etRecord_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                etRecord_2.tStop = t  # not accounting for scr refresh
                etRecord_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('etRecord_2.stopped', t)
                etRecord_2.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in End_Screen_MemoryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "End_Screen_Memory" ---
    for thisComponent in End_Screen_MemoryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if break_needed.keys in ['', [], None]:  # No response was made
        break_needed.keys = None
    break_catcher.addData('break_needed.keys',break_needed.keys)
    if break_needed.keys != None:  # we had a response
        break_catcher.addData('break_needed.rt', break_needed.rt)
    # make sure the eyetracker recording stops
    if etRecord_2.status != FINISHED:
        etRecord_2.status = FINISHED
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'break_catcher'


# --- Prepare to start Routine "break_time" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "break_time" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and break_catcher.data['break_needed.keys'] =='1':
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + break_catcher.data['break_needed.keys'] !='1'-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # *end_task* updates
    waitOnFlip = False
    if end_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_task.frameNStart = frameN  # exact frame index
        end_task.tStart = t  # local t and not account for scr refresh
        end_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_task, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_task.started')
        end_task.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_task.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_task.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_task.tStartRefresh + 8-frameTolerance:
            # keep track of stop time/frame for later
            end_task.tStop = t  # not accounting for scr refresh
            end_task.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_task.stopped')
            end_task.status = FINISHED
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_timeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "break_time" ---
for thisComponent in break_timeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_task.keys in ['', [], None]:  # No response was made
    end_task.keys = None
thisExp.addData('end_task.keys',end_task.keys)
if end_task.keys != None:  # we had a response
    thisExp.addData('end_task.rt', end_task.rt)
thisExp.nextEntry()
# the Routine "break_time" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
