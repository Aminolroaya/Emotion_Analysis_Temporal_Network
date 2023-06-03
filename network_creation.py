import dill
import networkx as nx

# directed graph
G = nx.DiGraph()

# Create network the weight of nodes and width of edges are based on frequency
def create_network(all_emotions):

    for ticket_emotions in all_emotions:

        last_emotion_index = len(ticket_emotions) -1

        for i in range(0, last_emotion_index):

            # if node does not exist add
            if G.has_node(ticket_emotions[i] + str(i))==False:
                G.add_node(ticket_emotions[i] + str(i))
                G.nodes[ticket_emotions[i] + str(i)]['WeightNode'] = 1

            if G.has_node(ticket_emotions[i+1] + str(i+1))==False:
                G.add_node(ticket_emotions[i+1] + str(i+1))
                G.nodes[ticket_emotions[i+1] + str(i+1)]['WeightNode'] = 1

            # only increase the weight of last emotion node if already exist
            elif i + 1 == last_emotion_index:
                G.nodes[ticket_emotions[i+1] + str(i+1)]['WeightNode'] += 1

            # Add edges to the graph
            if G.has_edge(ticket_emotions[i] + str(i), ticket_emotions[i + 1] + str(i + 1)) == False:
                G.add_edge(ticket_emotions[i] + str(i), ticket_emotions[i + 1] + str(i + 1), WeightEdge=0.1)

            else:
                # increase weight of edge if exist
                G[ticket_emotions[i] + str(i)][ticket_emotions[i + 1] + str(i + 1)]['WeightEdge'] +=0.1
    return G

def plot_network(G):
    #using NetworkX for saving the network
    edge_weight = list(nx.get_edge_attributes(G, 'WeightEdge').values())
    node_weight = list(nx.get_node_attributes(G, 'WeightNode').values())
    nx.draw_networkx(G, width=edge_weight,node_size =node_weight)
    nx.write_gexf(G, "EmotionGraph.gexf")

if __name__ == '__main__':
    # Loading data
    file_name = "emotions.pkl"
    open_file = open(file_name, "rb")
    all_emotions = dill.load(open_file)
    plot_network(create_network(all_emotions))
