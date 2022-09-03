# node_explorer_application

## Description
- PoS(Proof of Stake) Layer1, 2의 node&validator 현황을 종합적으로 확인할 수 있는 어플리케이션
- Layer 별 node&validator 수 및 현재 스테이킹 수익률, 예상 수익률 확인가능

## Structure
- Frontend : python vue, github action CI/CD을 통한 S3 정적 웹페이지 구성
- Backend : python flask 활용, github action CI/CD를 통한 도커 컨테이너 환경(ECR - ECS)
- Database : Mongodb(local)
- Terraform 활용한 인프라 리소스 관리

