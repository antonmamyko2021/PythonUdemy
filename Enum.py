data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []
s = 'Shrub'
f = 'Flower'


for i in range(0, len(data)):
    if s in data[i]:
        shrubs.append(data[i].replace(" - Shrub",""))
    elif f in data[i]:
        flowers.append(data[i].replace(" - Flower", ""))

print("Your options for flowers are:" )
print(flowers)
print("Your options for shrubs are:")
print(shrubs)
# write your code here
