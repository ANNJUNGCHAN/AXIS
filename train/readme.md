# 모델 학습 방법
- 모델을 학습하는 방법에 대해 담고있습니다.

## 1. 도커 컨테이너 구성
```
# nvidia 도커 이미지 풀링하기
docker pull nvcr.io/nvidia/pytorch:21.08-py3

# 도커 컨테이너 설치하기
## -v는 바인드 마운팅을 할 때 사용
## nvidia-docker는 wsl에서 사용할 수 없기에, 먼저 nvcr.io/nvidia/pytorch:21.08-py3 이미지를 다운받은 후, docker run을 실행
docker run --name yolov7 -it -v /home/sunjin/AXIS/AXIS/train:/Drive/ -v /home/sunjin/AXIS/AXIS/yolov7:/yolov7/ --gpus all --shm-size=64g nvcr.io/nvidia/pytorch:21.08-py3

# 필요한 패키지 apt install
apt update
apt install -y zip htop screen libgl1-mesa-glx

# 필요한 패키지 pip install
pip install seaborn thop

# 이동하기
cd /yolov7
```