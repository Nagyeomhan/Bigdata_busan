# 나의 작업
- Airflow를 활용해서 배치 작업 파이프라인을 구축했습니다 
- Flask -> HDFS 파이프라인
- Flask -> MySQL 파이프라인

---

### 폴더 설명
1. airflow_study : 팀원들과 스터디를 할 때 Airflow에 대해 설명한 내용
2. plugins : Airflow의 plugins 폴더에 저장하고 사용한 파일(hook, operator, sensor)
3. schedule_img : 웹에 유입되는 이미지 파일을 Airflow를 활용해 HDFS에 배치작업 구성 목적
    - 세부 내용은 schedule_img > about_schedule_img.md 참고
4. schedule_var : 웹에 유입되는 공정환경변수 파일을 Airflow를 활용해 MySQL에 ETL 목적
    - 세부 내용은 schedule_var > about_schedule_var.md 참고

---

### 파일 설명
1. sixdogma_img_input.ipynb
    <br>
    초기 원천 데이터 중 이미지 파일을 blob 형식으로 변환해서 MySQL에 저장한 코드
2. sixdogma_var_input.ipynb
    <br>
    초기 원천 데이터 중 공정환경변수 및 에러발생로트 파일을 MySQL에 저장한 코드
3. flask_test.ipynb
    <br>
    flask에서 HDFS에 저장된 이미지를 불러올 수 있도록 다양한 사항 테스트
4. labeltest.ipynb
    <br>
    schedule_var > main_labelmodel 작업을 실행할 수 있도록 테스트
5. testcode.ipynb
    <br>
    MySQL 스케줄러, upsert 기능, 그리고 csv 파일을 스파크로 열 수 있게 테스트