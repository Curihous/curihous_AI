
> QBit은 사용자의 투자 성향을 기반으로 맞춤형 투자 학습 경험을 제공하는 iOS 애플리케이션 서비스입니다.
> 이 레포지토리는 QBit의 AI 서버로, 강화학습을 활용한 투자 전략 추천 기능을 비롯해 다양한 투자 분석 및 피드백 기능을 담당합니다. FastAPI를 기반으로 구현되었으며, 서비스의 AI 연산을 분리하여 처리하는 구조입니다.

### 주요 기술 스택
- FastAPI: 비동기 웹 프레임워크
- Stable-Baselines3: 강화학습 모델 학습 및 추론 (PPO)
- pandas-ta: 기술적 지표 계산
- KeyBERT: 뉴스 키워드 추출 및 감성 분석
- numpy, pandas: 데이터 전처리 및 수치 계산
- Docker: 컨테이너 기반 실행
- PyTorch: PPO 모델 학습 프레임워크 (SB3 내부 사용)

### 핵심 폴더 구조
```
curihous_AI/
├── venv/                      # ✅ 가상환경 (Python 패키지, 실행파일 등 포함) ← Git에 올리지 않음
│
├── app/                      # ✅ FastAPI 백엔드 애플리케이션 코드
│   ├── main.py               # FastAPI 앱 시작점
│   ├── api/                  # 라우터 (예: /recommend)
│   │   └── recommend.py
│   ├── schemas/              # 요청/응답 Pydantic 모델
│   │   └── recommend.py
│   ├── services/             # 상태 생성, 추천 해석 등 비즈니스 로직
│   │   └── recommender.py
│   ├── core/                 # 공통 유틸 (설정, 예외처리, 응답포맷)
│   │   ├── config.py         # .env 설정 로더
│   │   ├── exceptions.py     # GlobalExceptionHandler
│   │   └── response.py       # ApiResponse
│   └── utils/                # 기술 지표 계산, 뉴스 처리 등 유틸
│       ├── ta_utils.py
│       └── news_utils.py
│
├── ai/                       # ✅ 강화학습 관련 코드
│   ├── env/                  # 사용자 정의 강화학습 환경
│   │   └── my_trading_env.py
│   ├── train/                # PPO 학습 스크립트
│   │   └── train_agent.py
│   ├── inference/           # FastAPI 서버에서 모델 서빙을 위한 모듈
│   │   └── policy_wrapper.py
│   └── models/              # ✅ 사용자별 학습된 정책 저장소 (.pkl)
│       ├── user_1.pkl
│       ├── user_2.pkl
│       └── ...
│
├── data/                     # ✅ 실시간 데이터 수집 및 전처리
│   ├── preprocess.py         # OHLCV, 기술지표, 뉴스 감성 등 전처리
│   └── raw/                  # 수집된 원본 데이터 저장소
│       └── tsla_ohlcv.csv
│
├── scripts/                  # 학습 or 서버 실행용 스크립트
│   ├── launch_train.sh
│   └── launch_server.sh
│
├── .env                      # 민감한 설정 (.env.example도 같이 두기)
├── .gitignore                # venv, __pycache__, .env 등 제외
├── requirements.txt          # pip install -r requirements.txt 용
└── README.md                 # 프로젝트 설명서
```

### 실행 방법
Python 가상환경을 만들고 필요한 패키지를 설치합니다.
```python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
FastAPI 서버를 실행합니다.
uvicorn main:app --reload
또는 Docker로 실행할 경우
docker build -t qbit-ai-server .
docker run -p 8000:8000 qbit-ai-server
```

### 기능 설명
* 강화학습 기반 전략 추천 (/recommend): 사용자의 투자 성향, 기술 지표, 뉴스 감성을 입력받아 적절한 투자 행동을 추천합니다.
* PPO 모델 로딩 및 추론: Stable-Baselines3를 통해 학습된 정책 모델을 로딩하여 실시간 예측에 활용합니다.
* 사용자 정의 환경: OpenAI Gym 형태로 구현된 강화학습 환경을 통해 투자 시뮬레이션이 가능합니다.
* 데이터 전처리 및 감성 분석: KeyBERT 및 기술 지표 계산을 통해 상태(state)를 구성합니다.


### 기타
* 모든 민감 정보는 secrets.toml 또는 환경변수로 관리됩니다.
* FastAPI 서버는 프론트엔드 및 백엔드 서버와 REST API로 통신합니다.
* 확장 가능한 모듈 구조로 구성되어 있어, sentiment_analysis, feedback_report 등의 기능을 추가할 수 있습니다.
