from binary_classification import classifyBinary

feature_vector = [1, 0.85, 1, 1, 0]
weight_vector = [-1.2, 0.6, 3, 2.2, 1.4]
classes = ["not email", "email"]

print(classifyBinary(feature_vector, weight_vector, classes))
