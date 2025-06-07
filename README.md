
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
```ai-server/
├── README.md
├── requirements.txt (필요 패키지 목록)
├── .gitignore
├── main.py (FastAPI 진입점)
├── app/ (전체 앱 실행 로직 포함)
│
├── modules/ (AI 기능별 모듈 디렉터리)
│ ├── trading_strategy/ (강화학습 기반 투자 전략 추천 기능)
│ │ ├── init.py
│ │ ├── api.py /recommend 엔드포인트 정의
│ │ ├── model.py PPO 모델 로딩 및 추론
│ │ ├── state.py 상태 벡터 구성 및 행동 디코딩
│ │ ├── env/
│ │ │ └── my_trading_env.py 사용자 정의 강화학습 환경 클래스
│ │ └── data/
│ │ ├── preprocess.py 기술 지표 및 감성 분석 전처리
│ │ └── external_api.py Benzinga 등 외부 API 연동 래퍼
│
├── configs/
│ ├── settings.py 설정값 및 환경변수 로딩
│ └── secrets.toml 민감 정보 관리 파일 (.gitignore 대상)
│
├── models/
│ └── trading_strategy/
│ └── policy_model.pkl 학습된 강화학습 정책 모델
│
└── tests/
├── test_main.py
└── trading_strategy/ 유닛 테스트 모음
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
