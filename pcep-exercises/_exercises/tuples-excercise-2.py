connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

trips = 0
sum = 0.0

for city in connections:
    if city[0] == 'Amsterdam':
        trips += 1
        sum += city[2] # city[2] refers to the minutes above
print(trips, 'connections lead to', connections[0][0], 'with an average flight time of', sum/trips, 'minutes')