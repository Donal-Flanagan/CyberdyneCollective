def get_project_dir(project):
    """Returns project directory path and appends it to sys.path"""
    current_dir = os.path.abspath('./')
    project_dir = current_dir[:current_dir.rfind(project)+len(project)+1]
    sys.path.append(project_dir)
    return project_dir
