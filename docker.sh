docker pull nvcr.io/nvidia/quantum/cuda-quantum:0.8.0
#docker run --gpus all -it nvcr.io/nvidia/quantum/cuda-quantum:0.8.0
docker run --gpus all -it -v ./:quantum-flappy-bird nvcr.io/nvidia/quantum/cuda-quantum:0.8.0
