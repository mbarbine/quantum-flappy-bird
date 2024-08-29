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
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install additional Python dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pygame numpy

# Set up the working directory inside the container
WORKDIR /workspace/quantum-flappy-bird

# Copy the local project files into the container
COPY . /workspace/quantum-flappy-bird/

# Switch back to a non-root user if needed (this step is optional and depends on your security requirements)
# USER cuda

# Expose necessary ports (if any)
# EXPOSE 8080  # Optional: use if you need network access

# Default command to run the game
CMD ["python3", "main.py"]
