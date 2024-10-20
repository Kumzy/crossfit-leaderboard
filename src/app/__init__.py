# SPDX-FileCopyrightText: 2023-present Cody Fincher <cody.fincher@gmail.com>
#
# SPDX-License-Identifier: MIT
import multiprocessing
import platform

if platform.system() in ("Darwin", "Windows"):
    multiprocessing.set_start_method("fork", force=True)
