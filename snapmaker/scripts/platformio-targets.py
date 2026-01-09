import sys
from os.path import join

Import("env", "projenv")

# Single action/command per 1 target
# env.AddCustomTarget("sysenv", None, 'python -c "import os; print(os.environ)"'))


# Multiple actions
# env.AddCustomTarget(
#     name="pioenv",
#     dependencies=None,
#     actions=[
#     "pio --version",
#     "python --version"
#     ],
#     title="Core Env",
#     description="Show PlatformIO Core and Python versions"
# )


project_dir = projenv.get("PROJECT_DIR")

pack_script = join(project_dir, 'snapmaker', 'scripts', 'pack.py')

fw_bin = join(projenv.get("PROJECT_BUILD_DIR"), projenv.get("PIOENV"), projenv.get("PROGNAME") + '.bin')


def _quote(path: str) -> str:
    return '"{0}"'.format(path)


env.AddCustomTarget(
    name="pack",
    dependencies=None,
    actions=[
    "{py} {script} -d {project} -c {bin} ".format(
        py=_quote(sys.executable),
        script=_quote(pack_script),
        project=_quote(project_dir),
        bin=_quote(fw_bin),
    ),
    ],
    title="Pack",
    description="Pack Snapmaker Firmware"
)
