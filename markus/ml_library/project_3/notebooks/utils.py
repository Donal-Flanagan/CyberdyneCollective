"""
This file has to be in every folder/package

Find project directory and append it to sys.path.
"""

import sys
import os
import warnings

def get_project_dir(project=None):
    current_dir = os.path.abspath('./')
    print(current_dir)

    if project is None:
        project_dir = current_dir
    else:
        position = current_dir.rfind(project)
        if position >= 0:
            project_dir = current_dir[:position+len(project)]
        elif position == -1:
            warnings.warn('project not found, return current_dir')
            project_dir = current_dir
        else:
            raise NotImplementedError
    if project_dir not in sys.path:
        sys.path.append(project_dir)
    return project_dir


def set_project_dir(project=None):
    current_dir = os.path.abspath('./')
    print(current_dir)

    if project is None:
        project_dir = current_dir
    else:
        position = current_dir.rfind(project)
        if position >= 0:
            project_dir = current_dir[:position+len(project)]
        elif position == -1:
            warnings.warn('project not found, return current_dir')
            project_dir = current_dir
        else:
            raise NotImplementedError
    if project_dir not in sys.path:
        sys.path.append(project_dir)
    os.chdir(project_dir)
    return project_dir
