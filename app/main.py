from fastapi import FastAPI
from app.api import recommend
from app.core.exceptions import add_exception_handlers

app = FastAPI()

# 라우터 등록
app.include_router(recommend.router)

# 예외 핸들러 등록
add_exception_handlers(app)

@app.get("/")
def root():
    return {"message": "PPO Trading Recommendation API is running"}