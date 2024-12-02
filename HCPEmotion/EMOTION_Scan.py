#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Part of the Human Connectome - Lifespan Project Task fMRI Battery
Psychopy implementation by Erik K Kastman, Constanza M Vidal Bustamente, and Leah H Somerville
**********************************************************************************************
Tested with Psychopy 1.83.04; Psyexp Experiment Builder XML available upon request
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
import datetime
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Common HCP Tools
import hcpcommon
hcpcommon.checkScreenCount()
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'EMOTION'  # from the Builder filename that created this script
expInfo = {u'mriMode': u'scan', u'sessionID': u'', u'counterbalance': u'',}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.path.sep + '_'.join([expName, expInfo['sessionID'], 'run1', expInfo['date']])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
## EKK Screen Edit of compiled script
import pyglet
display = pyglet.window.get_platform().get_default_display()
screens = display.get_screens()
resolution = [screens[-1].width, screens[-1].height]
import yaml
from psychopy import monitors
if not os.path.exists('siteConfig.yaml'): raise IOError('Missing siteConfig.yaml - Please copy configuration text file')
with open('siteConfig.yaml') as f:
    config = yaml.safe_load(f)
mon = monitors.Monitor('newMonitor')
mon.setWidth(config['monitor']['width'])
mon.setDistance(config['monitor']['distance'])
mon.setSizePix(resolution)

