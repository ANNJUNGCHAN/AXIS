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

## 2.학습시키기
```
# 가상환경 구성
python -m venv yolov7
source /yolov7/yolov7/bin/activate

# 가상환경 내 토치 환경 구성
pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

# 가상환경 내 yolov7 필요 패키지 설치
pip install -r requirements.txt

# docker 접속
docker exec -it yolov7 /bin/bash

# 가상환경 접속
source /yolov7/yolov7/bin/activate

# 경로 이동
cd /yolov7

# 훈련코드(초기)
python train_aux.py --workers 8 --device 0 --batch-size 8 --data /yolov7/data/xray.yaml --img 1280 1280 --cfg /yolov7/cfg/training/yolov7-e6e-xray.yaml --project /Drive/model --weights /Drive/model/AXIS_20240703_trial1/weights/best.pt --name AXIS_20240704_trial1 --hyp /yolov7/data/hyp.scratch.p6.yaml
```