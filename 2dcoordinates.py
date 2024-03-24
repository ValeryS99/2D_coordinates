
class Classifier:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def classify_point(self, predict, radius):
        min_distance = None
        nearest_class = None

        for key, value in self.data_dict.items():
            for point in value:
                distance = ((point[0] - predict[0]) ** 2 + (point[1] - predict[1]) ** 2) ** 0.5
                if min_distance is None or distance < min_distance:
                    min_distance = distance
                    nearest_class = key

        if min_distance is not None and min_distance <= radius:
            return nearest_class
        else:
            return "Unknown"

data_dict = {}

while True:
    x = int(input("Enter the coordinates of the point by the x value: "))
    y = int(input("Enter the coordinates of the point by the y value: "))
    obj_class = input("Enter the object class: ")

    if obj_class not in data_dict:
        data_dict[obj_class] = []

    data_dict[obj_class].append((x, y))

    response = input("Do you still want to add a point? Enter 'y' for yes, any other key to finish: ").lower()
    if response != 'y':
        break

unknown_x = int(input("Enter the x-coordinate of the unknown object: "))
unknown_y = int(input("Enter the y-coordinate of the unknown object: "))
predict = (unknown_x, unknown_y)

radius = int(input("Set the value of the radius of the nearest neighbors: "))

clf = Classifier(data_dict)
prediction = clf.classify_point(predict, radius)

print("The predicted class for the unknown object is:", prediction)
