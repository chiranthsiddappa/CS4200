# Setup Project   
To prove a successful verilator and cocotb setup, run the example from the README:   
- [https://github.com/cocotb/cocotb](https://github.com/cocotb/cocotb)
- `make SIM=verilator`

Verilator: Version 5.016
## Dockerfile

The following [Dockerfile](./Dockerfile) can be used with this [Makefile](./Makefile).
This allows for make to handle passing the parameters and build arguments to docker directly.

```bash
make
```

### Python Requirements   
I recommend using a virtual environment specifically for this course.
The docker image built from above will contain these dependencies.   
```
python3 -m venv venv
source venv/bin/activate
```
If you are on an Intel/AMD CPU, please install this version of numpy, otherwise remove the `-i`  or run only the second line.   
```
pip install -i https://pypi.anaconda.org/intel/simple numpy==1.26.*
pip install numpy==1.26.* matplotlib jupyterlab pymap3d
```
If you ran the `venv`  step above, make sure that your virtual environment is active.   
To show a completed setup, run the following:   
```python
import numpy as np

np.show_config()
```

## Incline

```bash
sbatch nvidia-smi-output.sh
```
