#!/bin/bash

##Resource Request

#SBATCH --job-name BuildPython
#SBATCH --output python_build.out   ## filename of the output; the %j is equivalent to jobID; default is slurm-[jobID].out
#SBATCH --nodes=1
#SBATCH --time=0-00:10:00  ## time for analysis (day-hour:min:sec)

pushd $HOME/Python-3.9.20
make -j 10
make -j 10 install
popd

