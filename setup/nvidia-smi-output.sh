#!/bin/bash

##Resource Request

#SBATCH --job-name InspectCUDAJob
#SBATCH --output result.out   ## filename of the output; the %j is equivalent to jobID; default is slurm-[jobID].out
#SBATCH --nodes=1
#SBATCH --partition=gpu  ## the partitions to run in (comma seperated)
#SBATCH --time=0-00:01:00  ## time for analysis (day-hour:min:sec)

##Load the CUDA module
module load cuda

nvidia-smi > $HOME/nvidia_output.txt

nvcc --version >> $HOME/nvidia_output.txt