# Setup the Window
win = visual.Window(size=resolution, fullscr=False, screen=config['monitor']['screen'], allowGUI=False, allowStencil=False,
    monitor=mon, color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
import yaml
import itertools

if os.path.exists('siteConfig.yaml'):
    with open('siteConfig.yaml') as f:
        config = yaml.safe_load(f)
else:
    copyMsg = ('Please copy configuration text file '
               '"siteConfig.yaml.example" to "siteConfig.yaml" '
               'and edit it with your trigger and buttons.')
    raise IOError(copyMsg)

logging.exp('Using Site Configuration: %s' % config)
allowed_keys = list(itertools.chain.from_iterable(
    config['keys'].values()))

nRuns = 1

counterbalance = expInfo['counterbalance']
if counterbalance not in ['CB1', 'CB2', 'CB3', 'practice']:
    raise ValueError('counterbalance must be one of "CB1", "CB2", "CB3", or "practice" (capitalization counts), but it was %s' % counterbalance)
elif expInfo['counterbalance'] == 'practice':
    nBlocks= 2
    session = 0
    mode = 'practice'
    condFile = 'conditions/practice.csv'
else:
    nBlocks= 6
    session = 1
    mode = 'scan'
    condFile = 'conditions/trials%s.csv' % counterbalance

titleLetterSize = config['style']['titleLetterSize']  # 3
textLetterSize = config['style']['textLetterSize']  # 1.5
fixLetterSize = config['style']['fixLetterSize']  # 2.5
subtitleLetterSize = config['style']['subtitleLetterSize']  # .7
wrapWidth = config['style']['wrapWidth']  # 30

imageSize = [4, 4]
trialTopPos = [0, 4]
trialLeftPos = [-4, -1.25]
trialRightPos = [4, -1.25]

introText = visual.TextStim(win=win, ori=0, name='introText',
    text='MATCHING',    font='Arial',
    pos=[0, 2], height=titleLetterSize, wrapWidth=wrapWidth,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
# Setup the RA Experimenter Window
raWin = visual.Window(size=[1280,800], fullscr=False, allowGUI=True, allowStencil=False,
    monitor=u'testMonitor', color=u'black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg',
    screen=0)

raText= visual.TextStim(win=raWin, ori=0, name='raText',
    text='',    font='Arial',
    pos=[0, -4], height=textLetterSize * 1.5, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

raVerbalText = visual.TextStim(win=raWin, ori=0, name='raVerbalText',
    text='', font='Arial',
    pos=[0,3], height=textLetterSize * 1.5, wrapWidth=30,
    color='#3EB4F0', colorSpace='rgb', opacity=1,
    depth=0.0, italic=True)
outerFrame = visual.Rect(win=win, lineWidth=1, lineColor='white',
                         width=16.4, height=12.4, units='deg')

pointerXoffset = 4
pointerYoffset = -4.5

pointerLabelPrompt = visual.TextStim(win=win, height=subtitleLetterSize,
                             text='', pos=(-pointerXoffset, pointerYoffset), name='pointerLabelPrompt')
pointerFingerPrompt = visual.TextStim(win=win, height=subtitleLetterSize,
                             text='POINTER FINGER', pos=(-pointerXoffset, pointerYoffset-1),  name='pointerFingerPrompt')
middleLabelPrompt = visual.TextStim(win=win, height=subtitleLetterSize,
                             text='', pos=(pointerXoffset, pointerYoffset),  name='middleLabelPrompt')
middleFingerPrompt = visual.TextStim(win=win, height=subtitleLetterSize,
                             text='MIDDLE FINGER', pos=(pointerXoffset, pointerYoffset-1),  name='middleFingerPrompt')

pointerLabelPrompt.text = 'Bottom left'
middleLabelPrompt.text = 'Bottom right'

buttonPrompts = [pointerLabelPrompt, pointerFingerPrompt, 
                 middleLabelPrompt, middleFingerPrompt]

# outerFrame.autoDraw = True
introText2 = visual.TextStim(win=win, ori=0, name='introText2',
    text='GAME',    font='Arial',
    pos=[0, -2], height=titleLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
# Record Git Status in Subject Logs
from subprocess import check_output, check_call, CalledProcessError
try:
    revision = check_output(['git','rev-parse', '--short', 'HEAD'])
    revision = revision.strip()
    gitInstalled = True
except:
    if os.path.exists('VERSION'):
        with open('VERSION', 'r') as f:
            revision = f.read().strip()
    else:
        revision = ''
    gitInstalled = False

if gitInstalled:
    try:
        check_call(['git', 'diff-files', '--quiet'])
    except CalledProcessError:
        revision = 'Task changes detected. Nearest head: %s' % revision
        status_msg = check_output(['git', 'status'])
        msg ="""%s

Warning: the experiment has unexpected changes.
""" % status_msg
        logging.critical(msg)
        # core.quit()

expInfo['git-revision'] = revision
logging.exp('git-revision: %s' % revision)
import hcpcommon
movieClock = core.Clock()

record_example, cleanup = False, True

winRecorder = hcpcommon.WinRecorder(win=win, 
                                    clock=movieClock, 
                                    record=record_example,
                                    cleanup=cleanup)

raWinRecorder = hcpcommon.WinRecorder(win=raWin, 
                                      clock=movieClock, 
                                      record=record_example,
                                      cleanup=cleanup)

def save_movie(filename, recorder1, recorder2):
    win_fname = filename + '_win-movie.png'
    rawin_fname = filename + '_rawin-movie.png'

    # Save stills and convert to .mov
    recorder1.save(win_fname)
    recorder2.save(rawin_fname)
    movie_outfile = filename + '_EXAMPLE.mov'
    hcpcommon.WinRecorder.save_sidebyside([recorder1, recorder2], 
                                          movie_outfile)
    print('Saved %s' % movie_outfile)
    return movie_outfile


# Initialize components for Routine "pracInstr1"
pracInstr1Clock = core.Clock()
top_image = visual.ImageStim(win=win, name='top_image',
    image='images/FA-mock_top.jpg', mask=None,
    ori=0, pos=trialTopPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left_image = visual.ImageStim(win=win, name='left_image',
    image='images/FA-mock_left.jpg', mask=None,
    ori=0, pos=trialLeftPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right_image = visual.ImageStim(win=win, name='right_image',
    image='images/FA-mock_right.jpg', mask=None,
    ori=0, pos=trialRightPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)





# Initialize components for Routine "pracInstr2"
pracInstr2Clock = core.Clock()
top = visual.ImageStim(win=win, name='top',
    image='images/FA-mock_top.jpg', mask=None,
    ori=0, pos=trialTopPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left = visual.ImageStim(win=win, name='left',
    image='images/FA-mock_left.jpg', mask=None,
    ori=0, pos=trialLeftPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right = visual.ImageStim(win=win, name='right',
    image='images/FA-mock_right.jpg', mask=None,
    ori=0, pos=trialRightPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
pointerFinger = visual.ImageStim(win=win, name='pointerFinger',
    image='images/pointerFingerButton.png', mask=None,
    ori=0, pos=[0,-2.5], size=[367./454 * 4, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "pracInstr3"
pracInstr3Clock = core.Clock()
top3 = visual.ImageStim(win=win, name='top3',
    image='images/oval-vertical.bmp', mask=None,
    ori=0, pos=trialTopPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left3 = visual.ImageStim(win=win, name='left3',
    image='images/circle.bmp', mask=None,
    ori=0, pos=trialLeftPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
right3 = visual.ImageStim(win=win, name='right3',
    image='images/oval-vertical.bmp', mask=None,
    ori=0, pos=trialRightPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
middleFinger = visual.ImageStim(win=win, name='middleFinger',
    image='images/middleFingerButton.png', mask=None,
    ori=0, pos=[0,-2.5], size=[407./456 * 4, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "pracInstr4"
pracInstr4Clock = core.Clock()
exTopImage = visual.ImageStim(win=win, name='exTopImage',
    image='sin', mask=None,
    ori=0, pos=trialTopPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
exLeftImage = visual.ImageStim(win=win, name='exLeftImage',
    image='sin', mask=None,
    ori=0, pos=trialLeftPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
exRightImage = visual.ImageStim(win=win, name='exRightImage',
    image='sin', mask=None,
    ori=0, pos=trialRightPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "pracInstr5"
pracInstr5Clock = core.Clock()
pracInstr5Text = visual.TextStim(win=win, ori=0, name='pracInstr5Text',
    text="Let's practice. ",    font='Arial',
    pos=[0, 0], height=textLetterSize, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "exampleTrial"
exampleTrialClock = core.Clock()
topImageExample = visual.ImageStim(win=win, name='topImageExample',
    image='sin', mask=None,
    ori=0, pos=trialTopPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
leftImageExample = visual.ImageStim(win=win, name='leftImageExample',
    image='sin', mask=None,
    ori=0, pos=trialLeftPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rightImageExample = visual.ImageStim(win=win, name='rightImageExample',
    image='sin', mask=None,
    ori=0, pos=trialRightPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
botLeftTextExample = visual.TextStim(win=win, ori=0, name='botLeftTextExample',
    text=None,    font='Arial',
    pos=[-9,-9], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
botRightTextExample = visual.TextStim(win=win, ori=0, name='botRightTextExample',
    text=None,    font='Arial',
    pos=[9,-9], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
pointerTextExample = visual.TextStim(win=win, ori=0, name='pointerTextExample',
    text=None,    font='Arial',
    pos=[-9,-10.5], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
middleTextExample = visual.TextStim(win=win, ori=0, name='middleTextExample',
    text=None,    font='Arial',
    pos=[9,-10.5], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)



# Initialize components for Routine "fixation"
fixationClock = core.Clock()
cross = visual.TextStim(win=win, ori=0, name='cross',
    text='+',    font='Arial',
    pos=[0, 0], height=fixLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedbackText = visual.TextStim(win=win, ori=0, name='feedbackText',
    text='default text',    font='Arial',
    pos=[0, 0], height=textLetterSize, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "pracInstr6"
pracInstr6Clock = core.Clock()
pracInstr6Text = visual.TextStim(win=win, ori=0, name='pracInstr6Text',
    text='Do you have any questions?',    font='Arial',
    pos=[0, 0], height=textLetterSize, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "pracInstr7"
pracInstr7Clock = core.Clock()
pracInstr7Text = visual.TextStim(win=win, ori=0, name='pracInstr7Text',
    text='Are you ready to begin the practice?',    font='Arial',
    pos=[0, 0], height=textLetterSize, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "scanInstr1"
scanInstr1Clock = core.Clock()
##########################################
# Layout variables for Instruction Slide #
##########################################
y1 = 4
y2 = 0
x1 = -4
x1left = x1 - 2.25
x1right = x1 + 2.25
x2 = 4
x2left = x2 - 2.25
x2right = x2 + 2.25
stimSize = [3.75, 3.75]
faceTop = visual.ImageStim(win=win, name='faceTop',
    image='images/FF-mock_top.jpg', mask=None,
    ori=0, pos=(x2, y1), size=stimSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
faceLeft = visual.ImageStim(win=win, name='faceLeft',
    image='images/FF-mock_left.jpg', mask=None,
    ori=0, pos=(x2left, y2), size=stimSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
faceRight = visual.ImageStim(win=win, name='faceRight',
    image='images/FF-mock_right.jpg', mask=None,
    ori=0, pos=(x2right, y2), size=stimSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
shapeTop = visual.ImageStim(win=win, name='shapeTop',
    image='images/oval-horizontal.bmp', mask=None,
    ori=0, pos=(x1, y1), size=stimSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
shapeLeft = visual.ImageStim(win=win, name='shapeLeft',
    image='images/oval-horizontal.bmp', mask=None,
    ori=0, pos=(x1left, y2), size=stimSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
shapeRight = visual.ImageStim(win=win, name='shapeRight',
    image='images/circle.bmp', mask=None,
    ori=0, pos=(x1right, y2), size=stimSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)



# Initialize components for Routine "waitingScanner"
waitingScannerClock = core.Clock()
waitScannerText = visual.TextStim(win=win, ori=0, name='waitScannerText',
    text='Get ready!',    font='Arial',
    pos=[0, 0], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
import datetime
fmriClock = core.Clock()
trigger = 'usb'
#trigger = 'parallel'
if trigger == 'parallel':
    from psychopy.contrib import parallel as winioport
    #from psychopy import parallel
elif trigger == 'usb':
    from psychopy.hardware.emulator import launchScan
    #
    # settings for launchScan:
    MR_settings = { 
        'TR': 2.000, # duration (sec) per volume
        'volumes': 210, # number of whole-brain 3D volumes / frames
        'sync': '5', # character to use as the sync timing event; assumed to come at start of a volume
        'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
        }



# Initialize components for Routine "countdown"
countdownClock = core.Clock()

countdownText = visual.TextStim(win=win, ori=0, name='countdownText',
    text='default text',    font='Arial',
    pos=[0, 0], height=titleLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "cue"
cueClock = core.Clock()
msg=''
matchText = visual.TextStim(win=win, ori=0, name='matchText',
    text='Match',    font='Arial',
    pos=[0, 2], height=titleLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
cueText = visual.TextStim(win=win, ori=0, name='cueText',
    text='default text',    font='Arial',
    pos=[0, -2], height=titleLetterSize, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)


# Initialize components for Routine "trial"
trialClock = core.Clock()
topImage = visual.ImageStim(win=win, name='topImage',
    image='sin', mask=None,
    ori=0, pos=trialTopPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
leftImage = visual.ImageStim(win=win, name='leftImage',
    image='sin', mask=None,
    ori=0, pos=trialLeftPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
rightImage = visual.ImageStim(win=win, name='rightImage',
    image='sin', mask=None,
    ori=0, pos=trialRightPos, size=imageSize,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
botLeftText = visual.TextStim(win=win, ori=0, name='botLeftText',
    text=None,    font='Arial',
    pos=[-9,-9], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)
botRightText = visual.TextStim(win=win, ori=0, name='botRightText',
    text=None,    font='Arial',
    pos=[9,-9], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
pointerText = visual.TextStim(win=win, ori=0, name='pointerText',
    text=None,    font='Arial',
    pos=[-9,-10.5], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
middleText = visual.TextStim(win=win, ori=0, name='middleText',
    text=None,    font='Arial',
    pos=[9,-10.5], height=textLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0)

if mode == 'practice':
    total_trials = 12
else:
    total_trials = 36

import pandas as pd

# Specify columns explicitly for correct order 
COLUMNS = [
    'trialNum',
    'trialCondition',
    'countdownStartTime', 'countdownLabel',
    'cueStartTime', 'cueEndTime',
    'trialStartTime', 'trialEndTime',
    'fixStartTime', 'fixEndTime',
    'runEndTime',
    'stimLeft', 'stimTop', 'stimRight', 'corrAns',
    'condFile', 'trialResp.keys', 'trialResp.rt',
    'resp', 'msg', 'corrRespMsg', 'corrRespCode', 
    'countConsecutive',
] + expInfo.keys()

def updateRunLog(entries):
    df = pd.DataFrame(entries)
    df['run'] = runNum  # 1-based index for "run"

    # Filter rows for this run and selected columns
    run_df = df.filter(COLUMNS)
    if 'runs.thisN' in df.columns:
        run_df = run_df.loc[df['runs.thisN'] == runs.thisN]
    if 'trialNum' in run_df.columns:
        run_df.dropna(axis='index', subset=['trialNum'], inplace=True)
        run_df['trialNum'] = run_df['trialNum'].astype(int)

    runOutfile = '%s_wide.csv' % filename
    run_df.to_csv(runOutfile, encoding='utf-8',
                    header=True, index=False, )

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
cross = visual.TextStim(win=win, ori=0, name='cross',
    text='+',    font='Arial',
    pos=[0, 0], height=fixLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "lastFixation"
lastFixationClock = core.Clock()
lastFixationText = visual.TextStim(win=win, ori=0, name='lastFixationText',
    text='+',    font='Arial',
    pos=[0, 0], height=fixLetterSize, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "endRun"
endRunClock = core.Clock()



# Initialize components for Routine "end"
endClock = core.Clock()
import pandas as pd
endText = visual.TextStim(win=win, ori=0, name='endText',
    text='You finished this game!',    font='Arial',
    pos=[0, 0], height=textLetterSize, wrapWidth=30,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

introResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
introResp.status = NOT_STARTED
if mode == 'practice':
    raVerbalText.text = '"Welcome to the Matching Game!"'
    raText.text = 'Press <space> to continue.'
else:
    raVerbalText.text = '"Welcome back to the Matching Game!"'
    raText.text = 'Press <space> to continue.'

raVerbalText.draw()
raText.draw()
raWinRecorder.keyframe()
raWin.flip()



movieClock.reset()
# keep track of which components have finished
introComponents = []
introComponents.append(introText)
introComponents.append(introResp)
introComponents.append(introText2)
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *introText* updates
    if t >= 0.0 and introText.status == NOT_STARTED:
        # keep track of start time/frame for later
        introText.tStart = t  # underestimates by a little under one frame
        introText.frameNStart = frameN  # exact frame index
        introText.setAutoDraw(True)
    
    # *introResp* updates
    if t >= 0.0 and introResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        introResp.tStart = t  # underestimates by a little under one frame
        introResp.frameNStart = frameN  # exact frame index
        introResp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(introResp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if introResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            introResp.keys = theseKeys[-1]  # just the last key pressed
            introResp.rt = introResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    
    # *introText2* updates
    if t >= 0.0 and introText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        introText2.tStart = t  # underestimates by a little under one frame
        introText2.frameNStart = frameN  # exact frame index
        introText2.setAutoDraw(True)
    
    if frameN == 0:
        winRecorder.keyframe()
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if introResp.keys in ['', [], None]:  # No response was made
   introResp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('introResp.keys',introResp.keys)
if introResp.keys != None:  # we had a response
    thisExp.addData('introResp.rt', introResp.rt)
thisExp.nextEntry()




# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pracDirections = data.TrialHandler(nReps=mode == 'practice', method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pracDirections')
thisExp.addLoop(pracDirections)  # add the loop to the experiment
thisPracDirection = pracDirections.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPracDirection.rgb)
if thisPracDirection != None:
    for paramName in thisPracDirection.keys():
        exec(paramName + '= thisPracDirection.' + paramName)

for thisPracDirection in pracDirections:
    currentLoop = pracDirections
    # abbreviate parameter names if possible (e.g. rgb = thisPracDirection.rgb)
    if thisPracDirection != None:
        for paramName in thisPracDirection.keys():
            exec(paramName + '= thisPracDirection.' + paramName)
    
    #------Prepare to start Routine "pracInstr1"-------
    t = 0
    pracInstr1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    pracInstr1Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    pracInstr1Resp.status = NOT_STARTED
    raVerbalText.text = '"In this game, you will see groups of three faces or three shapes, arranged in a triangle, as shown here."'
    raText.text = 'Press <space> to continue.'
    
    raText.draw()
    raVerbalText.draw()
    raWin.flip()
    for prompt in buttonPrompts:
        prompt.autoDraw = True
    # keep track of which components have finished
    pracInstr1Components = []
    pracInstr1Components.append(top_image)
    pracInstr1Components.append(left_image)
    pracInstr1Components.append(right_image)
    pracInstr1Components.append(pracInstr1Resp)
    for thisComponent in pracInstr1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *top_image* updates
        if t >= 0.0 and top_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            top_image.tStart = t  # underestimates by a little under one frame
            top_image.frameNStart = frameN  # exact frame index
            top_image.setAutoDraw(True)
        
        # *left_image* updates
        if t >= 0.0 and left_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_image.tStart = t  # underestimates by a little under one frame
            left_image.frameNStart = frameN  # exact frame index
            left_image.setAutoDraw(True)
        
        # *right_image* updates
        if t >= 0.0 and right_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_image.tStart = t  # underestimates by a little under one frame
            right_image.frameNStart = frameN  # exact frame index
            right_image.setAutoDraw(True)
        
        # *pracInstr1Resp* updates
        if t >= 0.0 and pracInstr1Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr1Resp.tStart = t  # underestimates by a little under one frame
            pracInstr1Resp.frameNStart = frameN  # exact frame index
            pracInstr1Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(pracInstr1Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if pracInstr1Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                pracInstr1Resp.keys = theseKeys[-1]  # just the last key pressed
                pracInstr1Resp.rt = pracInstr1Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr1"-------
    for thisComponent in pracInstr1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracInstr1Resp.keys in ['', [], None]:  # No response was made
       pracInstr1Resp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('pracInstr1Resp.keys',pracInstr1Resp.keys)
    if pracInstr1Resp.keys != None:  # we had a response
        pracDirections.addData('pracInstr1Resp.rt', pracInstr1Resp.rt)
    
    
    # the Routine "pracInstr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pracInstr2"-------
    t = 0
    pracInstr2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    pracInstr2Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    pracInstr2Resp.status = NOT_STARTED
    raVerbalText.text = '"If the bottom left picture matches the top picture, like in this example, you should push the button under your POINTER finger. Go ahead and press the pointer finger button now."'
    raText.text = '\n\nWait for the participant to press the pointer finger button to continue.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    # keep track of which components have finished
    pracInstr2Components = []
    pracInstr2Components.append(top)
    pracInstr2Components.append(left)
    pracInstr2Components.append(right)
    pracInstr2Components.append(pointerFinger)
    pracInstr2Components.append(pracInstr2Resp)
    for thisComponent in pracInstr2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *top* updates
        if t >= 0.0 and top.status == NOT_STARTED:
            # keep track of start time/frame for later
            top.tStart = t  # underestimates by a little under one frame
            top.frameNStart = frameN  # exact frame index
            top.setAutoDraw(True)
        
        # *left* updates
        if t >= 0.0 and left.status == NOT_STARTED:
            # keep track of start time/frame for later
            left.tStart = t  # underestimates by a little under one frame
            left.frameNStart = frameN  # exact frame index
            left.setAutoDraw(True)
        
        # *right* updates
        if t >= 0.0 and right.status == NOT_STARTED:
            # keep track of start time/frame for later
            right.tStart = t  # underestimates by a little under one frame
            right.frameNStart = frameN  # exact frame index
            right.setAutoDraw(True)
        
        # *pointerFinger* updates
        if t >= 0.0 and pointerFinger.status == NOT_STARTED:
            # keep track of start time/frame for later
            pointerFinger.tStart = t  # underestimates by a little under one frame
            pointerFinger.frameNStart = frameN  # exact frame index
            pointerFinger.setAutoDraw(True)
        
        # *pracInstr2Resp* updates
        if t >= 0.0 and pracInstr2Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr2Resp.tStart = t  # underestimates by a little under one frame
            pracInstr2Resp.frameNStart = frameN  # exact frame index
            pracInstr2Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(pracInstr2Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if pracInstr2Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', 'num_1'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                pracInstr2Resp.keys = theseKeys[-1]  # just the last key pressed
                pracInstr2Resp.rt = pracInstr2Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr2"-------
    for thisComponent in pracInstr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracInstr2Resp.keys in ['', [], None]:  # No response was made
       pracInstr2Resp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('pracInstr2Resp.keys',pracInstr2Resp.keys)
    if pracInstr2Resp.keys != None:  # we had a response
        pracDirections.addData('pracInstr2Resp.rt', pracInstr2Resp.rt)
    
    # the Routine "pracInstr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pracInstr3"-------
    t = 0
    pracInstr3Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    pracInstr3Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    pracInstr3Resp.status = NOT_STARTED
    raVerbalText.text = '"And if the bottom right picture matches the top picture, like in this other example, you should push the button under your MIDDLE finger. Press the middle finger button now."'
    raText.text = '\n\nWait for the participant to press the middle finger button to continue.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    # keep track of which components have finished
    pracInstr3Components = []
    pracInstr3Components.append(top3)
    pracInstr3Components.append(left3)
    pracInstr3Components.append(right3)
    pracInstr3Components.append(middleFinger)
    pracInstr3Components.append(pracInstr3Resp)
    for thisComponent in pracInstr3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr3"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *top3* updates
        if t >= 0.0 and top3.status == NOT_STARTED:
            # keep track of start time/frame for later
            top3.tStart = t  # underestimates by a little under one frame
            top3.frameNStart = frameN  # exact frame index
            top3.setAutoDraw(True)
        
        # *left3* updates
        if t >= 0.0 and left3.status == NOT_STARTED:
            # keep track of start time/frame for later
            left3.tStart = t  # underestimates by a little under one frame
            left3.frameNStart = frameN  # exact frame index
            left3.setAutoDraw(True)
        
        # *right3* updates
        if t >= 0.0 and right3.status == NOT_STARTED:
            # keep track of start time/frame for later
            right3.tStart = t  # underestimates by a little under one frame
            right3.frameNStart = frameN  # exact frame index
            right3.setAutoDraw(True)
        
        # *middleFinger* updates
        if t >= 0.0 and middleFinger.status == NOT_STARTED:
            # keep track of start time/frame for later
            middleFinger.tStart = t  # underestimates by a little under one frame
            middleFinger.frameNStart = frameN  # exact frame index
            middleFinger.setAutoDraw(True)
        
        # *pracInstr3Resp* updates
        if t >= 0.0 and pracInstr3Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr3Resp.tStart = t  # underestimates by a little under one frame
            pracInstr3Resp.frameNStart = frameN  # exact frame index
            pracInstr3Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(pracInstr3Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if pracInstr3Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['2', 'num_2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                pracInstr3Resp.keys = theseKeys[-1]  # just the last key pressed
                pracInstr3Resp.rt = pracInstr3Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr3"-------
    for thisComponent in pracInstr3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracInstr3Resp.keys in ['', [], None]:  # No response was made
       pracInstr3Resp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('pracInstr3Resp.keys',pracInstr3Resp.keys)
    if pracInstr3Resp.keys != None:  # we had a response
        pracDirections.addData('pracInstr3Resp.rt', pracInstr3Resp.rt)
    
    # the Routine "pracInstr3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pracInstr4"-------
    t = 0
    pracInstr4Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    exTrialResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    exTrialResp.status = NOT_STARTED
    raVerbalText.text = '"While you play this game, we will remind you what buttons to press at the bottom of the screen, as you can see here."'
    raText.text = 'Press <space> to continue.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    # keep track of which components have finished
    pracInstr4Components = []
    pracInstr4Components.append(exTopImage)
    pracInstr4Components.append(exLeftImage)
    pracInstr4Components.append(exRightImage)
    pracInstr4Components.append(exTrialResp)
    for thisComponent in pracInstr4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr4"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *exTopImage* updates
        if t >= 0.0 and exTopImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            exTopImage.tStart = t  # underestimates by a little under one frame
            exTopImage.frameNStart = frameN  # exact frame index
            exTopImage.setAutoDraw(True)
        if exTopImage.status == STARTED:  # only update if being drawn
            exTopImage.setImage('images/FA-mock_top.jpg', log=False)
        
        # *exLeftImage* updates
        if t >= 0.0 and exLeftImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            exLeftImage.tStart = t  # underestimates by a little under one frame
            exLeftImage.frameNStart = frameN  # exact frame index
            exLeftImage.setAutoDraw(True)
        if exLeftImage.status == STARTED:  # only update if being drawn
            exLeftImage.setImage('images/FA-mock_left.jpg', log=False)
        
        # *exRightImage* updates
        if t >= 0.0 and exRightImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            exRightImage.tStart = t  # underestimates by a little under one frame
            exRightImage.frameNStart = frameN  # exact frame index
            exRightImage.setAutoDraw(True)
        if exRightImage.status == STARTED:  # only update if being drawn
            exRightImage.setImage('images/FA-mock_right.jpg', log=False)
        
        # *exTrialResp* updates
        if t >= 0 and exTrialResp.status == NOT_STARTED:
            # keep track of start time/frame for later
            exTrialResp.tStart = t  # underestimates by a little under one frame
            exTrialResp.frameNStart = frameN  # exact frame index
            exTrialResp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(exTrialResp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if exTrialResp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                exTrialResp.keys = theseKeys[-1]  # just the last key pressed
                exTrialResp.rt = exTrialResp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        for prompt in buttonPrompts:
            prompt.draw()
        
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr4"-------
    for thisComponent in pracInstr4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if exTrialResp.keys in ['', [], None]:  # No response was made
       exTrialResp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('exTrialResp.keys',exTrialResp.keys)
    if exTrialResp.keys != None:  # we had a response
        pracDirections.addData('exTrialResp.rt', exTrialResp.rt)
    
    # the Routine "pracInstr4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pracInstr5"-------
    t = 0
    pracInstr5Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    pracInstr5Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    pracInstr5Resp.status = NOT_STARTED
    raVerbalText.text = '"Let\'s practice a few trials together."'
    raText.text = 'Press <space> to continue.'
    
    raVerbalText.draw()
    raText.draw()
    raWin.flip()
    
    totalButtonTrack = []
    countConsecutive=1
    
    correct_resp = 0
    noResp = 0
    incorrect_resp = 0
    
    corrRespPerc = 0
    incorrRespPerc = 0
    noRespPerc = 0
    
    fiveBackCorrCount = 0
    fiveBacknoRespCount = 0
    fiveBackIncorrCount = 0
    
    totalCountList=[]
    
    
    # keep track of which components have finished
    pracInstr5Components = []
    pracInstr5Components.append(pracInstr5Text)
    pracInstr5Components.append(pracInstr5Resp)
    for thisComponent in pracInstr5Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr5"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr5Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracInstr5Text* updates
        if t >= 0.0 and pracInstr5Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr5Text.tStart = t  # underestimates by a little under one frame
            pracInstr5Text.frameNStart = frameN  # exact frame index
            pracInstr5Text.setAutoDraw(True)
        
        # *pracInstr5Resp* updates
        if t >= 0.0 and pracInstr5Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr5Resp.tStart = t  # underestimates by a little under one frame
            pracInstr5Resp.frameNStart = frameN  # exact frame index
            pracInstr5Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(pracInstr5Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if pracInstr5Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                pracInstr5Resp.keys = theseKeys[-1]  # just the last key pressed
                pracInstr5Resp.rt = pracInstr5Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr5"-------
    for thisComponent in pracInstr5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracInstr5Resp.keys in ['', [], None]:  # No response was made
       pracInstr5Resp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('pracInstr5Resp.keys',pracInstr5Resp.keys)
    if pracInstr5Resp.keys != None:  # we had a response
        pracDirections.addData('pracInstr5Resp.rt', pracInstr5Resp.rt)
    for prompt in buttonPrompts:
        prompt.autoDraw = False
    
    if frameN == 0:
        winRecorder.keyframe()
    # the Routine "pracInstr5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    exampleTrials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions/examples.csv'),
        seed=None, name='exampleTrials')
    thisExp.addLoop(exampleTrials)  # add the loop to the experiment
    thisExampleTrial = exampleTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisExampleTrial.rgb)
    if thisExampleTrial != None:
        for paramName in thisExampleTrial.keys():
            exec(paramName + '= thisExampleTrial.' + paramName)
    
    for thisExampleTrial in exampleTrials:
        currentLoop = exampleTrials
        # abbreviate parameter names if possible (e.g. rgb = thisExampleTrial.rgb)
        if thisExampleTrial != None:
            for paramName in thisExampleTrial.keys():
                exec(paramName + '= thisExampleTrial.' + paramName)
        
        #------Prepare to start Routine "exampleTrial"-------
        t = 0
        exampleTrialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        topImageExample.setImage(os.path.join('images', stimTop))
        leftImageExample.setImage(os.path.join('images', stimLeft))
        rightImageExample.setImage(os.path.join('images', stimRight))
        exampleTrialResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        exampleTrialResp.status = NOT_STARTED
        number_trials = exampleTrials.thisN + 1
        
        raText.pos= [0,0]
        
        raText.text = 'Watch the participant\'s performance and give feedback on the example trials as appropriate. \n\nMake sure the participant understands the task.'
        raText.draw()
        raWinRecorder.keyframe()
        raWin.flip()
        # keep track of which components have finished
        exampleTrialComponents = []
        exampleTrialComponents.append(topImageExample)
        exampleTrialComponents.append(leftImageExample)
        exampleTrialComponents.append(rightImageExample)
        exampleTrialComponents.append(botLeftTextExample)
        exampleTrialComponents.append(botRightTextExample)
        exampleTrialComponents.append(pointerTextExample)
        exampleTrialComponents.append(middleTextExample)
        exampleTrialComponents.append(exampleTrialResp)
        for thisComponent in exampleTrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "exampleTrial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = exampleTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *topImageExample* updates
            if t >= 0.0 and topImageExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                topImageExample.tStart = t  # underestimates by a little under one frame
                topImageExample.frameNStart = frameN  # exact frame index
                topImageExample.setAutoDraw(True)
            if topImageExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                topImageExample.setAutoDraw(False)
            
            # *leftImageExample* updates
            if t >= 0.0 and leftImageExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftImageExample.tStart = t  # underestimates by a little under one frame
                leftImageExample.frameNStart = frameN  # exact frame index
                leftImageExample.setAutoDraw(True)
            if leftImageExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                leftImageExample.setAutoDraw(False)
            
            # *rightImageExample* updates
            if t >= 0.0 and rightImageExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightImageExample.tStart = t  # underestimates by a little under one frame
                rightImageExample.frameNStart = frameN  # exact frame index
                rightImageExample.setAutoDraw(True)
            if rightImageExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                rightImageExample.setAutoDraw(False)
            
            # *botLeftTextExample* updates
            if t >= 0.0 and botLeftTextExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                botLeftTextExample.tStart = t  # underestimates by a little under one frame
                botLeftTextExample.frameNStart = frameN  # exact frame index
                botLeftTextExample.setAutoDraw(True)
            if botLeftTextExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                botLeftTextExample.setAutoDraw(False)
            
            # *botRightTextExample* updates
            if t >= 0.0 and botRightTextExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                botRightTextExample.tStart = t  # underestimates by a little under one frame
                botRightTextExample.frameNStart = frameN  # exact frame index
                botRightTextExample.setAutoDraw(True)
            if botRightTextExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                botRightTextExample.setAutoDraw(False)
            
            # *pointerTextExample* updates
            if t >= 0.0 and pointerTextExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                pointerTextExample.tStart = t  # underestimates by a little under one frame
                pointerTextExample.frameNStart = frameN  # exact frame index
                pointerTextExample.setAutoDraw(True)
            if pointerTextExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                pointerTextExample.setAutoDraw(False)
            
            # *middleTextExample* updates
            if t >= 0.0 and middleTextExample.status == NOT_STARTED:
                # keep track of start time/frame for later
                middleTextExample.tStart = t  # underestimates by a little under one frame
                middleTextExample.frameNStart = frameN  # exact frame index
                middleTextExample.setAutoDraw(True)
            if middleTextExample.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                middleTextExample.setAutoDraw(False)
            
            # *exampleTrialResp* updates
            if t >= 0 and exampleTrialResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                exampleTrialResp.tStart = t  # underestimates by a little under one frame
                exampleTrialResp.frameNStart = frameN  # exact frame index
                exampleTrialResp.status = STARTED
                # AllowedKeys looks like a variable named `allowed_keys`
                if not 'allowed_keys' in locals():
                    logging.error('AllowedKeys variable `allowed_keys` is not defined.')
                    core.quit()
                if not type(allowed_keys) in [list, tuple, np.ndarray]:
                    if not isinstance(allowed_keys, basestring):
                        logging.error('AllowedKeys variable `allowed_keys` is not string- or list-like.')
                        core.quit()
                    elif not ',' in allowed_keys: allowed_keys = (allowed_keys,)
                    else:  allowed_keys = eval(allowed_keys)
                # keyboard checking is just starting
                win.callOnFlip(exampleTrialResp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if exampleTrialResp.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                exampleTrialResp.status = STOPPED
            if exampleTrialResp.status == STARTED:
                theseKeys = event.getKeys(keyList=list(allowed_keys))
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    exampleTrialResp.keys.extend(theseKeys)  # storing all keys
                    exampleTrialResp.rt.append(exampleTrialResp.clock.getTime())
            for prompt in buttonPrompts:
                prompt.draw()
            
            if frameN == 0:
                winRecorder.keyframe()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in exampleTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "exampleTrial"-------
        for thisComponent in exampleTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if exampleTrialResp.keys in ['', [], None]:  # No response was made
           exampleTrialResp.keys=None
        # store data for exampleTrials (TrialHandler)
        exampleTrials.addData('exampleTrialResp.keys',exampleTrialResp.keys)
        if exampleTrialResp.keys != None:  # we had a response
            exampleTrials.addData('exampleTrialResp.rt', exampleTrialResp.rt)
        resp=None
        respLast=None
         
        if exampleTrialResp.keys: #coding first response made by participant
            if exampleTrialResp.keys[0] in config['keys']['left']:
                resp = 'left'
            elif exampleTrialResp.keys[0] in config['keys']['right']:
                resp = 'right'
            elif not exampleTrialResp.keys:
                resp = None
        
        if exampleTrialResp.keys: #coding last response made by participant
            if exampleTrialResp.keys[-1] in config['keys']['left']:
                respLast = 'left'
            elif exampleTrialResp.keys[-1] in config['keys']['right']:
                respLast = 'right'
        
        if resp==str('left'):
            totalButtonTrack.append(1)
        elif resp==str('right'):
            totalButtonTrack.append(2)
        else: #no response
            totalButtonTrack.append(0)
        
        
        if (str(corrAns)==str('left') and resp == str('left')) or (str(corrAns)==str('right') and resp == 'right'):
            msg="CORRECT!"
            corrRespMsg="correct"
            corrRespCode = 1
            respTrack = 1
            correct_resp+=1
            corrRespPerc= (correct_resp)/(number_trials)
            noRespPerc = (noResp)/(number_trials)
            incorrRespPerc= (incorrect_resp)/(number_trials)
            totalCountList.append(respTrack)
        elif resp==None:
            msg="TOO SLOW"
            corrRespMsg="miss"
            corrRespCode = 0
            respTrack = 2
            noResp+=1
            corrRespPerc= (correct_resp)/(number_trials)
            noRespPerc = (noResp)/(number_trials)
            incorrRespPerc= (incorrect_resp)/(number_trials)
            totalCountList.append(respTrack)
        elif (str(corrAns)==str('left') and resp != str('left')) or (str(corrAns)==str('right') and resp != 'right'):
            msg="INCORRECT"
            corrRespMsg="incorrect"
            corrRespCode = 0
            respTrack = 0
            incorrect_resp+=1
            corrRespPerc= (correct_resp)/(number_trials)
            noRespPerc = (noResp)/(number_trials)
            incorrRespPerc= (incorrect_resp)/(number_trials)
            totalCountList.append(respTrack)
        
        
        if number_trials >= 5:
            fiveBackCorrCount = 0
            fiveBacknoRespCount = 0
            fiveBackIncorrCount = 0
            for i in range(-1, -6,-1):
                if totalCountList[i] == 1:
                    fiveBackCorrCount+=1
                elif totalCountList[i] == 2:
                    fiveBacknoRespCount+=1
                elif totalCountList[i] == 0:
                    fiveBackIncorrCount+=1
        
        #countConsecutive=1
        if number_trials >=2:
            if totalButtonTrack[-1]==totalButtonTrack[-2]:
                countConsecutive+=1
            elif totalButtonTrack[-1]!=totalButtonTrack[-2]:
                countConsecutive=1
        
        
        currentLoop.addData('number_trials', number_trials)
        currentLoop.addData('resp', resp)
        currentLoop.addData('msg', msg)
        currentLoop.addData('corrRespMsg', corrRespMsg)
        currentLoop.addData('corrRespCode', corrRespCode)
        currentLoop.addData('respTrack', respTrack)
        currentLoop.addData('correct_resp', correct_resp)
        currentLoop.addData('incorrect_resp', incorrect_resp)
        currentLoop.addData('noResp', noResp)
        currentLoop.addData('corrRespPerc', corrRespPerc)
        currentLoop.addData('incorrRespPerc', incorrRespPerc)
        currentLoop.addData('noRespPerc', noRespPerc)
        
        currentLoop.addData('totalCountList', totalCountList)
        currentLoop.addData('fiveBackCorrCount', fiveBackCorrCount)
        currentLoop.addData('fiveBacknoRespCount', fiveBacknoRespCount)
        currentLoop.addData('fiveBackIncorrCount', fiveBackIncorrCount)
        
        currentLoop.addData('totalButtonTrack', totalButtonTrack)
        currentLoop.addData('countConsecutive', countConsecutive)
        
        
        #------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        fixationComponents = []
        fixationComponents.append(cross)
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "fixation"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross* updates
            if t >= 0.0 and cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                cross.tStart = t  # underestimates by a little under one frame
                cross.frameNStart = frameN  # exact frame index
                cross.setAutoDraw(True)
            if cross.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                cross.setAutoDraw(False)
            if frameN == 0:
                fixStartTime = fmriClock.getTime()
                winRecorder.keyframe()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        fixEndTime = fmriClock.getTime()
        
        currentLoop.addData('fixStartTime', fixStartTime)
        currentLoop.addData('fixEndTime', fixEndTime)
        
        entries = thisExp.entries
        
        if currentLoop.name != 'exampleTrials':
            updateRunLog(entries)
        
        #------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        feedbackComponents = []
        feedbackComponents.append(feedbackText)
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackText* updates
            if t >= 0.0 and feedbackText.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackText.tStart = t  # underestimates by a little under one frame
                feedbackText.frameNStart = frameN  # exact frame index
                feedbackText.setAutoDraw(True)
            if feedbackText.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                feedbackText.setAutoDraw(False)
            if feedbackText.status == STARTED:  # only update if being drawn
                feedbackText.setText(msg, log=False)
            if frameN == 0:
                winRecorder.keyframe()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'exampleTrials'
    
    
    #------Prepare to start Routine "pracInstr6"-------
    t = 0
    pracInstr6Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    pracInstr6Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    pracInstr6Resp.status = NOT_STARTED
    raText.pos= [0,-3]
    
    raVerbalText.text = '"Do you have any questions?\n\nNow you will complete a short practice that will look exactly like the game you will play in the scanner.\n\nIn this practice, we will not tell you if you are right or wrong. Just try your best to follow the instructions and play the game."'
    raText.text = '\n\n\n\n\nPress <space> to continue.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    # keep track of which components have finished
    pracInstr6Components = []
    pracInstr6Components.append(pracInstr6Text)
    pracInstr6Components.append(pracInstr6Resp)
    for thisComponent in pracInstr6Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr6"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr6Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracInstr6Text* updates
        if t >= 0.0 and pracInstr6Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr6Text.tStart = t  # underestimates by a little under one frame
            pracInstr6Text.frameNStart = frameN  # exact frame index
            pracInstr6Text.setAutoDraw(True)
        
        # *pracInstr6Resp* updates
        if t >= 0.0 and pracInstr6Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr6Resp.tStart = t  # underestimates by a little under one frame
            pracInstr6Resp.frameNStart = frameN  # exact frame index
            pracInstr6Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(pracInstr6Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if pracInstr6Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                pracInstr6Resp.keys = theseKeys[-1]  # just the last key pressed
                pracInstr6Resp.rt = pracInstr6Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr6"-------
    for thisComponent in pracInstr6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracInstr6Resp.keys in ['', [], None]:  # No response was made
       pracInstr6Resp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('pracInstr6Resp.keys',pracInstr6Resp.keys)
    if pracInstr6Resp.keys != None:  # we had a response
        pracDirections.addData('pracInstr6Resp.rt', pracInstr6Resp.rt)
    
    # the Routine "pracInstr6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "pracInstr7"-------
    t = 0
    pracInstr7Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    pracInstr7Resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    pracInstr7Resp.status = NOT_STARTED
    raVerbalText.text = '"Are you ready to begin the practice?"'
    raText.text = 'Press <space> to continue.\n\nWatch the participant\'s performance and give feedback as appropriate. Make sure the participant understands the task.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    
    # keep track of which components have finished
    pracInstr7Components = []
    pracInstr7Components.append(pracInstr7Text)
    pracInstr7Components.append(pracInstr7Resp)
    for thisComponent in pracInstr7Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pracInstr7"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pracInstr7Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracInstr7Text* updates
        if t >= 0.0 and pracInstr7Text.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr7Text.tStart = t  # underestimates by a little under one frame
            pracInstr7Text.frameNStart = frameN  # exact frame index
            pracInstr7Text.setAutoDraw(True)
        
        # *pracInstr7Resp* updates
        if t >= 0.0 and pracInstr7Resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            pracInstr7Resp.tStart = t  # underestimates by a little under one frame
            pracInstr7Resp.frameNStart = frameN  # exact frame index
            pracInstr7Resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(pracInstr7Resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if pracInstr7Resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                pracInstr7Resp.keys = theseKeys[-1]  # just the last key pressed
                pracInstr7Resp.rt = pracInstr7Resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracInstr7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pracInstr7"-------
    for thisComponent in pracInstr7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracInstr7Resp.keys in ['', [], None]:  # No response was made
       pracInstr7Resp.keys=None
    # store data for pracDirections (TrialHandler)
    pracDirections.addData('pracInstr7Resp.keys',pracInstr7Resp.keys)
    if pracInstr7Resp.keys != None:  # we had a response
        pracDirections.addData('pracInstr7Resp.rt', pracInstr7Resp.rt)
    raText.text = ''
    raText.draw()
    raWin.flip()
    # the Routine "pracInstr7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed mode == 'practice' repeats of 'pracDirections'


# set up handler to look after randomisation of conditions etc
scanDirections = data.TrialHandler(nReps=mode != 'practice', method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='scanDirections')
thisExp.addLoop(scanDirections)  # add the loop to the experiment
thisScanDirection = scanDirections.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisScanDirection.rgb)
if thisScanDirection != None:
    for paramName in thisScanDirection.keys():
        exec(paramName + '= thisScanDirection.' + paramName)

for thisScanDirection in scanDirections:
    currentLoop = scanDirections
    # abbreviate parameter names if possible (e.g. rgb = thisScanDirection.rgb)
    if thisScanDirection != None:
        for paramName in thisScanDirection.keys():
            exec(paramName + '= thisScanDirection.' + paramName)
    
    #------Prepare to start Routine "scanInstr1"-------
    t = 0
    scanInstr1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    
    
    raText.pos=[0, -6]
    raVerbalText.text = '"Remember, in this game, your job is to indicate which face or shape on the bottom row matches the face or shape on the top row. \n\nIf the left picture matches the top picture, press the button under your POINTER finger. If the right picture matches the top picture, press the button under your MIDDLE finger."'
    raText.text = 'Press <space> to continue.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    
    npresses = 0
    record_exp_win = True
    # keep track of which components have finished
    scanInstr1Components = []
    scanInstr1Components.append(faceTop)
    scanInstr1Components.append(faceLeft)
    scanInstr1Components.append(faceRight)
    scanInstr1Components.append(shapeTop)
    scanInstr1Components.append(shapeLeft)
    scanInstr1Components.append(shapeRight)
    for thisComponent in scanInstr1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "scanInstr1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = scanInstr1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *faceTop* updates
        if t >= 0.0 and faceTop.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceTop.tStart = t  # underestimates by a little under one frame
            faceTop.frameNStart = frameN  # exact frame index
            faceTop.setAutoDraw(True)
        
        # *faceLeft* updates
        if t >= 0.0 and faceLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceLeft.tStart = t  # underestimates by a little under one frame
            faceLeft.frameNStart = frameN  # exact frame index
            faceLeft.setAutoDraw(True)
        
        # *faceRight* updates
        if t >= 0.0 and faceRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceRight.tStart = t  # underestimates by a little under one frame
            faceRight.frameNStart = frameN  # exact frame index
            faceRight.setAutoDraw(True)
        
        # *shapeTop* updates
        if t >= 0.0 and shapeTop.status == NOT_STARTED:
            # keep track of start time/frame for later
            shapeTop.tStart = t  # underestimates by a little under one frame
            shapeTop.frameNStart = frameN  # exact frame index
            shapeTop.setAutoDraw(True)
        
        # *shapeLeft* updates
        if t >= 0.0 and shapeLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            shapeLeft.tStart = t  # underestimates by a little under one frame
            shapeLeft.frameNStart = frameN  # exact frame index
            shapeLeft.setAutoDraw(True)
        
        # *shapeRight* updates
        if t >= 0.0 and shapeRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            shapeRight.tStart = t  # underestimates by a little under one frame
            shapeRight.frameNStart = frameN  # exact frame index
            shapeRight.setAutoDraw(True)
        for prompt in buttonPrompts:
            prompt.draw()
        if record_exp_win:
            winRecorder.keyframe()
            record_exp_win = False
        
        if event.getKeys(keyList = ['space']):
            npresses += 1
            record_exp_win = True
            if npresses == 1:
                raVerbalText.text = '"Do you have any questions? Are you ready to play the game and be super still in this scan?"'
                raText.text = 'Press <space> to continue.'
                raVerbalText.draw()
                raText.draw()
                raWinRecorder.keyframe()
                raWin.flip()
            else:
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scanInstr1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "scanInstr1"-------
    for thisComponent in scanInstr1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    raText.text =''
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    
    
    # the Routine "scanInstr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed mode != 'practice' repeats of 'scanDirections'


# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
    #------Prepare to start Routine "waitingScanner"-------
    t = 0
    waitingScannerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    
    runNum = session + runs.thisN
    
    events = []
    
    raText.pos=[0, 0]
    
    raVerbalText.text = ''
    raText.text = 'Start the scan.'
    
    raVerbalText.draw()
    raText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    
    # keep track of which components have finished
    waitingScannerComponents = []
    waitingScannerComponents.append(waitScannerText)
    for thisComponent in waitingScannerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "waitingScanner"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = waitingScannerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waitScannerText* updates
        if t >= 0.0 and waitScannerText.status == NOT_STARTED:
            # keep track of start time/frame for later
            waitScannerText.tStart = t  # underestimates by a little under one frame
            waitScannerText.frameNStart = frameN  # exact frame index
            waitScannerText.setAutoDraw(True)
        if expInfo['mriMode'] != 'Off':
            winRecorder.keyframe()
            if trigger == 'usb':
                vol = launchScan(win, MR_settings, 
                      globalClock=fmriClock, 
                      mode=expInfo['mriMode'],
                      wait_msg = '')
        
            elif trigger == 'parallel':
                address = 0x378
                #parallel.setPortAddress(0x378)
                wait_msg = "Get ready!"
                pinStatus = winioport.inp(address)
                waitMsgStim = visual.TextStim(win, color='white', text=wait_msg)
                waitMsgStim.draw()
                win.flip()
                while True:
                    if pinStatus != winioport.inp(address):
                       break
                       # start exp when pin values change
                fmriClock.reset()
                logging.exp('parallel trigger: start of scan')
                win.flip()  # blank the screen on first sync pulse received
        else:
            fmriClock.reset()
        
        triggerWallTime = datetime.datetime.today()
        expInfo['triggerWallTime'] = triggerWallTime.strftime('%a %b %d %H:%M:%S %Y')
        expInfo['triggerGlobalTime'] = globalClock.getTime()
        continueRoutine = False
        
        filename = _thisDir + os.sep + u'data/' + '_'.join([expName, expInfo['sessionID'], 'run%s'%runNum, triggerWallTime.strftime('%Y-%m-%d_%H%M%S')])
        continueRoutine = False
        
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitingScannerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "waitingScanner"-------
    for thisComponent in waitingScannerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    raVerbalText.text = ''
    raText.text = ''
    raText.pos = [0, 0]
    raText.draw()
    raVerbalText.draw()
    raWinRecorder.keyframe()
    raWin.flip()
    # the Routine "waitingScanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    countdowns = data.TrialHandler(nReps=4, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='countdowns')
    thisExp.addLoop(countdowns)  # add the loop to the experiment
    thisCountdown = countdowns.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisCountdown.rgb)
    if thisCountdown != None:
        for paramName in thisCountdown.keys():
            exec(paramName + '= thisCountdown.' + paramName)
    
    for thisCountdown in countdowns:
        currentLoop = countdowns
        # abbreviate parameter names if possible (e.g. rgb = thisCountdown.rgb)
        if thisCountdown != None:
            for paramName in thisCountdown.keys():
                exec(paramName + '= thisCountdown.' + paramName)
        
        #------Prepare to start Routine "countdown"-------
        t = 0
        countdownClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        countdownMsg = currentLoop.nRemaining + 1
        currentLoop.addData('countdownLabel', countdownMsg)
        
        totalButtonTrack = []
        countConsecutive=1
        
        correct_resp = 0
        noResp = 0
        incorrect_resp = 0
        
        corrRespPerc = 0
        incorrRespPerc = 0
        noRespPerc = 0
        
        fiveBackCorrCount = 0
        fiveBacknoRespCount = 0
        fiveBackIncorrCount = 0
        
        totalCountList=[]
        countdownText.setText(countdownMsg)
        
        # keep track of which components have finished
        countdownComponents = []
        countdownComponents.append(countdownText)
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "countdown"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = countdownClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Countdown Timing
            if frameN == 0:
                countdownTime = fmriClock.getTime()
                currentLoop.addData('countdownStartTime', countdownTime)
            
            
            # *countdownText* updates
            if t >= 0.0 and countdownText.status == NOT_STARTED:
                # keep track of start time/frame for later
                countdownText.tStart = t  # underestimates by a little under one frame
                countdownText.frameNStart = frameN  # exact frame index
                countdownText.setAutoDraw(True)
            if countdownText.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                countdownText.setAutoDraw(False)
            if frameN == 1:
                winRecorder.keyframe()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in countdownComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "countdown"-------
        for thisComponent in countdownComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        currentLoop.addData('countdownStartTime', countdownTime)
        currentLoop.addData('countdownLabel', countdownMsg)
        currentLoop.addData('trialNum', 0)
        
        
        thisExp.nextEntry()
        
    # completed 4 repeats of 'countdowns'
    
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=nBlocks, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock.keys():
                exec(paramName + '= thisBlock.' + paramName)
        
        #------Prepare to start Routine "cue"-------
        t = 0
        cueClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # Start the clock
        timer = core.Clock()
        
        if blocks.thisN in (0,2,4):
            msg= 'Shapes'
        
        elif blocks.thisN in (1,3,5):
            msg= 'Faces'
        
        rows = range(currentLoop.thisN * 6, currentLoop.thisN * 6 + 6)
        
        cueText.setText(msg)
        
        # keep track of which components have finished
        cueComponents = []
        cueComponents.append(matchText)
        cueComponents.append(cueText)
        for thisComponent in cueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "cue"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if frameN == 0:
                cueStartTime = fmriClock.getTime()
            
            
            # *matchText* updates
            if t >= 0.0 and matchText.status == NOT_STARTED:
                # keep track of start time/frame for later
                matchText.tStart = t  # underestimates by a little under one frame
                matchText.frameNStart = frameN  # exact frame index
                matchText.setAutoDraw(True)
            if matchText.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                matchText.setAutoDraw(False)
            
            # *cueText* updates
            if t >= 0.0 and cueText.status == NOT_STARTED:
                # keep track of start time/frame for later
                cueText.tStart = t  # underestimates by a little under one frame
                cueText.frameNStart = frameN  # exact frame index
                cueText.setAutoDraw(True)
            if cueText.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
                cueText.setAutoDraw(False)
            if frameN == 0:
                winRecorder.keyframe()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "cue"-------
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        cueEndTime = fmriClock.getTime()
        
        events.append(dict(
            run=runNum,
            condition='cue',
            duration=3,
            onset=cueStartTime))
        
        currentLoop.addData('cueStartTime', cueStartTime)
        currentLoop.addData('cueEndTime', cueEndTime)
        
        
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(condFile, selection=rows),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial.keys():
                    exec(paramName + '= thisTrial.' + paramName)
            
            #------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock 
            frameN = -1
            routineTimer.add(2.000000)
            # update component parameters for each repeat
            topImage.setImage(os.path.join('images', stimTop))
            leftImage.setImage(os.path.join('images', stimLeft))
            rightImage.setImage(os.path.join('images', stimRight))
            trialResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            trialResp.status = NOT_STARTED
            number_trials = ((trials.thisN + 1) + (blocks.thisN*6))
            
            trial_pat = 'Trial # %s of %d in this round.\n\nCorrect responses in this run: %04.2f %% \n\nNo responses in this run: %04.2f %% \n\n# correct responses in last five trials: %s \n\n# no response in last five trials: %s \n\n# same consecutive (no) responses: %s'
            trial_args = (number_trials, total_trials, corrRespPerc*100,noRespPerc*100,fiveBackCorrCount,fiveBacknoRespCount,countConsecutive)
            raText.text = trial_pat % trial_args
            raText.draw()
            raWinRecorder.keyframe()
            raWin.flip()
            
            # keep track of which components have finished
            trialComponents = []
            trialComponents.append(topImage)
            trialComponents.append(leftImage)
            trialComponents.append(rightImage)
            trialComponents.append(botLeftText)
            trialComponents.append(botRightText)
            trialComponents.append(pointerText)
            trialComponents.append(middleText)
            trialComponents.append(trialResp)
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trial"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *topImage* updates
                if t >= 0.0 and topImage.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    topImage.tStart = t  # underestimates by a little under one frame
                    topImage.frameNStart = frameN  # exact frame index
                    topImage.setAutoDraw(True)
                if topImage.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    topImage.setAutoDraw(False)
                
                # *leftImage* updates
                if t >= 0.0 and leftImage.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    leftImage.tStart = t  # underestimates by a little under one frame
                    leftImage.frameNStart = frameN  # exact frame index
                    leftImage.setAutoDraw(True)
                if leftImage.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    leftImage.setAutoDraw(False)
                
                # *rightImage* updates
                if t >= 0.0 and rightImage.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    rightImage.tStart = t  # underestimates by a little under one frame
                    rightImage.frameNStart = frameN  # exact frame index
                    rightImage.setAutoDraw(True)
                if rightImage.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    rightImage.setAutoDraw(False)
                
                # *botLeftText* updates
                if t >= 0.0 and botLeftText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    botLeftText.tStart = t  # underestimates by a little under one frame
                    botLeftText.frameNStart = frameN  # exact frame index
                    botLeftText.setAutoDraw(True)
                if botLeftText.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    botLeftText.setAutoDraw(False)
                
                # *botRightText* updates
                if t >= 0.0 and botRightText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    botRightText.tStart = t  # underestimates by a little under one frame
                    botRightText.frameNStart = frameN  # exact frame index
                    botRightText.setAutoDraw(True)
                if botRightText.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    botRightText.setAutoDraw(False)
                
                # *pointerText* updates
                if t >= 0.0 and pointerText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    pointerText.tStart = t  # underestimates by a little under one frame
                    pointerText.frameNStart = frameN  # exact frame index
                    pointerText.setAutoDraw(True)
                if pointerText.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    pointerText.setAutoDraw(False)
                
                # *middleText* updates
                if t >= 0.0 and middleText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    middleText.tStart = t  # underestimates by a little under one frame
                    middleText.frameNStart = frameN  # exact frame index
                    middleText.setAutoDraw(True)
                if middleText.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    middleText.setAutoDraw(False)
                
                # *trialResp* updates
                if t >= 0 and trialResp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    trialResp.tStart = t  # underestimates by a little under one frame
                    trialResp.frameNStart = frameN  # exact frame index
                    trialResp.status = STARTED
                    # AllowedKeys looks like a variable named `allowed_keys`
                    if not 'allowed_keys' in locals():
                        logging.error('AllowedKeys variable `allowed_keys` is not defined.')
                        core.quit()
                    if not type(allowed_keys) in [list, tuple, np.ndarray]:
                        if not isinstance(allowed_keys, basestring):
                            logging.error('AllowedKeys variable `allowed_keys` is not string- or list-like.')
                            core.quit()
                        elif not ',' in allowed_keys: allowed_keys = (allowed_keys,)
                        else:  allowed_keys = eval(allowed_keys)
                    # keyboard checking is just starting
                    win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if trialResp.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                    trialResp.status = STOPPED
                if trialResp.status == STARTED:
                    theseKeys = event.getKeys(keyList=list(allowed_keys))
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        trialResp.keys.extend(theseKeys)  # storing all keys
                        trialResp.rt.append(trialResp.clock.getTime())
                for prompt in buttonPrompts:
                    prompt.draw()
                if frameN == 0:
                    trialStartTime = fmriClock.getTime()
                if frameN == 0:
                    winRecorder.keyframe()
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if trialResp.keys in ['', [], None]:  # No response was made
               trialResp.keys=None
            # store data for trials (TrialHandler)
            trials.addData('trialResp.keys',trialResp.keys)
            if trialResp.keys != None:  # we had a response
                trials.addData('trialResp.rt', trialResp.rt)
            trialEndTime = fmriClock.getTime()
            
            resp=None
            respLast=None
            
            if trialResp.keys: #coding first response made by participant
                if trialResp.keys[0] in config['keys']['left']:
                    resp = 'left'
                elif trialResp.keys[0] in config['keys']['right']:
                    resp = 'right'
                elif not trialResp.keys:
                    resp = None
                    noResp+=1
            
            if trialResp.keys: #coding last response made by participant
                if trialResp.keys[-1] in config['keys']['left']:
                    respLast = 'left'
                elif trialResp.keys[-1] in config['keys']['right']:
                    respLast = 'right'
            
            if resp==str('left'):
                totalButtonTrack.append(1)
            elif resp==str('right'):
                totalButtonTrack.append(2)
            else: #no response
                totalButtonTrack.append(0)
            
            
            if (str(corrAns)==str('left') and resp == str('left')) or (str(corrAns)==str('right') and resp == 'right'):
                msg="Correct!"
                corrRespMsg="correct"
                corrRespCode = 1
                respTrack = 1
                correct_resp+=1
                corrRespPerc= (correct_resp)/(number_trials)
                noRespPerc = (noResp)/(number_trials)
                incorrRespPerc= (incorrect_resp)/(number_trials)
                totalCountList.append(respTrack)
            elif resp==None:
                msg="Too slow"
                corrRespMsg="miss"
                corrRespCode = 0
                respTrack = 2
                noResp+=1
                corrRespPerc= (correct_resp)/(number_trials)
                noRespPerc = (noResp)/(number_trials)
                incorrRespPerc= (incorrect_resp)/(number_trials)
                totalCountList.append(respTrack)
            elif (str(corrAns)==str('left') and resp != str('left')) or (str(corrAns)==str('right') and resp != 'right'):
                msg="Incorrect"
                corrRespMsg="incorrect"
                corrRespCode = 0
                respTrack = 0
                incorrect_resp+=1
                corrRespPerc= (correct_resp)/(number_trials)
                noRespPerc = (noResp)/(number_trials)
                incorrRespPerc= (incorrect_resp)/(number_trials)
                totalCountList.append(respTrack)
            
            if number_trials >= 5:
                fiveBackCorrCount = 0
                fiveBacknoRespCount = 0
                fiveBackIncorrCount = 0
                for i in range(-1, -6,-1):
                    if totalCountList[i] == 1:
                        fiveBackCorrCount+=1
                    elif totalCountList[i] == 2:
                        fiveBacknoRespCount+=1
                    elif totalCountList[i] == 0:
                        fiveBackIncorrCount+=1
            
            #track # consecutive responses with same button:
            if number_trials >=2:
                if totalButtonTrack[-1]==totalButtonTrack[-2]:
                    countConsecutive+=1
                elif totalButtonTrack[-1]!=totalButtonTrack[-2]:
                    countConsecutive=1
            
            if 'oval' in stimTop or 'circle' in stimTop:
                trialCondition = 'shape'
            else:
                trialCondition = 'face'
            
            currentLoop.addData('trialCondition', trialCondition)
            currentLoop.addData('trialNum', number_trials)
            currentLoop.addData('resp', resp)
            currentLoop.addData('respLast', respLast)
            currentLoop.addData('msg', msg)
            currentLoop.addData('corrRespMsg', corrRespMsg)
            currentLoop.addData('corrRespCode', corrRespCode)
            currentLoop.addData('respTrack', respTrack)
            currentLoop.addData('correct_resp', correct_resp)
            currentLoop.addData('incorrect_resp', incorrect_resp)
            currentLoop.addData('noResp', noResp)
            currentLoop.addData('corrRespPerc', corrRespPerc)
            currentLoop.addData('incorrRespPerc', incorrRespPerc)
            currentLoop.addData('noRespPerc', noRespPerc)
            
            #currentLoop.addData('totalCountList', totalCountList)
            currentLoop.addData('fiveBackCorrCount', fiveBackCorrCount)
            currentLoop.addData('fiveBacknoRespCount', fiveBacknoRespCount)
            currentLoop.addData('fiveBackIncorrCount', fiveBackIncorrCount)
            
            #currentLoop.addData('totalButtonTrack', totalButtonTrack)
            currentLoop.addData('countConsecutive', countConsecutive)
            
            currentLoop.addData('trialStartTime', trialStartTime)
            currentLoop.addData('trialEndTime', trialEndTime)
            
            events.append(dict(
                run=runNum,
                condition=trialCondition,
                duration=2,
                onset=trialStartTime))
            
            raText.text = trial_pat % trial_args
            raText.draw()
            raWin.flip()
            
            
            #------Prepare to start Routine "fixation"-------
            t = 0
            fixationClock.reset()  # clock 
            frameN = -1
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            
            # keep track of which components have finished
            fixationComponents = []
            fixationComponents.append(cross)
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "fixation"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = fixationClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cross* updates
                if t >= 0.0 and cross.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    cross.tStart = t  # underestimates by a little under one frame
                    cross.frameNStart = frameN  # exact frame index
                    cross.setAutoDraw(True)
                if cross.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    cross.setAutoDraw(False)
                if frameN == 0:
                    fixStartTime = fmriClock.getTime()
                    winRecorder.keyframe()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "fixation"-------
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            fixEndTime = fmriClock.getTime()
            
            currentLoop.addData('fixStartTime', fixStartTime)
            currentLoop.addData('fixEndTime', fixEndTime)
            
            entries = thisExp.entries
            
            if currentLoop.name != 'exampleTrials':
                updateRunLog(entries)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
    # completed nBlocks repeats of 'blocks'
    
    
    #------Prepare to start Routine "lastFixation"-------
    t = 0
    lastFixationClock.reset()  # clock 
    frameN = -1
    routineTimer.add(8.400000)
    # update component parameters for each repeat
    
    # keep track of which components have finished
    lastFixationComponents = []
    lastFixationComponents.append(lastFixationText)
    for thisComponent in lastFixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "lastFixation"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = lastFixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lastFixationText* updates
        if t >= 0.0 and lastFixationText.status == NOT_STARTED:
            # keep track of start time/frame for later
            lastFixationText.tStart = t  # underestimates by a little under one frame
            lastFixationText.frameNStart = frameN  # exact frame index
            lastFixationText.setAutoDraw(True)
        if lastFixationText.status == STARTED and t >= (0.0 + (8.4-win.monitorFramePeriod*0.75)): #most of one frame period left
            lastFixationText.setAutoDraw(False)
        if frameN == 0:
            winRecorder.keyframe()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lastFixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "lastFixation"-------
    for thisComponent in lastFixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    runEndTime = fmriClock.getTime()
    trials.addData('runEndTime', runEndTime)
    blocks.addData('runEndTime', runEndTime)
    
    events.append(dict(
        run=runNum,
        condition='runEnd',
        duration=0,
        onset=runEndTime))
    
    entries = thisExp.entries
    entries[-1]['runEndTime'] = runEndTime
    updateRunLog(entries)
    
    #------Prepare to start Routine "endRun"-------
    t = 0
    endRunClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    updateRunLog(thisExp.entries)
    
    # keep track of which components have finished
    endRunComponents = []
    for thisComponent in endRunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "endRun"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = endRunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "endRun"-------
    for thisComponent in endRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "endRun" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'runs'


#------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
if mode == 'practice':
    msg='You finished this practice!'
else:
    msg='You finished this game!'

endResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
endResp.status = NOT_STARTED
raText.text='Press <space> to exit.'
raText.draw()
raWinRecorder.keyframe()
raWin.flip()
# keep track of which components have finished
endComponents = []
endComponents.append(endText)
endComponents.append(endResp)
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *endText* updates
    if t >= 0.0 and endText.status == NOT_STARTED:
        # keep track of start time/frame for later
        endText.tStart = t  # underestimates by a little under one frame
        endText.frameNStart = frameN  # exact frame index
        endText.setAutoDraw(True)
    
    # *endResp* updates
    if t >= 0.0 and endResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        endResp.tStart = t  # underestimates by a little under one frame
        endResp.frameNStart = frameN  # exact frame index
        endResp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if endResp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            endResp.keys = theseKeys[-1]  # just the last key pressed
            endResp.rt = endResp.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    if frameN == 0:
        winRecorder.keyframe()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if endResp.keys in ['', [], None]:  # No response was made
   endResp.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('endResp.keys',endResp.keys)
if endResp.keys != None:  # we had a response
    thisExp.addData('endResp.rt', endResp.rt)
thisExp.nextEntry()

# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




save_movie(filename, winRecorder, raWinRecorder)





























events_df = pd.DataFrame(events)

design_outfile = os.path.join('data', filename + '_design.csv')
events_df.to_csv(design_outfile, index=False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
