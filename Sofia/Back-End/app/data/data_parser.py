import pandas as pd
import app.data.score_calculator as sc

def get_marks(df, subjects, terms=[1, 2, 3, 4, 5, 6, 7, 8]):
    """
    Returns a data frame with marks for given subjects and terms for given schools

    Parameters
        ----------
        subjects : list of subjects ["History","Sinhala","English"]
        terms : list of terms from 1 to 9 [1,2]
                if not specified return marks for all the terms.
    """

    columns = []

    for subject in subjects:

        for term in terms:
            columns.append((subject + "_" + str(term)).rstrip())

    df = df[columns]

    return df


def get_demographics(df, features=["scholarship", "f_edu", "m_edu", "s_num", "s_edu", "tution"]):
    return df[features]


def get_lci(df):
    features = []

    for i in range(1, 21):
        features.append("Lci_" + str(i))

    df = df[features]

    return df


def put_missing_values(dataframe):
    dataframe.replace('-1', -1, inplace=True)
    dataframe.replace('#N/A', -1, inplace=True)
    dataframe.replace('', -1, inplace=True)
    dataframe.fillna(-1, inplace=True)
    return dataframe


def discretize_marks(dataframe, subjects, terms=[1, 2, 3, 4, 5, 6, 7, 8]):
    dataframe = dataframe.apply(pd.to_numeric, errors='ignore')

    columns = []

    for subject in subjects:
        for term in terms:
            columns.append(subject + "_" + str(term))

    for column in columns:
        grades = []
        marks = dataframe[column]
        for val in marks:
            if val >= 75:
                grades.append(1)
            elif 75 > val >= 65:
                grades.append(2)
            elif 65 > val >= 55:
                grades.append(3)
            elif 55 > val >= 40:
                grades.append(4)
            elif 40 > val >= 0:
                grades.append(5)
            else:
                grades.append(-1)

        grade_series = pd.Series(grades)
        dataframe[column] = grade_series

    return dataframe


def generate_dataset(df, subjects, discretize='no'):
    if discretize == 'no':
        df_marks = get_marks(df, subjects)
    else:
        df_marks = discretize_marks(get_marks(df, subjects), subjects)
    df_demo = get_demographics(df)
    df_lci = get_lci(df)

    df_join = df_marks.join(df_demo).join(df_lci)

    df = put_missing_values(df_join)  # replace missing values with -1

    for subject in subjects:
        tution_score = sc.getTutionScore(df, subject)
        tution_score_series = pd.Series(tution_score)
        df[subject + "_tution"] = tution_score_series
    df = df.drop('tution', axis=1)

    sibiling_score = sc.getSibilingEducationScore(df)
    sibiling_score_series = pd.Series(sibiling_score)
    df["s_edu"] = sibiling_score_series

    df = df.apply(pd.to_numeric, errors='ignore')

    # imp = Imputer(missing_values=-1, strategy='mean', axis=1)
    # df = pd.DataFrame(imp.fit_transform(df))

    return df


def df_to_numeric(dataframe):
    columns = list(dataframe)


def generate_dataset_orange(subject, tution_score="no", discretize='no'):
    features = [subject + "_1", subject + "_2", subject + "_3", subject + "_4", subject + "_5",
                subject + "_6", subject + "_7", subject + "_8", subject + "_9", "scholarship", "f_edu", "m_edu",
                "s_num", "s_edu",
                "tution", ]

    for i in range(1, 21):
        features.append("Lci_" + str(i))

    df = get_all()[features];
    df = handle_missing_values(df, '?');
    df = handle_missing_values(df, '?', is_nan=True)

    if (tution_score == "yes"):
        tution_score = sc.getTutionScore(df, subject)
        tution_score_series = pd.Series(tution_score)
        df["tution"] = tution_score_series;

    else:
        tution_category = sc.getTutionCategory(df, subject)
        tution_category_series = pd.Series(tution_category)
        df["tution"] = tution_category_series

    sibiling_score = sc.getSibilingEducationScore(df)
    sibiling_score_series = pd.Series(sibiling_score)
    df["s_edu"] = sibiling_score_series

    if (discretize == 'yes'):
        df = discretize_marks(df, subject)
        df.to_csv('out_dec.csv')
    else:
        df.to_csv('out.csv')


def isNaN(val):
    return val != val
