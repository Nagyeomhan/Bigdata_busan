# 크로메이트 도금 양불 판정 서비스 개발 프로젝트

1. 프로젝트 목적 : 크로메이트 도금 제품의 정상·불량 판정 웹 서비스 구현
2. 프로젝트 기간 : 2022.10 ~ 2022.12 (약 3개월)
3. 프로젝트 멤버 : 데이터시스템 1명, 모델러 1명, 백엔드 1명, 프론트엔드 1명
4. 사용 데이터 : <a href='https://www.kamp-ai.kr/front/dataset/AiDataDetail.jsp?AI_SEARCH=&page=2&DATASET_SEQ=25&EQUIP_SEL=&GUBUN_SEL=&FILE_TYPE_SEL=&WDATE_SEL='>[인공지능 중소벤처 제조 플랫폼 KAMP] 크로메이트 AI 데이터셋</a>
5. 개발 환경<br>
(1) 주요 개발 언어 : Python<br>
(2) 모델링 및 학습 : Google Colab GPU<br>
(3) Flask 및 데이터 파이프라인 서버 : AWS EC2 Ubuntu 22.04
<br>

## 프로젝트 전체 구조
<br>
<img width="800" alt="image" src="https://user-images.githubusercontent.com/108378151/218929701-16ac2769-8b41-45f3-8c99-67842c52c2cb.png">

**이 중 데이터 수집·저장·관리 파트를 주로 담당하였고** 머신러닝 작업도 일부 담당<br>

* Git 폴더 구성<br>
(1) DL : 위 그림의 Deep Learning 파트<br>
(2) **ML : 공정환경변수 csv 파일 양불 판정 머신러닝 관련 (위 그림에서는 생략)**<br>
(3) web : 위 그림의 양불 판정 웹서비스 파트<br>
(4) **hng : 위 그림의 데이터 수집 저장 관리 파트**<br><br>

* ML 폴더 상세<br>
트리 기반 모델을 탐색하기 위한 코드 구현

| 상위 폴더   | 파일 이름                | 작업 내용 설명 |
| ------     | ----                     | -------       | 
| hng_PREPRO | hng_PREPRO_TOTAL.ipynb   | EDA, 하이퍼파라미터 탐색, 모델 탐색이 가능하도록 구성한 코드 | 
<br>

* hng 폴더 상세<br>
표에 설명된 파일 이외에는 전부 테스트를 위한 코드

| 상위 폴더     | 파일 이름                | 작업 내용 설명 |
| ------       | ----                    | -------       | 
| schedule_img | main_schedulegood_sh.py | 양품 판정 이미지 파일을 HDFS의 good 폴더에 적재하도록 구성된 DAG |
| schedule_img | main_schedulebad_sh.py  | 불량 판정 이미지 파일을 HDFS의 bad 폴더에 적재하도록 구성된 DAG |
| schedule_var | main_schedulevar.py     | 공정환경변수 csv 파일을 전처리를 거쳐 MySQL에 적재하도록 구성된 DAG |
| schedule_var | main_scheduleerr.py     | 에러발생로트 csv 파일을 전처리를 거쳐 MySQL에 적재하도록 구성된 DAG |
| schedule_var | main_labelmodel.py      | 공정환경변수 파일에 에러발생로트를 라벨링할 수 있도록 MySQL에서 var과 err 내역을 추출하여 1주 1회 라벨링 작업 후 MySQL에 적재되도록 구성된 DAG |
<br>

## 데이터 수집 저장 관리 파트 설명
<img width="800" alt="image" src="https://user-images.githubusercontent.com/108378151/218930620-190b6297-0686-4d1e-a7d1-ec49f5a0b169.png">
<img width="800" alt="image" src="https://user-images.githubusercontent.com/108378151/218931493-3aae7dfe-a2e8-458e-8a97-28e6adec7815.png">

**워크플로우 배치 관리 툴로 Airflow를 도입하여 1일 1회 배치 작업을 관리**

* Flask → HDFS  : 웹에 업로드되는 이미지 파일 저장
* Flask → MySQL : 웹에 업로드되는 공정환경변수 csv 파일 저장
