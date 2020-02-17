import pickle

def get_learning_styles(lci_df):
    lci_df = lci_df.apply(calculate_lci_sums, axis=1)

    lci_df = lci_df.apply(calculate_lci_percentages, axis=1)

    lci_df = lci_df[["technical_%", "confluence_%", "precision_%", "sequence_%"]]

    init_model = pickle.load(open('app/analytics/models/learningstyle.model', 'rb'), encoding='latin1')

    return init_model.predict(lci_df)[0]





def calculate_lci_sums(items):
    question_info = {
        "sequence": ["Lci_1", "Lci_5", "Lci_9", "Lci_13", "Lci_17"],
        "precision": ["Lci_2", "Lci_6", "Lci_10", "Lci_14", "Lci_18"],
        "technical": ["Lci_3", "Lci_7", "Lci_11", "Lci_15", "Lci_19"],
        "confluence": ["Lci_4", "Lci_8", "Lci_12", "Lci_16", "Lci_20"]
    }

    for category in question_info:
        category_list = question_info[category]

        # Get non missing values
        category_scores = [int(items[key]) for key in category_list if (-1 < int(items[key]) <= 6)]

        # Adjust for missing value
        items[category] = (sum(category_scores) / len(category_scores)) * len(category_list)

    items["lci_sum"] = int(items["sequence"]) + int(items["precision"]) + int(items["technical"]) + int(
        items["confluence"])

    return items


def calculate_lci_percentages(items):
    question_info = {
        "sequence": ["1", "5", "9", "13", "17"],
        "precision": ["2", "6", "10", "14", "18"],
        "technical": ["3", "7", "11", "15", "19"],
        "confluence": ["4", "8", "12", "16", "20"]
    }

    # Calculate percentage for each category against total score

    for category in question_info:
        items[str(category) + "_%"] = (items[category] / items["lci_sum"]) * 100

    return items


def calculate_lci_missing(items):
    question_info = {
        "sequence": ["1", "5", "9", "13", "17"],
        "precision": ["2", "6", "10", "14", "18"],
        "technical": ["3", "7", "11", "15", "19"],
        "confluence": ["4", "8", "12", "16", "20"]
    }

    for category in question_info:
        category_list = question_info[category]
        for key in category_list:
            if (int(items[key]) < -1):
                items[key] = items[category] / len(category_list)
    return items

