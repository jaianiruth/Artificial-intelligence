def is_safe(node, color, graph, assigned_colors):
    # Check if any neighbor has the same color
    for neighbor in graph[node]:
        if assigned_colors.get(neighbor) == color:
            return False
    return True

def color_map(graph, colors, nodes, index, assigned_colors):
    if index == len(nodes):
        return True # all regions are colored
        
    current_node = nodes[index]
    
    for c in colors:
        if is_safe(current_node, c, graph, assigned_colors):
            assigned_colors[current_node] = c
            # move to next node
            if color_map(graph, colors, nodes, index + 1, assigned_colors):
                return True
            # backtrack if we get stuck
            assigned_colors[current_node] = None
            
    return False

# Map of Australia
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}
colors = ['Red', 'Green', 'Blue']
nodes = list(graph.keys())
assigned = {}

if color_map(graph, colors, nodes, 0, assigned):
    print("Map Coloring Solution:")
    for region, color in assigned.items():
        print(region, "->", color)
else:
    print("No coloring possible")
