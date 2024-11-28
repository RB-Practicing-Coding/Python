### This a swallow copy
# Create a list of colors
warmtones = ['brown', 'yellow', 'red', 'green', 'blue']

print(warmtones) # ['brown', 'yellow', 'red', 'green', 'blue']

palette = warmtones

print(palette) # ['brown', 'yellow', 'red', 'green', 'blue']

palette[0] = 'Q'

print(palette) # ['Q', 'yellow', 'red', 'green', 'blue']
print(warmtones) # ['Q', 'yellow', 'red', 'green', 'blue']

warmtones[1] = 'W'

print(palette) # ['Q', 'W', 'red', 'green', 'blue']
print(warmtones) # ['Q', 'W', 'red', 'green', 'blue']


### This is a deep copy
warmtones = ['brown', 'yellow', 'red', 'green', 'blue']
palette = list(warmtones) # Create a deep copy

print(palette) # ['brown', 'yellow', 'red', 'green', 'blue']

palette[0] = 'Q'

print(palette) # ['Q', 'yellow', 'red', 'green', 'blue']
print(warmtones) # ['brown', 'yellow', 'red', 'green', 'blue']

warmtones[1] = 'W'

print(palette) # ['Q', 'yellow', 'red', 'green', 'blue']
print(warmtones) # ['brown', 'W', 'red', 'green', 'blue']