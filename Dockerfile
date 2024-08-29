# Use the NVIDIA CUDA Quantum base image
FROM nvcr.io/nvidia/quantum/cuda-quantum:0.8.0

# Switch to root user to perform installation of dependencies
USER root

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    build-essential \
    libffi-dev \
    libssl-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libsdl2-dev \
    python3-tk \
    wget \
    bzip2 \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh && \
    /opt/conda/bin/conda init bash

# Set environment variables for Conda
ENV PATH=/opt/conda/bin:$PATH
ENV SHELL=/bin/bash

# Create a new Conda environment with Python 3.10 and pip
RUN /bin/bash -c "source /opt/conda/etc/profile.d/conda.sh && conda create -y -n cuda-quantum python=3.10 pip"

# Install CUDA and MPI-related packages
RUN /bin/bash -c "source /opt/conda/etc/profile.d/conda.sh && \
    conda install -y -n cuda-quantum -c 'nvidia/label/cuda-11.8.0' cuda && \
    conda install -y -n cuda-quantum -c conda-forge mpi4py openmpi cxx-compiler"

# Set environment variables for the Conda environment
RUN /bin/bash -c "source /opt/conda/etc/profile.d/conda.sh && \
    conda env config vars set -n cuda-quantum LD_LIBRARY_PATH='$CONDA_PREFIX/envs/cuda-quantum/lib:$LD_LIBRARY_PATH' && \
    conda env config vars set -n cuda-quantum MPI_PATH=$CONDA_PREFIX/envs/cuda-quantum"

# Install additional Python packages
RUN /bin/bash -c "source /opt/conda/etc/profile.d/conda.sh && \
    conda run -n cuda-quantum pip install cuda-quantum pygame numpy"

# Add custom MPI activation to bashrc
RUN echo 'source $CONDA_PREFIX/lib/python3.10/site-packages/distributed_interfaces/activate_custom_mpi.sh' >> ~/.bashrc

# Set up the working directory inside the container
WORKDIR /workspace/quantum-flappy-bird

# Copy the local project files into the container
COPY . /workspace/quantum-flappy-bird/

# Default command to run the game using the Conda environment
CMD ["/bin/bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate cuda-quantum && python main.py"]
