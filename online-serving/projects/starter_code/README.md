# FastAPI Web Single Pattern
- 목적 : FastAPI를 사용해 Web Single 패턴을 구현합니다
- 상황 : 데이터 과학자가 model.py을 만들었고(model.joblib이 학습 결과), 그 model을 FastAPI을 사용해 Online Serving을 구현해야 함
  - model.py는 추후에 수정될 수 있으므로, model.py를 수정하지 않음(데이터 과학자쪽에서 수정)

# 시작하기 전에...
- 어떻게 설계하고 시작할까?
  - 내 생각과 모범 답안의 diff를 찾아내고, 왜 그러한 diff가 발생했는지

# FastAPI 개발
- FastAPI를 개발할 떄의 흐름
- 전체 구조를 생각 => 파일, 폴더 구조를 어떻게 할까?
  - predict.py, api.py, config.py ..
  - 계층화 아키텍쳐 : 3 tier, 4 tier ...
  - Presentation(API) <-> Application(Service) <-> Database
- API : 외부와 통신, 건물의 문처럼 외부 경로. Client에서 API 호출. 학습 결과 Return
  - schema : FastAPI에서 사용되는 개념
    - 자바의 DTO(Data Tranfer Object). Network를 통해 데이터를 주고받을 때 어떤 형태로 주고 받을지 정의
    - 예측(Request, Response)
    - Pydantic의 BaseModel을 사용해서 정의. (Payload라고도 함)
- Application : 실제 로직이 담긴 부분, ML 모델이 예측/추론하는 곳
- Database : 데이터를 어딘가 저장하고, 데이터를 가지고 오면서 활용
- Config : 프로젝트의 설정 파일(Config) 저장


# 구현해야하는 기능
- TODO Tree 확장 프로그램 설치
- [ ] 해야할 것
- [x] 완료
- FIXME : FIXME

# 기능 구현
- [x] : FastAPI 서버 만들기
  - [x] : POST /predict : 예측을 진행한 후, PredictResponse
    - [x] : Response 저장. CSV, JSON 가능함. 여기선 DB에 저장
  - [x] : GET /predict : DB에 저장된 모든 PredictResponse 변환
  - [x] : GET /predict/{id} : id로 필터링해서 해당 id에 맞는 PredictResponse를 저장
- [x] : FastAPI가 띄워질 때, Model Load
- [x] : Config 설정
- [x] : DB 객체 만들기

# 참고
- DB는 SQLite3, 라이브러리는 SQLModel 사용

# SQLModel?
- FastAPI를 만든 사람이 만든 Python ORM(Object Relational Mapping)임.
- 객체를 DB Table에 저장하는 방식
- DB = Table에 데이터를 저장하고 불러올 수 있음.
- Session : DB의 연결을 관리하는 방식
  - 외식. 음식점에 가서 나올때까지를 하나의 Session으로 표현. Session 안에서 가게 입장, 주문, 식사 진행
  - Session 내에서 데이터를 추가/조회/수정할 수 있음 => POST/GET/PATCH
  - Transaction : 세션 내에서 일어나는 모든 활동. 트랜잭션이 완료되면 DB에 저장됨

## 코드 예시
```python
SQLModel.metadata.create_all(engine) : SQLModel로 정의된 모델(테이블)을 DB에 생성
- 처음 init할 때 DB Table을 생성
```

```python
with Session(engine) as session:
  ...
  result = ''
  session.add(result) # 새로운 객체를 세션에 추가. DB에 저장은 x
  session.commit() # 세션의 변경 사항을 DB에 저장
  session.refresh(result) # 세선에 있는 객체를 업데이트

  # 테이블에서 id를 기준으로 가져오고 싶다.
  session.get(DB Model, id)

  # 테이블에서 쿼리를 하고 싶다
  session.query(DB Model).all() # 모든 값을 가져오겠다.
```

# SQLite3
- 가볍게 사용할 수 있는 간단한 DB. 디버깅용!!