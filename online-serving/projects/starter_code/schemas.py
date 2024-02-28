from pydantic import BaseModel


class PredictionRequest(BaseModel):
    # input data를 여기서 정의해주면 됨
    features: list


class PredictionResponse(BaseModel):
    id: int
    result: int