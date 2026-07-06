# 변경 이력

이 프로젝트의 버전별 변경 사항을 기록합니다. 버전은 유의적 버전(SemVer)을 따릅니다.

## [1.0] - 2026-07-05

첫 공식 릴리스.

### 사이트 (`docs/`, 라이브: https://airoasting-image.vercel.app)
- 7가지 품질 원칙과 7블록 프롬프트 템플릿
- 프롬프트 도움창(빌더)
- 10개 카테고리 · 100개 선별 레퍼런스 갤러리

### 번들 스킬 (`SKILL.md`, `references/`, `scripts/`, `hooks/`)
- 7원칙 프롬프트 설계 규칙과 10개 카테고리 라우팅
- 레퍼런스 라이브러리: 10개 카테고리 파일(각 10개, 사이트 갤러리 100개와 1:1) + 작성 규칙(`gpt-image-prompt-craft.md`) + 변주 레시피(`gpt-image-variation-recipes.md`)
- 품질 도구: 규칙 검증기(`scripts/check_prompt.py`), 생성물 위 글자 후처리 차단 훅(`hooks/gpt-image-block-text-overlay.sh`), 실측 채점(`experiments/`)
- 비개발자 비즈니스 리더용 설치 안내

### 라이선스
- Apache License 2.0
