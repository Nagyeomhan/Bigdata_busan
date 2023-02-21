# schedule_img 폴더 설명 (이미지 파일)
- 웹에 유입되는 이미지 파일을 Airflow를 활용해 HDFS에 배치작업 구성 목적
- 메인 코드와 테스트 코드로 나누어 설명

---

### 메인 코드
1. main_schedulegood_sh.py
    <br>
    Flask 웹에 들어오는 이미지 파일들 중 good으로 판정된 이미지들을
    <br>
    Airflow와 쉘 스크립트를 활용하여 HDFS로 1일 1회 배치작업 하는 코드

2. main_schedulebad_sh.py
    <br>
    Flask 웹에 들어오는 이미지 파일들 중 bad로 판정된 이미지들을
    <br>
    Airflow와 쉘 스크립트를 활용하여 HDFS로 스케줄링 하기 위한 코드

---

### 테스트 코드
1. hdfscli_test.py
    <br>
    <a href="https://hdfscli.readthedocs.io/en/latest/api.html">WebHDFS API clients</a>
    <br>
    WebHDFS API client를 이용해서 DAG를 테스트해본 코드

2. sftpoperator_test.py
    <br>
    <a href="https://airflow.apache.org/docs/apache-airflow-providers-sftp/stable/connections/sftp.html">SFTP Operator</a>
    <br>
    Airflow의 SFTP Operator를 이용해서 DAG를 테스트해본 코드

3. sshoperator_test.py
    <br>
    <a href="https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/connections/ssh.html">SSH Operator</a>
    <br>
    Airflow의 SSH Operator를 이용해서 DAG를 테스트해본 코드

4. webhdfsoperator_test.py
    <br>
    <a href="https://github.com/mcarujo/twitter-scraper/blob/main/dags/twitter_furiagg_dag.py">WebHDFS Operator</a>
    <br>
    WebHDFS Operator 예제문을 활용해서 DAG를 테스트해본 코드

5. schedulegood_test.py
    <br>
    Flask 웹에 들어오는 이미지 파일들 중 good으로 판정된 이미지들을
    <br>
    Airflow를 이용하여 HDFS로 스케줄링 하기 위한 코드
    <br>
    거의 구현되었으나 명령어가 길어서 잘 작동 안 됨 → 쉘 스크립트로 해결

6. schedulebad_test.py
    <br>
    Flask 웹에 들어오는 이미지 파일들 중 bad로 판정된 이미지들을
    <br>
    Airflow를 이용하여 HDFS로 스케줄링 하기 위한 코드
    <br>
    거의 구현되었으나 명령어가 길어서 잘 작동 안 됨 → 쉘 스크립트로 해결