# schedule_var 폴더 설명 (공정환경변수 파일)
- 웹에 유입되는 공정환경변수 파일을 Airflow를 활용해 MySQL에 ETL 목적
- 메인 코드와 테스트 코드로 나누어 설명

---

### 메인 코드
1. main_schedulevar.py
    공정환경변수 csv 파일들을 Airflow를 이용하여
    <br>
    전처리 작업을 거친 후 MySQL로 스케줄링 하기 위한 코드

2. main_scheduleerr.py
    에러발생로트 csv 파일들을 Airflow를 이용하여
    <br>
    전처리 작업을 거친 후 MySQL로 스케줄링 하기 위한 코드

3. main_labelmodel.py
    MySQL에 저장해둔 공정환경변수 및 에러발생로트 내역을 불러와서
    <br>
    원활한 모델링이 가능하도록 라벨링해주는 작업을
    <br>
    1주 1회 Airflow를 이용하여 실행한 후 MySQL로 스케줄링 하기 위한 코드

---

## 테스트 코드
1. sql_input_test.py
    Airflow를 활용한 MySQL 적재 작업이 실행되는지 테스트한 코드