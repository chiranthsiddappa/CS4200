# Python 3.9 Incline

## Build and Install

```shell
./python_incline.sh
```
This shell script runs the sbatch command to build and install python using the compute servers.
Once the build is complete, you will see the following output in a file `python_build.out`

```text
Installing collected packages: setuptools, pip
  WARNING: The scripts pip3 and pip3.9 are installed in '/home/csiddapp/bin/Python-3.9.20/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-23.0.1 setuptools-58.1.0
```

To watch the build process live, you can follow the file using `tail`

```shell
tail -F python_build.out
```

## Environment

To build your environemt on incline, run the following commands:

```shell
$HOME/bin/Python-3.9.20/bin/python3 -m venv $HOME/venv_cs4200
source $HOME/venv_cs4200/bin/activate
pip install -r requirements-np.txt
pip install cupy-cuda11x==13.3.*
```
