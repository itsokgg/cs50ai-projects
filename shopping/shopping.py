import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # removed "VisitorType", "Month", and "Weekend" from type_ints as they are handled seperatly
    type_ints = ["Administrative", "Informational", "ProductRelated",
                 "OperatingSystems", "Browser", "Region", "TrafficType"]
    type_floats = ["Administrative_Duration", "Informational_Duration", "ProductRelated_Duration",
                   "BounceRates", "ExitRates", "PageValues", "SpecialDay"]
    # "June" is spelled with all letters in csv; not "Jun"
    months = {"Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3, "May": 4, "June": 5,
              "Jul": 6, "Aug": 7, "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11}

    evidence = []
    labels = []
    with open("shopping.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            e = []
            for column in row:
                if column in type_ints:
                    e.append(int(row[column]))
                elif column in type_floats:
                    e.append(float(row[column]))
                elif column == "Month":
                    e.append(months[row[column]])
                elif column == "VisitorType":
                    if row[column] == "Returning_Visitor":
                        e.append(1)
                    else:
                        e.append(0)
                elif column == "Weekend":
                    if row[column] == "FALSE":
                        e.append(False)
                    else:
                        e.append(True)
                elif column == "Revenue":
                    if row[column] == "FALSE":
                        labels.append(0)
                    else:
                        labels.append(1)
            evidence.append(e)

    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    return model.fit(evidence, labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    correct0 = 0
    correct1 = 0
    total0 = 0
    total1 = 0
    for actual, predicted in zip(labels, predictions):
        if actual == 0:
            total0 += 1
            if actual == predicted:
                correct0 += 1

        else:
            total1 += 1
            if actual == predicted:
                correct1 += 1
            
    sensitivity = correct1 / total1
    specificity = correct0 / total0
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
