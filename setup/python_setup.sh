python3 -m venv venv
source venv/bin/activate
pip install -i https://pypi.anaconda.org/intel/simple numpy==1.26.*
pip install numpy==1.26.* matplotlib jupyterlab pymap3d
pip install "cocotb>=1.8,<1.9" "pytest>=7.4,<7.5"
