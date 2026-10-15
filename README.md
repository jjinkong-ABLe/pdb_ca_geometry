# pdb_ca_geometry

Python 3.11 이상 표준 라이브러리만 사용하는 생물정보학 CLI입니다. AI 도움을 받아 작성했으며 예제는 합성 자료입니다.

## 실행

```console
python pdb_ca_geometry.py examples/toy.pdb
python -m unittest -v
```

결과는 표준 출력으로 내보냅니다. 파일로 저장하려면 `> results.txt`를 붙이세요. 잘못된 입력은 오류 메시지와 종료 코드 2로 반환합니다.

## 5. PDB Cα geometry

Legacy 고정폭 PDB의 첫 모델, `ATOM`의 `CA`만 읽습니다. HETATM·mmCIF는 지원하지 않습니다. altloc 공백을 A보다 우선하고 다른 altloc은 제외합니다. chain ID·residue number·insertion code로 원자를 식별합니다. 각 chain의 파일상 연속 관측 Cα 거리와 전체 관측 Cα의 동일 가중 회전반경을 Å 단위로 계산합니다. 결손 잔기 사이 거리도 포함될 수 있어 결합 길이로 해석하면 안 됩니다. 동일 chain ID를 TER 뒤에서 다시 사용하는 구조는 지원하지 않습니다. 질량 가중 전체 원자 회전반경·구조 품질·기능·결합 친화도를 추정하지 않습니다.

[wwPDB 좌표 형식](https://www.wwpdb.org/documentation/file-format-content/format33/sect9.html)

