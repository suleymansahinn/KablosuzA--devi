import matplotlib.pyplot as plt
import networkx as nx


G = nx.Graph()


G.add_node("ASA 5505", pos=(0, 3), device="firewall")
G.add_node("Router0", pos=(2, 2.5), device="router")
G.add_node("Switch0", pos=(0, 2), device="switch")
G.add_node("Switch1", pos=(-2, 1), device="switch")
G.add_node("Switch2", pos=(0, 1), device="switch")
G.add_node("Switch3", pos=(2, 1), device="switch")
G.add_node("Switch4", pos=(4, 1), device="switch")
G.add_node("Switch5", pos=(6, 1), device="switch")
G.add_node("PC0", pos=(-2, 0), device="pc")
G.add_node("PC1", pos=(-1, 0), device="pc")
G.add_node("PC2", pos=(0, 0), device="pc")
G.add_node("PC3", pos=(1, 0), device="pc")
G.add_node("PC4", pos=(2, 0), device="pc")
G.add_node("PC5", pos=(3, 0), device="pc")
G.add_node("PC6", pos=(4, 0), device="pc")
G.add_node("PC7", pos=(5, 0), device="pc")
G.add_node("PC8", pos=(6, 0), device="pc")
G.add_node("PC9", pos=(7, 0), device="pc")
G.add_node("Server0", pos=(4, 2), device="server")


G.add_edge("ASA 5505", "Router0")
G.add_edge("ASA 5505", "Switch0")
G.add_edge("Switch0", "Switch1")
G.add_edge("Switch0", "Switch2")
G.add_edge("Switch0", "Switch3")
G.add_edge("Switch0", "Switch4")
G.add_edge("Switch0", "Switch5")
G.add_edge("Switch1", "PC0")
G.add_edge("Switch1", "PC1")
G.add_edge("Switch2", "PC2")
G.add_edge("Switch2", "PC3")
G.add_edge("Switch3", "PC4")
G.add_edge("Switch3", "PC5")
G.add_edge("Switch4", "PC6")
G.add_edge("Switch4", "PC7")
G.add_edge("Switch5", "PC8")
G.add_edge("Switch5", "PC9")
G.add_edge("Switch0", "Server0")


pos = nx.get_node_attributes(G, 'pos')


color_map = []
for node in G:
    if G.nodes[node]['device'] == 'router':
        color_map.append('red')
    elif G.nodes[node]['device'] == 'switch':
        color_map.append('blue')
    elif G.nodes[node]['device'] == 'pc':
        color_map.append('green')
    elif G.nodes[node]['device'] == 'server':
        color_map.append('orange')
    elif G.nodes[node]['device'] == 'firewall':
        color_map.append('purple')


nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=1000, font_size=6, font_color='black')


plt.title("Network Topology")
plt.show()
