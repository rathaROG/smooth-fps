[![Test PyPI Build](https://github.com/rathaROG/smooth-fps/actions/workflows/prepublish.yaml/badge.svg)](https://github.com/rathaROG/smooth-fps/actions/workflows/prepublish.yaml)
[![Publish on PyPI](https://github.com/rathaROG/smooth-fps/actions/workflows/publish.yaml/badge.svg)](https://github.com/rathaROG/smooth-fps/actions/workflows/publish.yaml)

# SFPS - Smooth FPS

`SFPS` is a small and very efficient Python library which helps calculate the real-time computing frame rate with a few lines of code.

You can install from [PyPI](https://pypi.org/project/sfps/):

```
pip install sfps
```

You can import and initialize `SFPS` in your Python code:

```
from sfps import SFPS
sfps = SFPS(nframes=8, interval=1)
```
* `nframes` (`int`, `default=5`) : Number of the last frames, used for averaging.
* `interval` (`int`, `default=1`) : Time interval in second.

And then you can call `fps()` or `raw_fps()` to calculate the real-time frame rate.
```
...
fps = sfps.fps(format_spec='.2f')
...
```

For usage details, please check [`SFPS`](https://github.com/rathaROG/smooth-fps/blob/main/sfps/sfps.py). You can also check an [example here](https://github.com/rathaROG/smooth-fps/blob/main/example).
