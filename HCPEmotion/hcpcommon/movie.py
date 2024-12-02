import glob
import os
import numpy as np
from subprocess import Popen, PIPE


class WinRecorder(object):
    def __init__(self, win, clock, record=False, cleanup=True):
        self._keyframes = []
        self._keyframeTimes = []
        self._win = win
        self._clock = clock
        self._record = record
        self._cleanup = cleanup
        self.movie_fname = None

        # print(win, win.name)

    def keyframe(self, buffer='back'):
        if self._record:
            self._keyframe(buffer=buffer)

    def _keyframe(self, buffer):
        for thisStim in self._win._toDraw:
            thisStim.draw()  # Manually AutoDraw
        self._keyframes.append(self._win.getMovieFrame(buffer=buffer))
        self._keyframeTimes.append(self._clock.getTime())
        # print('Saving keyframe for {}'.format(self._win.name))
        # print('Window {} now has {} frames'.format(self._win.name,
        #                                            len(self._win.movieFrames)))

    def save(self, fname='win-frame.png'):
        '''Write out screenshots.

           Call at the end of the task.
           Filename should include include extension; Psychopy's window capture
           will add frame indices automatically.'''
        if self._record:
            self.movie_fname = self._save(fname)

    def _save(self, fname):
        print('Saving {} keyframes for {}'.format(
            len(self._keyframes), self._win.name))
        self._win.saveMovieFrames(fname)
        stillbase, stillext = os.path.splitext(fname)
        demuxBase = stillbase + '_demux'
        demuxFname = demuxBase + '.txt'
        self._writeConcatDemuxFile(demuxFname, fname)
        video_fname = demuxBase + '.mov'
        # print('To demux and create video, run:')
        cmd = ['ffmpeg', '-f', 'concat', '-i', demuxFname, '-vsync', 'vfr',
               '-pix_fmt', 'yuv420p', video_fname]
        # print(' '.join(cmd))
        out = Popen(cmd)
        out.communicate()
        if self._cleanup and os.path.exists(
                video_fname):  # Concat was successfull
            for f in glob.glob(stillbase + '*' + stillext):
                os.remove(f)
            for f in glob.glob(stillbase + '*demux*.txt'):
                os.remove(f)
        return video_fname

    def _writeConcatDemuxFile(self, demuxFname, imFname):
        times = self.diffTimes(self._keyframeTimes)
        names = self.genFnames(imFname, len(times))

        with open(demuxFname, 'w') as f:
            for fn, dt in zip(names, times):
                f.write(fn + '\n')
                f.write('duration %.02f\n' % dt)

    def diffTimes(self, times):
        times = np.array(times)
        diffs = times[1:] - times[:-1]

        # Add last time again for ffmpeg quirk that requires last frame to be
        # listed twice.
        np.append(diffs, diffs[-1])
        return diffs

    def genFnames(self, fname, n):
        base, ext = os.path.splitext(fname)
        n_digits = len(str(n))
        fnames = ["file '{}{:0{n_digits}}{}'".format(base,
                                                     i,
                                                     ext,
                                                     n_digits=n_digits)
                  for i in range(1, n + 1)]

        # Add the last frame a second time - ffmpeg quirk
        fnames.append(fnames[-1])
        return fnames

    @classmethod
    def save_sidebyside(cls, movies, fname):
        if movies[0]._record:
            cls._save_sidebyside(movies, fname)

    @classmethod
    def _save_sidebyside(cls, movies, fname, quality=35):
        cmd = ['ffmpeg']
        for movie in movies:
            cmd.extend(['-i', movie.movie_fname])

        movie_options = ["-filter_complex",
                         "[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]",
                         "-map", "[vid]", "-c:v", "libx264", "-crf",
                         str(quality), "-preset", "veryfast"]

        cmd.extend(movie_options + [fname])

        # print(' '.join(cmd))
        out = Popen(cmd, shell=False)
        out.communicate()

        if movies[0]._cleanup and os.path.exists(fname):
            for movie in movies:
                os.remove(movie.movie_fname)
