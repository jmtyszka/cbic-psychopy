#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on September 28, 2022, at 14:08
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

# Movie file selector
mp4_fname = gui.fileOpenDlg(prompt='Select Movie', allowed='*.mp4')[0]

if mp4_fname:
    print(f'Selected {mp4_fname}')
else:
    print('User cancelled - exiting')
    core.quit()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'MovieWithEyetracking'  # from the Builder filename that created this script
expInfo = {'participant': 'Damy001'}
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
    originPath='D:\\Adolphslab\\psychopy\\cbic-psychopy\\MovieWithEyetracking\\MovieWithEyetracking_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.INFO)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 960], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='hPrisma Projector', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = 'eyetracker.hw.sr_research.eyelink.EyeTracker'
ioConfig = {
    ioDevice: {
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
}
ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='MovieWithEyetracking', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "et_instructions"
et_instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='EYE TRACKER SETUP\n\nPlease stare at the moving dots when they appear\n\nPRESS BUTTON 1 TO CONTINUE',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=0.9, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
et_continue = keyboard.Keyboard()

# Initialize components for Routine "sound_check_instr"
sound_check_instrClock = core.Clock()
sound_check_text = visual.TextStim(win=win, name='sound_check_text',
    text='SOUND LEVEL CHECK\n\nPress 1 for louder\nPress 2 for quieter\nPress 4 to accept\n\nCLOSE YOUR EYES then PRESS BUTTON 1',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=0.9, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_check_inst_text = keyboard.Keyboard()

# Initialize components for Routine "trigger_wait"
trigger_waitClock = core.Clock()
trigger_detect = keyboard.Keyboard()
trigger_wait_text = visual.TextStim(win=win, name='trigger_wait_text',
    text='Waiting for scanner ...',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=0.9, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "sound_check"
sound_checkClock = core.Clock()
movie_check = visual.MovieStim3(
    win=win, name='movie_check',
    noAudio = False,
    filename=mp4_fname.replace('.mp4', '_soundcheck.mp4'),
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    depth=0.0,
    )
adjust = keyboard.Keyboard()

# Initialize components for Routine "play_movie_instr"
play_movie_instrClock = core.Clock()
play_movie_instr_text = visual.TextStim(win=win, name='play_movie_instr_text',
    text='The sound check is complete!\n\nThe movie will start shortly.\n\nWaiting for operator ...',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=0.9, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
play_movie_trigger = keyboard.Keyboard()

# Initialize components for Routine "trigger_wait"
trigger_waitClock = core.Clock()
trigger_detect = keyboard.Keyboard()
trigger_wait_text = visual.TextStim(win=win, name='trigger_wait_text',
    text='Waiting for scanner ...',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=0.9, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "play_movie"
play_movieClock = core.Clock()
et_record = hardware.eyetracker.EyetrackerControl(
    server=ioServer,
    tracker=eyetracker
)
movie_player = visual.MovieStim3(
    win=win, name='movie_player',units='cm', 
    noAudio = False,
    filename=mp4_fname,
    ori=0.0, pos=(0, 0), opacity=None,
    loop=False,
    size=[36.0, 20.3],
    depth=-1.0,
    )

# Initialize components for Routine "post_movie"
post_movieClock = core.Clock()
thanks_text = visual.TextStim(win=win, name='thanks_text',
    text='Thanks for watching!',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=0.9, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "et_instructions"-------
continueRoutine = True
# update component parameters for each repeat
et_continue.keys = []
et_continue.rt = []
_et_continue_allKeys = []
# keep track of which components have finished
et_instructionsComponents = [text, et_continue]
for thisComponent in et_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
et_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "et_instructions"-------
while continueRoutine:
    # get current time
    t = et_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=et_instructionsClock)
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
    
    # *et_continue* updates
    waitOnFlip = False
    if et_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        et_continue.frameNStart = frameN  # exact frame index
        et_continue.tStart = t  # local t and not account for scr refresh
        et_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(et_continue, 'tStartRefresh')  # time at next scr refresh
        et_continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(et_continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(et_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if et_continue.status == STARTED and not waitOnFlip:
        theseKeys = et_continue.getKeys(keyList=['1'], waitRelease=False)
        _et_continue_allKeys.extend(theseKeys)
        if len(_et_continue_allKeys):
            et_continue.keys = _et_continue_allKeys[-1].name  # just the last key pressed
            et_continue.rt = _et_continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in et_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "et_instructions"-------
for thisComponent in et_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if et_continue.keys in ['', [], None]:  # No response was made
    et_continue.keys = None
thisExp.addData('et_continue.keys',et_continue.keys)
if et_continue.keys != None:  # we had a response
    thisExp.addData('et_continue.rt', et_continue.rt)
thisExp.addData('et_continue.started', et_continue.tStartRefresh)
thisExp.addData('et_continue.stopped', et_continue.tStopRefresh)
thisExp.nextEntry()
# the Routine "et_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    targetLayout='FIVE_POINTS', randomisePos=True,
    movementAnimation=False, targetDelay=1.0
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
    positions='FIVE_POINTS', randomize_positions=True,
    expand_scale=1.25, target_duration=1.5,
    enable_position_animation=False, target_delay=1.0,
    progress_on_key=None,
    show_results_screen=True, save_results_screen=True,
    color_space='rgb', unit_type=None
)
# run validation
validation.run()
# clear any keypresses from during validation so they don't interfere with the experiment
defaultKeyboard.clearEvents()
# the Routine "validation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sound_check_instr"-------
continueRoutine = True
# update component parameters for each repeat
sound_check_inst_text.keys = []
sound_check_inst_text.rt = []
_sound_check_inst_text_allKeys = []
# keep track of which components have finished
sound_check_instrComponents = [sound_check_text, sound_check_inst_text]
for thisComponent in sound_check_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sound_check_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sound_check_instr"-------
while continueRoutine:
    # get current time
    t = sound_check_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sound_check_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sound_check_text* updates
    if sound_check_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_check_text.frameNStart = frameN  # exact frame index
        sound_check_text.tStart = t  # local t and not account for scr refresh
        sound_check_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sound_check_text, 'tStartRefresh')  # time at next scr refresh
        sound_check_text.setAutoDraw(True)
    
    # *sound_check_inst_text* updates
    waitOnFlip = False
    if sound_check_inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sound_check_inst_text.frameNStart = frameN  # exact frame index
        sound_check_inst_text.tStart = t  # local t and not account for scr refresh
        sound_check_inst_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sound_check_inst_text, 'tStartRefresh')  # time at next scr refresh
        sound_check_inst_text.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sound_check_inst_text.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sound_check_inst_text.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sound_check_inst_text.status == STARTED and not waitOnFlip:
        theseKeys = sound_check_inst_text.getKeys(keyList=['1'], waitRelease=False)
        _sound_check_inst_text_allKeys.extend(theseKeys)
        if len(_sound_check_inst_text_allKeys):
            sound_check_inst_text.keys = _sound_check_inst_text_allKeys[-1].name  # just the last key pressed
            sound_check_inst_text.rt = _sound_check_inst_text_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sound_check_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sound_check_instr"-------
for thisComponent in sound_check_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('sound_check_text.started', sound_check_text.tStartRefresh)
thisExp.addData('sound_check_text.stopped', sound_check_text.tStopRefresh)
# check responses
if sound_check_inst_text.keys in ['', [], None]:  # No response was made
    sound_check_inst_text.keys = None
thisExp.addData('sound_check_inst_text.keys',sound_check_inst_text.keys)
if sound_check_inst_text.keys != None:  # we had a response
    thisExp.addData('sound_check_inst_text.rt', sound_check_inst_text.rt)
thisExp.addData('sound_check_inst_text.started', sound_check_inst_text.tStartRefresh)
thisExp.addData('sound_check_inst_text.stopped', sound_check_inst_text.tStopRefresh)
thisExp.nextEntry()
# the Routine "sound_check_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trigger_wait"-------
continueRoutine = True
# update component parameters for each repeat
trigger_detect.keys = []
trigger_detect.rt = []
_trigger_detect_allKeys = []
# keep track of which components have finished
trigger_waitComponents = [trigger_detect, trigger_wait_text]
for thisComponent in trigger_waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trigger_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trigger_wait"-------
while continueRoutine:
    # get current time
    t = trigger_waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trigger_waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_detect* updates
    waitOnFlip = False
    if trigger_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_detect.frameNStart = frameN  # exact frame index
        trigger_detect.tStart = t  # local t and not account for scr refresh
        trigger_detect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_detect, 'tStartRefresh')  # time at next scr refresh
        trigger_detect.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_detect.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_detect.status == STARTED and not waitOnFlip:
        theseKeys = trigger_detect.getKeys(keyList=['5'], waitRelease=False)
        _trigger_detect_allKeys.extend(theseKeys)
        if len(_trigger_detect_allKeys):
            trigger_detect.keys = _trigger_detect_allKeys[-1].name  # just the last key pressed
            trigger_detect.rt = _trigger_detect_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *trigger_wait_text* updates
    if trigger_wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_wait_text.frameNStart = frameN  # exact frame index
        trigger_wait_text.tStart = t  # local t and not account for scr refresh
        trigger_wait_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_wait_text, 'tStartRefresh')  # time at next scr refresh
        trigger_wait_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trigger_waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trigger_wait"-------
for thisComponent in trigger_waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_detect.keys in ['', [], None]:  # No response was made
    trigger_detect.keys = None
thisExp.addData('trigger_detect.keys',trigger_detect.keys)
if trigger_detect.keys != None:  # we had a response
    thisExp.addData('trigger_detect.rt', trigger_detect.rt)
thisExp.addData('trigger_detect.started', trigger_detect.tStartRefresh)
thisExp.addData('trigger_detect.stopped', trigger_detect.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('trigger_wait_text.started', trigger_wait_text.tStartRefresh)
thisExp.addData('trigger_wait_text.stopped', trigger_wait_text.tStopRefresh)
# the Routine "trigger_wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "sound_check"-------
continueRoutine = True
# update component parameters for each repeat
adjust.keys = []
adjust.rt = []
_adjust_allKeys = []
last_rt = -1.0
# keep track of which components have finished
sound_checkComponents = [movie_check, adjust]
for thisComponent in sound_checkComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
sound_checkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "sound_check"-------
while continueRoutine:
    # get current time
    t = sound_checkClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=sound_checkClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_check* updates
    if movie_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_check.frameNStart = frameN  # exact frame index
        movie_check.tStart = t  # local t and not account for scr refresh
        movie_check.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_check, 'tStartRefresh')  # time at next scr refresh
        movie_check.setAutoDraw(True)
    if movie_check.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
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
                print('LOUDER')
                sys.stdout.flush()
                
            if adjust.keys == '2':
                print('QUIETER')
                sys.stdout.flush() 
                
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
    for thisComponent in sound_checkComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "sound_check"-------
for thisComponent in sound_checkComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
movie_check.stop()
# check responses
if adjust.keys in ['', [], None]:  # No response was made
    adjust.keys = None
thisExp.addData('adjust.keys',adjust.keys)
if adjust.keys != None:  # we had a response
    thisExp.addData('adjust.rt', adjust.rt)
thisExp.addData('adjust.started', adjust.tStartRefresh)
thisExp.addData('adjust.stopped', adjust.tStopRefresh)
thisExp.nextEntry()
# the Routine "sound_check" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "play_movie_instr"-------
continueRoutine = True
# update component parameters for each repeat
play_movie_trigger.keys = []
play_movie_trigger.rt = []
_play_movie_trigger_allKeys = []
# keep track of which components have finished
play_movie_instrComponents = [play_movie_instr_text, play_movie_trigger]
for thisComponent in play_movie_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
play_movie_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "play_movie_instr"-------
while continueRoutine:
    # get current time
    t = play_movie_instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=play_movie_instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *play_movie_instr_text* updates
    if play_movie_instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        play_movie_instr_text.frameNStart = frameN  # exact frame index
        play_movie_instr_text.tStart = t  # local t and not account for scr refresh
        play_movie_instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(play_movie_instr_text, 'tStartRefresh')  # time at next scr refresh
        play_movie_instr_text.setAutoDraw(True)
    
    # *play_movie_trigger* updates
    waitOnFlip = False
    if play_movie_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        play_movie_trigger.frameNStart = frameN  # exact frame index
        play_movie_trigger.tStart = t  # local t and not account for scr refresh
        play_movie_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(play_movie_trigger, 'tStartRefresh')  # time at next scr refresh
        play_movie_trigger.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(play_movie_trigger.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(play_movie_trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if play_movie_trigger.status == STARTED and not waitOnFlip:
        theseKeys = play_movie_trigger.getKeys(keyList=['space'], waitRelease=False)
        _play_movie_trigger_allKeys.extend(theseKeys)
        if len(_play_movie_trigger_allKeys):
            play_movie_trigger.keys = _play_movie_trigger_allKeys[-1].name  # just the last key pressed
            play_movie_trigger.rt = _play_movie_trigger_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in play_movie_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "play_movie_instr"-------
for thisComponent in play_movie_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('play_movie_instr_text.started', play_movie_instr_text.tStartRefresh)
thisExp.addData('play_movie_instr_text.stopped', play_movie_instr_text.tStopRefresh)
# check responses
if play_movie_trigger.keys in ['', [], None]:  # No response was made
    play_movie_trigger.keys = None
thisExp.addData('play_movie_trigger.keys',play_movie_trigger.keys)
if play_movie_trigger.keys != None:  # we had a response
    thisExp.addData('play_movie_trigger.rt', play_movie_trigger.rt)
thisExp.addData('play_movie_trigger.started', play_movie_trigger.tStartRefresh)
thisExp.addData('play_movie_trigger.stopped', play_movie_trigger.tStopRefresh)
thisExp.nextEntry()
# the Routine "play_movie_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trigger_wait"-------
continueRoutine = True
# update component parameters for each repeat
trigger_detect.keys = []
trigger_detect.rt = []
_trigger_detect_allKeys = []
# keep track of which components have finished
trigger_waitComponents = [trigger_detect, trigger_wait_text]
for thisComponent in trigger_waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trigger_waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trigger_wait"-------
while continueRoutine:
    # get current time
    t = trigger_waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trigger_waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_detect* updates
    waitOnFlip = False
    if trigger_detect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_detect.frameNStart = frameN  # exact frame index
        trigger_detect.tStart = t  # local t and not account for scr refresh
        trigger_detect.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_detect, 'tStartRefresh')  # time at next scr refresh
        trigger_detect.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_detect.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_detect.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_detect.status == STARTED and not waitOnFlip:
        theseKeys = trigger_detect.getKeys(keyList=['5'], waitRelease=False)
        _trigger_detect_allKeys.extend(theseKeys)
        if len(_trigger_detect_allKeys):
            trigger_detect.keys = _trigger_detect_allKeys[-1].name  # just the last key pressed
            trigger_detect.rt = _trigger_detect_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *trigger_wait_text* updates
    if trigger_wait_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_wait_text.frameNStart = frameN  # exact frame index
        trigger_wait_text.tStart = t  # local t and not account for scr refresh
        trigger_wait_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_wait_text, 'tStartRefresh')  # time at next scr refresh
        trigger_wait_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trigger_waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trigger_wait"-------
for thisComponent in trigger_waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_detect.keys in ['', [], None]:  # No response was made
    trigger_detect.keys = None
thisExp.addData('trigger_detect.keys',trigger_detect.keys)
if trigger_detect.keys != None:  # we had a response
    thisExp.addData('trigger_detect.rt', trigger_detect.rt)
thisExp.addData('trigger_detect.started', trigger_detect.tStartRefresh)
thisExp.addData('trigger_detect.stopped', trigger_detect.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('trigger_wait_text.started', trigger_wait_text.tStartRefresh)
thisExp.addData('trigger_wait_text.stopped', trigger_wait_text.tStopRefresh)
# the Routine "trigger_wait" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "play_movie"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
play_movieComponents = [et_record, movie_player]
for thisComponent in play_movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
play_movieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "play_movie"-------
while continueRoutine:
    # get current time
    t = play_movieClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=play_movieClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *et_record* updates
    if et_record.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        et_record.frameNStart = frameN  # exact frame index
        et_record.tStart = t  # local t and not account for scr refresh
        et_record.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(et_record, 'tStartRefresh')  # time at next scr refresh
        et_record.status = STARTED
    
    # *movie_player* updates
    if movie_player.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        movie_player.frameNStart = frameN  # exact frame index
        movie_player.tStart = t  # local t and not account for scr refresh
        movie_player.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(movie_player, 'tStartRefresh')  # time at next scr refresh
        movie_player.setAutoDraw(True)
    if movie_player.status == FINISHED:  # force-end the routine
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in play_movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "play_movie"-------
for thisComponent in play_movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# make sure the eyetracker recording stops
if et_record.status != FINISHED:
    et_record.status = FINISHED
movie_player.stop()
# the Routine "play_movie" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "post_movie"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
post_movieComponents = [thanks_text]
for thisComponent in post_movieComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
post_movieClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "post_movie"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = post_movieClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=post_movieClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_text* updates
    if thanks_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_text.frameNStart = frameN  # exact frame index
        thanks_text.tStart = t  # local t and not account for scr refresh
        thanks_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_text, 'tStartRefresh')  # time at next scr refresh
        thanks_text.setAutoDraw(True)
    if thanks_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanks_text.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            thanks_text.tStop = t  # not accounting for scr refresh
            thanks_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanks_text, 'tStopRefresh')  # time at next scr refresh
            thanks_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in post_movieComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "post_movie"-------
for thisComponent in post_movieComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks_text.started', thanks_text.tStartRefresh)
thisExp.addData('thanks_text.stopped', thanks_text.tStopRefresh)

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
