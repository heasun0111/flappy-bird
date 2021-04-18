### ‘AI입문’ 수업을 통해 진행한 프로젝트입니다.

Pytorch를 이용해서 모델을 만들었으며, 다층 레이어를 통해 학습하며 activation function으로는 ReLU를 사용했습니다.<br>
본 프로그램은 train.py에서 학습시키고, 학습되는 값을 보며 DQN.py (Deep Neural Network)의 파라미터 값을 조정합니다.
<br>

This project was conducted through AI Introduction class.<br>
This program used Pytorch to model, learn from multi-layer layers, and use ReLU activation function.<br>
train.py has a code for learning and adjusts parameter values for DQN.py (Deep Neural Network).
<br><br><br>


#### <실행법>
Colab notebooks 디렉토리에 flappy bird파일을 업로드하고 main.ipynb파일을 업로드해서 모두 실행을 누르면 실행할 수 있습니다.<br>
(하드웨어 가속기는 GPU 사용 추천)
<br><br>

#### <DQN.py 설명>
DQN.py에서 nn.Module을 이용해서 forward만 코딩을 했으며, backward는 파이토치 내장 함수로 구현하였습니다.<br>
Forward의 input에 텐서가 들어오는데 Batch x channel x H x W (ex: 32 x 4 x 84 x 84)를 이용해서 계산했습니다.
<br><br>

#### <train.py>
하이퍼 파라미터를 통해 Batch_size, Buffer_size, Learning rate 등을 선언하고, Agent(새)는 agent폴더에 있는 agent.py로 구현했고 import해서 사용했습니다.<br> train에 hParam, env(환경), agent를 통해 학습했으며 SummaryWriter( )를 통해 텐서보드를 출력해서 flappy bird가 제대로 학습되고 있는지 확인시켰습니다.<br> Loss=agent.updateQnet( )을 통해서 학습한 내용을 업데이트 했으며, buffer에 다음 state, 이미지, 게임이 끝났는지 아닌지 등의 정보를 입력하여 학습을 반복합니다.
<br><br>

#### <flappy bird 게임 이미지>
![flappy bird play image](./example img/flappy bird 예시.png)
