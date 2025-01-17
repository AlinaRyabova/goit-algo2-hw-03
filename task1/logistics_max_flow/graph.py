import networkx as nx

def build_graph():
    G = nx.DiGraph()

    # Додавання ребер з пропускною здатністю
    edges = [
        ("Terminal 1", "Warehouse 1", 25),
        ("Terminal 1", "Warehouse 2", 20),
        ("Terminal 1", "Warehouse 3", 15),
        ("Terminal 2", "Warehouse 3", 15),
        ("Terminal 2", "Warehouse 4", 30),
        ("Terminal 2", "Warehouse 2", 10),
        ("Warehouse 1", "Shop 1", 15),
        ("Warehouse 1", "Shop 2", 10),
        ("Warehouse 1", "Shop 3", 20),
        ("Warehouse 2", "Shop 4", 15),
        ("Warehouse 2", "Shop 5", 10),
        ("Warehouse 2", "Shop 6", 25),
        ("Warehouse 3", "Shop 7", 20),
        ("Warehouse 3", "Shop 8", 15),
        ("Warehouse 3", "Shop 9", 10),
        ("Warehouse 4", "Shop 10", 20),
        ("Warehouse 4", "Shop 11", 10),
        ("Warehouse 4", "Shop 12", 15),
        ("Warehouse 4", "Shop 13", 5),
        ("Warehouse 4", "Shop 14", 10),
    ]

    # Додавання ребер до графа
    for edge in edges:
        G.add_edge(edge[0], edge[1], capacity=edge[2])

    # Додамо штучні джерело та стік
    G.add_node("SuperSource")
    G.add_node("SuperSink")

    # Зв'язок SuperSource із терміналами
    G.add_edge("SuperSource", "Terminal 1", capacity=float("inf"))
    G.add_edge("SuperSource", "Terminal 2", capacity=float("inf"))

    # Зв'язок магазинів із SuperSink
    for shop in ["Shop 1", "Shop 2", "Shop 3", "Shop 4", "Shop 5",
                 "Shop 6", "Shop 7", "Shop 8", "Shop 9", "Shop 10",
                 "Shop 11", "Shop 12", "Shop 13", "Shop 14"]:
        G.add_edge(shop, "SuperSink", capacity=float("inf"))

    return G


def find_max_flow(G, source, sink):
    flow_value, flow_dict = nx.maximum_flow(G, source, sink)
    return flow_value, flow_dict


if __name__ == "__main__":
    # Побудова графа
    G = build_graph()

    # Пошук максимального потоку між штучними вершинами
    source = "SuperSource"
    sink = "SuperSink"

    max_flow, flow_distribution = find_max_flow(G, source, sink)

    print("Максимальний потік у системі логістики:", max_flow)
    print("\nРозподіл потоку:")
    for node, flows in flow_distribution.items():
        print(node, "->", flows)
