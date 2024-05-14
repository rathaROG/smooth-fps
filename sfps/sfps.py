# SFPS - Smooth FPS
# BSD 2-Clause License
# Copyright (c) 2024, Ratha SIV

from timeit import time
from collections import deque

class SFPS(object):
    """SFPS - Smooth FPS.
    """

    def __init__(self, nframes=5, interval=1):
        """Construct a SFPS.

        Parameters
        ----------
        nframes : int, default=5
            Number of the last frames, used for averaging.
        interval : int, default=1
            Time interval in second.
        """
        self._nf = int(nframes)
        self._itv = int(interval)
        self._ts = deque(maxlen=self._nf if self._nf > -1 else 0)
        self._pt = 0.0
        self._fps = 0.0
    
    def _update(self):
        """Update/Calculate the FPS.
        """
        ct = time.time()
        t = ct - self._pt
        self._pt = ct
        self._ts.append(t)
        st = sum(self._ts)
        if st > 0:
            self._fps = self._itv * len(self._ts) / st
    
    def fps(self, format_spec='.2f'):
        """Calculate FPS and return string FPS.

        Parameters
        ----------
        format_spec : str, default='.2f'
            Format specification.

        Returns
        -------
        str
            FPS number as string.
        """
        self._update()
        return format(self._fps, format_spec)
    
    def raw_fps(self):
        """Calculate FPS and return raw FPS.

        Returns
        -------
        float
            FPS number.
        """
        self._update()
        return self._fps
