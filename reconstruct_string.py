ef reconstruct_string(k, d, paired_reads):
    # Create a paired de Bruijn graph
    graph = create_paired_de_bruijn_graph(paired_reads)

    path = find_eulerian_path(graph)

    reconstructed_string = reconstruct_from_path(path, k, d)

    return reconstructed_string

def create_paired_de_bruijn_graph(paired_reads):
    graph = {}
    for paired_read in paired_reads:
        kmer1, kmer2 = paired_read.split('|')
        prefix = kmer1[:-1] + '|' + kmer2[:-1]
        suffix = kmer1[1:] + '|' + kmer2[1:]
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
    return graph

def find_eulerian_path(graph):
    # Find an Eulerian path using Hierholzer's algorithm
    path = []
    stack = []
    current_node = list(graph.keys())[0]  # Start from any node

    while True:
        if graph.get(current_node):
            stack.append(current_node)
            next_node = graph[current_node].pop()
            current_node = next_node
        else:
            path.append(current_node)
            if stack:
                current_node = stack.pop()
            else:
                break

    # Reverse the path to get the correct order
    path.reverse()
    return path

def reconstruct_from_path(path, k, d):
    # Reconstruct the string from the Eulerian path
    reconstructed_string = path[0]

    for i in range(1, len(path)):
        kmer = path[i].split('|')
        reconstructed_string += kmer[1][-1]

    return reconstructed_string

k = 4
d = 2
paired_reads = ["GAGA|TTGA", "TCGT|GATG", "CGTG|ATGT", "TGGT|TGAG", "GTGA|TGTT", "GTGG|GTGA", "TGAG|GTTG", "GGTC|GAGA", "GTCG|AGAT"]

result = reconstruct_string(k, d, paired_reads)

print(result)
