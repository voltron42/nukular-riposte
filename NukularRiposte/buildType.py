""" This module provides the build type enum """
# nukular-riposte/buildType.py

from enum import Enum

class BuildType(Enum):
    Ecosystem = 1
    App = 2
    Page = 3
    Component = 4
    Namespace = 5
