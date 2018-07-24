import importlib
from typing import Any

from . import mgl
from .limits import Limits
from .program import Program


class Context:
    __slots__ = ['__mglo', 'version_code', 'limits', 'extra']

    def __init__(self):
        self.__mglo = None  # type: Any
        self.version_code = None  # type: int
        self.limits = None  # type: Limits
        self.extra = None  # type: Any

    def program(self, vertex_shader, fragment_shader=None, geometry_shader=None, tess_control_shader=None, tess_evaluation_shader=None, varyings=()) -> Program:
        return self.__mglo.program(vertex_shader, fragment_shader, geometry_shader, tess_control_shader, tess_evaluation_shader, varyings)


def create_context(standalone=False, debug=False):
    if debug:
        moderngl_debug = importlib.import_module('moderngl.debug')
        return moderngl_debug.create_context(standalone)
    else:
        return mgl.create_context(standalone)


def extensions(context):
    return mgl.extensions(context)


def hwinfo(context):
    return mgl.hwinfo(context)