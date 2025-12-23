from __future__ import annotations

import inspect
import sys
from types import FrameType
from typing import Optional

from .lazy_module import LazyModule

__all__ = ["lazyload"]


def _get_caller_globals() -> Optional[dict]:
    frame: Optional[FrameType] = inspect.currentframe()
    if frame is None or frame.f_back is None:
        return None
    return frame.f_back.f_globals


def lazyload(name: str, *, inject: bool = True) -> LazyModule:
    """
    Lazily load a module.

    Example:
        lazyload("pygame")
        pygame.display.set_mode((800, 600))

    Or:
        pygame = lazyload("pygame")

    :param name: Name of the module to load.
    :param inject: Whether to inject generated LazyModule instance to global variables.
    :return: Generated LazyModule instance.
        This can be used instead of the injected variable if injection doesn't work or is disabled.
    """

    existing = sys.modules.get(name)
    if isinstance(existing, LazyModule):
        proxy = existing
    elif existing is not None:
        return LazyModule(name)
    else:
        proxy = LazyModule(name)
        sys.modules[name] = proxy

    if inject:
        globals_ = _get_caller_globals()
        if globals_ is not None:
            globals_.setdefault(name, proxy)

    return proxy
