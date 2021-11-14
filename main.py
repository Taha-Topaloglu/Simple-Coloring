neighbours = {'1': ['2', '3'],
              '2': ['1', '3'],
              '3': ['2', '4'],
              '4': ['1', '3'],
              'T': []
              }
colors = dict()
for region in neighbours.keys():
    colors[region] = 'black'


def is_valid(colors):
    for region, region_neighbours in neighbours.items():
        for neighbour in region_neighbours:
            if (colors[neighbour] == colors[region]):
                return False
    return True


def print_map(colors):
    for region, color in colors.items():
        print(region + ':' + color)
    print()


def rec_coloring(colors, remaining_regions):
    # base condition
    if (len(remaining_regions) == 0):
        if (is_valid(colors)):
            print_map(colors)
        return
    # coloring case
    region = remaining_regions.pop()
    for color in ['red', 'green', 'blue']:
        colors[region] = color
        rec_coloring(colors, remaining_regions)
    remaining_regions.append(region)


remaining_regions = list(colors.keys())
rec_coloring(colors, remaining_regions)