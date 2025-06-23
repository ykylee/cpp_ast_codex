# Software Requirement Specification

This document derives the detailed software requirements from GitHub issues prefixed with `[CRS]`. The following items summarize issues #1 and #2.

## 기능 요구사항
1. 프로그램은 C/C++로 작성된 소스코드를 입력 받아 **Abstract Syntax Tree(AST)** 구조로 변환해야 한다.
   - 전체 코드를 분석하여 노드 간 계층 구조를 표현한다.
   - AST 구성은 *Pylint*의 트리 포맷을 참고한다.
2. 입력은 단일 파일뿐 아니라 폴더 단위로도 제공될 수 있다.
   - 폴더가 주어질 경우 하위의 모든 C/C++ 파일을 재귀적으로 탐색하여 하나의 통합 AST를 생성한다.
3. AST를 생성하는 과정에서 필요한 `libclang` 라이브러리는 사용자가 경로를 지정할 수 있어야 한다.

## 디자인 요구사항
1. 생성된 AST는 트리 이미지로 시각화되어야 한다.
   - Graphviz 등을 활용하여 PNG 형식으로 저장한다.
2. 명령줄 인터페이스로 입력 경로와 출력 파일명을 지정할 수 있어야 한다.
   - 추가 clang 인자를 전달하여 파서 동작을 세밀하게 조정할 수 있다.
