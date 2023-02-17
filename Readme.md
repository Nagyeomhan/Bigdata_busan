# 크로메이트 도금 양불 판정 서비스 개발 프로젝트
<br>
프로젝트 목적 : 크로메이트 도금 제품의 정상·불량 판정 웹 서비스 구현
<br>
프로젝트 기간 : 약 3개월
<br>
<br>
# 프로젝트 전체 구조
<br>
<img width="682" alt="image" src="https://user-images.githubusercontent.com/108378151/218929701-16ac2769-8b41-45f3-8c99-67842c52c2cb.png">
<br>
**이 중 데이터 수집·저장·관리 파트를 담당했습니다.**
<br>
1. Git 폴더 구성
<br>
(1) DL : 위 그림의 Deep Learning 파트
<br>
(2) ML : 공정환경변수 csv 파일 양불 판정 머신러닝 관련 (데이터로 유의미한 상관관계가 도출되지 못했기 때문에 위 그림에서는 생략되었습니다)
<br>
(3) web : 위 그림의 양불 판정 웹서비스 파트
<br>
(4) **hng : 위 그림의 데이터 수집 저장 관리 파트**
<br>
<br>
2. hng 폴더 상세
<br>
(1) schedule_img > main_schedulegood_sh.py : 양품으로 판정된 이미지 데이터를 1일 1회 HDFS의 good 폴더에 적재하도록 구성된 DAG
<br>
(2) schedule_img > main_schedulebad_sh.py : 불량품으로 판정된 이미지 데이터를 1일 1회 HDFS의 bad 폴더에 적재하도록 구성된 DAG
<br>
(3) schedule_var > main_schedulevar.py : 공정환경변수 csv 파일을 전처리를 거쳐서 1일 1회 MySQL에 적재하도록 구성된 DAG
<br>
(4) schedule_var > main_scheduleerr.py : 에러발생로트 csv 파일을 전처리를 거쳐서 1일 1회 MySQL에 적재하도록 구성된 DAG
<br>
(5) schedule_var > main_labelmodel.py : 공정환경변수 파일에 에러발생로트를 라벨링할 수 있도록 MySQL에서 var과 err 내역을 추출하여
<br>
1주 1회 MySQL에 라벨링작업 후 적재되도록 구성된 DAG
<br>
<br>
# 데이터 수집 저장 관리 파트 설명
<br>
<img width="801" alt="image" src="https://user-images.githubusercontent.com/108378151/218930620-190b6297-0686-4d1e-a7d1-ec49f5a0b169.png">
<img width="676" alt="image" src="https://user-images.githubusercontent.com/108378151/218931493-3aae7dfe-a2e8-458e-8a97-28e6adec7815.png">
<br>
워크플로우 배치 관리 툴로 Airflow를 도입하여 1일 1회 배치 작업을 관리했습니다.
<br>
* Flask -> HDFS  : 웹에 업로드되는 이미지 파일 저장
<br>
* Flask -> MySQL : 웹에 업로드되는 공정환경변수 csv 파일 저장
