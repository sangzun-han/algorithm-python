fr_info = {
  'Summer': ['John','Justin','Mike'],
  'John' :['Summer','Justin'],
  "Justin" : ['John','Summer','Mike','May'],
  "Mike" : ['Summer','Justin'],
  "May": ['Justin','Kim'],
  'Kim' :['May'],
  'Tom': ["Jerry"],
  'Jerry' :['Tome']
 }

graph_info = {
  1 : [2,3],
  2 : [1,4,5],
  3 : [1],
  4 : [2],
  5 : [2]
}

 # 친구의 친구 찾기
def print_all_frineds(g,start):
  qu = []
  done = set()

  qu.append(start)
  done.add(start)

  while qu:
    p = qu.pop(0)
    print(p)
    for x in g[p]:
      if x not in done:
        qu.append(x)
        done.add(x)

# 친구 친밀도 계산
def print_all_frineds(g,start):
  qu = []
  done = set()

  qu.append((start,0))
  done.add(start)

  while qu:
    (p,d) = qu.pop(0)
    print(p,d)
    for x in g[p]:
      if x not in done:
        qu.append((x,d+1))
        done.add(x)

# 그래프 탐색
def search_graph(g,start):
  qu = []
  done = set()

  qu.append(start)
  done.add(start)

  while qu:
    p = qu.pop(0)
    print(p)
    for x in g[p]:
      if x not in done:
        qu.append(x)
        done.add(x)