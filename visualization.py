import matplotlib.pyplot as plt

def visualize_deforestation_map(deforestation_map):
    plt.imshow(deforestation_map, cmap='gray')
    plt.title("Deforestation Map")
    plt.show()