from graphviz import Graph

g = Graph(name='Undirected', ## 그래프 이름
          comment='basic', ## 코멘트 소스 텍스트 첫 번째 줄에 표시됨.
          filename='boj2630', ## 파일 이름
          format='png', ## 파일 형식
          directory='./', ## 파일 저장 디렉토리
          )
g.node(name='A') ## 노드 A 생성, g.node('A')와 동일
g.node(name='B') ## 노드 B 생성, g.node('B')와 동일
g.node(name='C') ## 노드 C 생성, g.node('B')와 동일
 
g.edge(tail_name='A', head_name='B') ## edge 생성, g.edge('A', 'B')와 동일
g.edge(tail_name='B', head_name='C') ## edge 생성, g.edge('A', 'B')와 동일
## g.edges(['AC', 'BC'])과 동일
 
g.view() ## 사전에 정의한 format으로 저장 및 파일 열기
print(g.source) ## 소스 텍스트 출력