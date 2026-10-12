import numpy as np

q = np.array([1, 2, 0, 0, 0, 0])
d1 = np.array([6, 12, 0, 0, 0, 0])
d2 = np.array([2, 4, 0, 0, 0, 0])
d3 = np.array([3, 6, 0, 0, 0, 0])
d4 = np.array([0, 0, 1, 1, 0, 0])

documents = [d1, d2, d3, d4]

for i, d in enumerate(documents, start=1):
    sim = np.dot(q, d) / (np.linalg.norm(q) * np.linalg.norm(d))
    print(f"sim(q, d{i}) = {sim:.2f}")

sim = np.dot(q, d1) / (np.linalg.norm(q) * np.linalg.norm(d1))

# d1, d2, d3:
# same direction as q → cosine similarity = 1
# d4:
# orthogonal to q → cosine similarity = 0
