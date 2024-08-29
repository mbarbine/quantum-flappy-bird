# Conda Install

conda create -y -n cuda-quantum python=3.10 pip
conda install -y -n cuda-quantum -c "nvidia/label/cuda-11.8.0" cuda
conda install -y -n cuda-quantum -c conda-forge mpi4py openmpi cxx-compiler
conda env config vars set -n cuda-quantum LD_LIBRARY_PATH="$CONDA_PREFIX/envs/cuda-quantum/lib:$LD_LIBRARY_PATH"
conda env config vars set -n cuda-quantum MPI_PATH=$CONDA_PREFIX/envs/cuda-quantum
conda run -n cuda-quantum pip install cuda-quantum
conda activate cuda-quantum
source $CONDA_PREFIX/lib/python3.10/site-packages/distributed_interfaces/activate_custom_mpi.sh

