# node_explorer_application

## Description
- PoS(Proof of Stake) Layer1, 2의 node&validator 현황을 종합적으로 확인할 수 있는 어플리케이션
- Layer 별 node&validator 수 및 현재 스테이킹 수익률, 예상 수익률 확인가능

## Structure
- python flask, vue 
- github action 도커 컨테이너 환경 CI/CD 구축(AWS ECS, ECR)
- Mongodb
- Terraform 활용한 인프라 리소스 관리

## Database
- MongoDB
- DB name : explorer_session_db
- collection name : explorer_collection

### Data
![image](https://user-images.githubusercontent.com/89952061/188305139-741ca731-22f2-46d5-ae6c-3fb71e7ac178.png)
- session_ip : 사용자 ip 주소
- access_time : 접속 시간
```
docker run \
    --name mongodb \
    -d \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=root \
    -e MONGO_INITDB_ROOT_PASSWORD=root \
    mongo
```

## Environment Variable
- username (mongodb username)
- password (mongodb passwd)
- ip_address (mongodb host)
