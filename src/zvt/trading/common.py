# -*- coding: utf-8 -*-
from enum import Enum


class ExecutionStatus(Enum):
    init = "init"
    success = "success"
    failed = "failed"
