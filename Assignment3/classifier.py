raw_data_set = []
structured_data_set = []
features = ["age", "sex", "cp_type", "rbp", "serum_chol", "fast_bls", "rest_ecg", "maxhr", "eia", "oldpeak", "slope", "num_vessels", "thal", "heart_disease"]

def ingest():
    f = open("heart.data", 'r')
    for line in f:
        line.rstrip()
        datapoints = line.split()
        raw_data_set.append(datapoints)
    for subject in raw_data_set:
        structured_line = []
        for point in subject:
            feature_name = features[subject.index(point)]
            structured_line.append(classifier(feature_name, point))
        structured_data_set.append(structured_line)

def classifier(feature, value):
    return {
        'age': 1 if float(value) > 50 else 0,
        'rbp': 1 if float(value) > 130 else 0,
        'serum_chol': 1 if float(value) > 250 else 0,
        'maxhr': 1 if float(value) > 120 else 0,
        'oldpeak': 1 if float(value) > 1 else 0,
        'sex': nominal_classifier(feature, value),
        'cp_type': nominal_classifier(feature, value),
        'fast_bls': nominal_classifier(feature, value),
        'rest_ecg': nominal_classifier(feature, value),
        'eia': nominal_classifier(feature, value),
        'slope': nominal_classifier(feature, value),
        'num_vessels': nominal_classifier(feature, value),
        'thal': nominal_classifier(feature, value),
        'heart_disease': 0 if float(value) == 1 else 1
    }[feature]

def nominal_classifier(feature, value):
    nominals = list(set(points[features.index(feature)] for points in raw_data_set))
    return nominals.index(value)

ingest()
print structured_data_set
