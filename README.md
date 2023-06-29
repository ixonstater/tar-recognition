# Run Tensorflow in Bash
* GPU Support: `docker run -v /home/ixonstater/code/:/root/code --gpus all -it tensorflow/tensorflow:latest-gpu bash`
* CPU Only: `docker run -p 8080:8080 -v /root/code:/root/code -it tensorflow/tensorflow:latest bash`

Data may be downloaded from [Google Drives](https://drive.google.com/file/d/1K-r2qYxtwnTMoaWzqRRry5PAQZQ6o0GY/view?usp=sharing).