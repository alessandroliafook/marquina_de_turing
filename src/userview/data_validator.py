def validade_path(path):
    try:
        open(path, "r")
        return True
    except IOError:
        return False