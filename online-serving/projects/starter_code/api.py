from fastapi import APIRouter, HTTPException, status

from schemas import PredictionRequest, PredictionResponse
from dependency import get_model
from database import PredictionResult, engine
from sqlmodel import Session, select

router = APIRouter()

@router.post("/predict")
def predict(requests: PredictionRequest) -> PredictionResponse:
    # Model load
    model = get_model()
    
    # predict
    prediction = int(model.predict([requests.features])[0])
    
    # save to db
    # DB 객체를 생성하고, 그때 prediction을 사용
    prediction_result = PredictionResult(result=prediction)
    with Session(engine) as session:
        session.add(prediction_result)
        session.commit() # id를 자동으로 만들어줌
        session.refresh(prediction_result) 
        
    return PredictionResponse(id=prediction_result.id, result=prediction)


@router.get("/predict/{id}")
def get_prediction_with_id(id: int):
    with Session(engine) as session:
        prediction_result = session.get(PredictionResult, id)
        if not prediction_result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail="Prediction not found"
            )
        
        return PredictionResponse(id=prediction_result.id, result=prediction_result.result)


@router.get("/predict")
def get_predictions() -> list[PredictionResponse]:
    with Session(engine) as session:
        statement = select(PredictionResult)
        prediction_results = session.exec(statement).all()
        # prediction_results = session.query(PredictionResult).all() # query가 deprecated
        
    return [PredictionResponse(id=prediction_result.id, result=prediction_result.result)
        for prediction_result in prediction_results
    ]
