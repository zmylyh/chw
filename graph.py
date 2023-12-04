graph = {
    '西塱站': {'坑口站': 2},
    '坑口站': {'西塱站': 2, '花地湾站': 3},
    '花地湾站': {'坑口站': 3, '芳村站': 1},
    '芳村站': {'花地湾站': 1, '黄沙站': 4},
    '黄沙站': {'芳村站': 4, '长寿路站': 5},
    '长寿路站': {'黄沙站': 5, '陈家祠站': 5},
    '陈家祠站': {'长寿路站': 5, '西门口站': 4},
    '西门口站': {'陈家祠站': 4, '公园前站1': 2},
    '公园前站1': {'西门口站': 2, '农讲所站': 3, '公园前站2': 10, '公园前站': 0},
    '农讲所站': {'公园前站1': 3, '烈士陵园站': 3},
    '烈士陵园站': {'农讲所站': 3, '东山口站': 5},
    '东山口站': {'烈士陵园站': 5, '杨箕站': 5},
    '杨箕站': {'东山口站': 5, '体育西路站1': 3},
    '体育西路站1': {'杨箕站': 3, '体育中心站': 5, '体育西路站3': 10, '体育西路站': 0},
    '体育中心站': {'体育西路站1': 5, '广州东站1': 5},
    '广州南站': {'石壁站': 4},
    '石壁站': {'广州南站': 4, '会江站': 3},
    '会江站': {'石壁站': 3, '南浦站': 5},
    '南浦站': {'会江站': 5, '洛溪站': 2},
    '洛溪站': {'南浦站': 2, '南洲站': 4},
    '南洲站': {'洛溪站': 4, '东晓南站': 3},
    '东晓南站': {'南洲站': 3, '江泰路站': 4},
    '江泰路站': {'东晓南站': 4, '昌岗站': 3},
    '昌岗站': {'江泰路站': 3, '江南西站': 3},
    '江南西站': {'昌岗站': 3, '市二宫站': 4},
    '市二宫站': {'江南西站': 4, '海珠广场站': 4},
    '海珠广场站': {'市二宫站': 4, '公园前站2': 1},
    '公园前站2': {'海珠广场站': 1, '纪念堂站': 1, '公园前站1': 10, '公园前站': 0},
    '纪念堂站': {'公园前站2': 1, '越秀公园站': 1},
    '越秀公园站': {'纪念堂站': 1, '广州火车站': 3},
    '广州火车站': {'越秀公园站': 3, '三元里站': 3},
    '三元里站': {'广州火车站': 3, '飞翔公园站': 3},
    '飞翔公园站': {'三元里站': 3, '白云公园站': 4},
    '白云公园站': {'飞翔公园站': 4, '白云文化广场站': 3},
    '白云文化广场站': {'白云公园站': 3, '萧岗站': 3},
    '萧岗站': {'白云文化广场站': 3, '江夏站': 1},
    '江夏站': {'萧岗站': 1, '黄边站': 2},
    '黄边站': {'江夏站': 2, '嘉禾望岗站2': 1},
    '嘉禾望岗站2': {'黄边站': 1, '嘉禾望岗站3': 10, '嘉禾望岗站': 0},
    '天河客运站': {'五山站': 2},
    '五山站': {'天河客运站': 2, '华师站': 5},
    '华师站': {'岗顶站': 5, '五山站': 5},
    '岗顶站': {'石牌桥站': 4, '华师站': 5},
    '石牌桥站': {'体育西路站3': 3, '岗顶站': 4},
    '体育西路站3': {'珠江新城站': 3, '石牌桥站': 3, '体育西路站1': 10, '林和西站': 2, '体育西路站': 0},
    '珠江新城站': {'广州塔站': 2, '体育西路站3': 3},
    '广州塔站': {'客村站': 3, '珠江新城站': 2},
    '客村站': {'大塘站': 3, '广州塔站': 3},
    '大塘站': {'沥滘站': 5, '客村站': 3},
    '沥滘站': {'厦滘站': 3, '大塘站': 5},
    '厦滘站': {'大石站': 4, '沥滘站': 3},
    '大石站': {'汉溪长隆站': 2, '厦滘站': 4},
    '汉溪长隆站': {'市桥站': 3, '大石站': 2},
    '市桥站': {'番禺广场站': 4, '汉溪长隆站': 3},
    '番禺广场站': {'市桥站': 4},
    '机场北站': {'机场南站': 4},
    '机场南站': {'高增站': 4, '机场北站': 4},
    '高增站': {'人和站': 5, '机场南站': 4},
    '人和站': {'龙归站': 3, '高增站': 5},
    '龙归站': {'嘉禾望岗站': 1, '人和站': 3},
    '嘉禾望岗站3': {'白云大道北站': 2, '龙归站': 1, '嘉禾望岗站2': 10, '嘉禾望岗站': 0},
    '白云大道北站': {'永泰站': 3, '嘉禾望岗站': 2},
    '永泰站': {'同和站': 4, '白云大道北站': 3},
    '同和站': {'京溪南方医院站': 3, '永泰站': 4},
    '京溪南方医院站': {'梅花园站': 3, '同和站': 3},
    '梅花园站': {'燕塘站': 3, '京溪南方医院站': 3},
    '燕塘站': {'广州东站3': 5, '梅花园站': 3},
    '广州东站3': {'林和西站': 5, '燕塘站': 5, '广州东站1': 10, '广州东站': 0},
    '广州东站1': {'体育中心站': 5, '广州东站3': 10, '广州东站': 0},
    '林和西站': {'体育西路站3': 2, '广州东站3': 5},
    '广州东站': {'广州东站3': 0, '广州东站1': 0},
    '公园前站': {'公园前站1': 0, '公园前站2': 0},
    '体育西路站': {'体育西路站1': 0, '体育西路站3': 0},
    '嘉禾望岗站': {'嘉禾望岗站2': 0, '嘉禾望岗站3': 0}
}

graph2 = graph.copy()
del graph2['广州东站']
del graph2['公园前站']
del graph2['体育西路站']
del graph2['嘉禾望岗站']
graph2.update({'广州东站3': {'林和西站': 5, '燕塘站': 5, '广州东站1': 10}})
graph2.update({'广州东站1': {'体育中心站': 5, '广州东站3': 10}})
graph2.update({'公园前站1': {'西门口站': 2, '农讲所站': 3, '公园前站2': 10}})
graph2.update({'公园前站2': {'海珠广场站': 1, '纪念堂站': 1, '公园前站1': 10}})
graph2.update({'体育西路站1': {'杨箕站': 3, '体育中心站': 5, '体育西路站3': 10}})
graph2.update({'体育西路站3': {'珠江新城站': 3, '石牌桥站': 3, '林和西站': 2, '体育西路站1': 10}})
graph2.update({'嘉禾望岗站2': {'黄边站': 1, '嘉禾望岗站3': 10}})
graph2.update({'嘉禾望岗站3': {'白云大道北站': 2, '龙归站': 1, '嘉禾望岗站2': 10}})


def dijkstra(graph, start, end):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, weight in destinations.items():
            weight = weight + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return formatprint(path)


def formatprint(l):
    restr = ''
    totalt = sum([graph.get(i).get(l[l.index(i) + 1]) for i in l[:-1]])
    for i in l[:-1]:
        restr += i + ' - ' + str(graph.get(i).get(l[l.index(i) + 1])) + ' - '
    return restr + l[-1], totalt