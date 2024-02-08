from math import exp

feature_vector = [1, 0.85, 1, 1, 0]
weight_vector = [-1.2, 0.6, 3, 2.2, 1.4]
classes = ["not email", "email"]

wx = 0
for i in range(len(feature_vector)):
    wx += feature_vector[i] * weight_vector[i]

p = 1/(1+exp(-wx))
if p < 0.5:
    y = 0
else:
    y = 1

print(classes[y])