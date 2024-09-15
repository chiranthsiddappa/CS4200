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

Recommended run options:

* `-v`: Host volume mounted into container
* `--net=host`: Provide all ports to the container
* `-p`: Expose a container port to the host (recommended)

```bash
docker run -it -v /path/on/host:/home/$USER/cs4200 -p 8888:8888 cs4200 /bin/bash
```

### Python Requirements   
I recommend using a virtual environment specifically for this course.
The docker image built from above will contain these dependencies.   
```
python3 -m venv venv
source venv/bin/activate
```
If you are on an Intel/AMD CPU, please install this version of numpy, otherwise remove the `-i`  or run only the second line.   
```bash
pip install -i https://pypi.anaconda.org/intel/simple numpy==1.26.*
pip install numpy==1.26.* matplotlib jupyterlab pymap3d
```
If you ran the `venv`  step above, make sure that your virtual environment is active.   
To show a completed setup, run the following:   
```python
import numpy as np

np.show_config()
```

## VM

The `Vagrantfile` was tested with major version 2 for vagrant, and version `7.0` for virtualbox.

```bash
vagrant up
vagrant ssh
```

More notes on accessing the virtual machine ports can be found [here](https://github.com/chiranthsiddappa/CS2080/tree/main/vm).

## Incline

```bash
sbatch nvidia-smi-output.sh
```
