# Software Requirement Specification

The following requirements were collected from GitHub issues with the `[SRS]` prefix.

## 기능
- C/C++ 로 작성된 코드를 읽어 AST 구조로 정리해야 한다.
  - Abstract Syntax Tree (AST) 구조로 코드 전체 내용을 정리한다.
  - AST 구성은 Pylint 구성을 참조한다.
  - 소스코드는 파일 단위 또는 폴더 단위로 입력한다.
  - 전체 소스코드를 분석하여 AST를 구성한다.

## 디자인
- 구성된 Tree를 이미지로 출력해야 한다.
  - AST를 생성하고 구성된 Tree를 이미지로 출력한다.
