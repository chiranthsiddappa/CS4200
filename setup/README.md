# Setup Project   
To prove a successful verilator and cocotb setup, run the example from the README:   
- [https://github.com/cocotb/cocotb](https://github.com/cocotb/cocotb)
- `make SIM=verilator`

Verilator: Version 5.016   
```
FROM python:3.9.18

COPY --from=verilator/verilator:v5.016 /usr/local/bin /usr/local/bin
COPY --from=verilator/verilator:v5.016 /usr/local/share/verilator /usr/local/share/verilator

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    && apt-get install --no-install-recommends -y \
    ccache \
    perl-doc

ARG developer
ARG uid
ENV developer $developer
ENV uid $uid
ARG gid
ENV gid $gid

RUN adduser $developer && \
        usermod -u $uid $developer
RUN groupmod $developer -g $gid

USER $developer
WORKDIR /home/$developer/

COPY requirements.txt requirements.txt
RUN python3 -m venv /home/$developer/venv
RUN /home/$developer/venv/bin/pip install "cocotb>=1.8,<1.9" "pytest>=7.4,<7.5"
RUN /home/$developer/venv/bin/pip install -r requirements.txt

CMD su - $developer
```
### Python Requirements   
I recommend using a virtual environment specifically for this course.   
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
```
import numpy as np

np.show_config()
```

## Incline

```bash
sbatch nvidia-smi-output.sh
```
