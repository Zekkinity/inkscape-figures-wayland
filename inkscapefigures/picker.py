import subprocess
import platform

SYSTEM_NAME = platform.system()


def get_picker_cmd(picker_args=None, fuzzy=True):
    """
    Create the shell command that will be run to start the picker.
    """

    if SYSTEM_NAME == "Linux":
        args = ['wofi', '--show=dmenu']
        if fuzzy:
            args += ['--matching=token']
        args += ['--prompt=Select Figure']
    elif SYSTEM_NAME == "Darwin":
        args = ["choose"]
    else:
        raise ValueError("No supported picker for {}".format(SYSTEM_NAME))

    if picker_args is not None:
        args += picker_args

    return [str(arg) for arg in args]


def pick(options, picker_args=None, fuzzy=True):
    optionstr = '\n'.join(option.replace('\n', ' ') for option in options)
    cmd = get_picker_cmd(picker_args=picker_args, fuzzy=fuzzy)
    result = subprocess.run(cmd, input=optionstr, stdout=subprocess.PIPE,
                            universal_newlines=True)
    stdout = result.stdout.strip()

    if result.returncode == 0:
        key = 0
    elif result.returncode == 1:
        key = -1
    else:
        raise RuntimeError(f"Picker returned unexpected code: {result.returncode}")

    selected = stdout.strip()
    try:
        index = [opt.strip() for opt in options].index(selected)
    except ValueError:
        index = -1

    return key, index, selected

