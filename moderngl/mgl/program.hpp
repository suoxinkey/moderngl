#pragma once
#include "mgl.hpp"
#include "context.hpp"

struct MGLProgram {
    PyObject_HEAD
    PyObject * wrapper;
    MGLContext * context;
    int program_obj;
    int shader_obj[5];
};