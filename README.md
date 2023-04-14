# Run Tensorflow in Bash
* GPU Support: `docker run -p 8080:8080 -v /home/ixonstater/code/:/root/code --gpus all -it tensorflow/tensorflow:latest-gpu bash`
* CPU Only: `docker run -p 8080:8080 -v /root/code:/root/code -it tensorflow/tensorflow:latest bash`