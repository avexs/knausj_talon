from talon import Module, Context, actions, ui, imgui, clip, settings
import re

from talon import actions, Context, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.tcl
mode: command 
and code.language: tcl
"""
ctx.lists["user.code_functions"] = {
    "after": "after",
    "append": "append",
    "apply": "apply",
    "array": "array" ,
    "break": "break" ,
    "catch": "catch",
    "change directory": "cd",
    "channel": "chan",
    "clock": "clock",
    "close": "close",
    "concatenate": "concat",
    "dictionary": "dict",
    "evaluate": "eval",
    "execute": "exec",
    "exit": "exit",
    "expression": "expr",
    "file": "file" ,
    "for": "for",
    "foreach": "foreach",
    "if": "if",
    "increment": "incr",
    "info": "info",
    "list append": "lappend",
    "list assign": "lassign",
    "list insert": "linsert",
    "list": "list",
    "list length": "llength",
    "list map": "lmap",
    "load": "load",
    "list range": "lrange",
    "list repeat": "lrepeat",
    "list replace": "lreplace",
    "list reverse": "lreverse",
    "list search": "lsearch",
    "list set": "lset",
    "list sort": "lsort",
    "namespace": "namespace",
    "open": "open",
    "package": "package",
    "procedure": "procedure",
    "proc": "proc",
    "puts": "puts",
    "print working directory": "pwd",
}


