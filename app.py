cell = (5, 5)

neighbors_cells = []
for i in range(-1, 2):
    for j in range(-1, 2):
        neighbors_cells.append((cell[0]+i, cell[0]+j))
        
neighbors_cells.remove(cell)
print(neighbors_cells)