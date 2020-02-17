import pandas as pd
from score_calculators import ScoreCalculator as sc
from imblearn.over_sampling import SMOTE
import os

def get_all(schools=["sirisaman","southland"]):
    """
        Returns a data frame with all the features for given schools
    """
    dirname = os.path.dirname(__file__)

    files = [];

    for school in schools:
        files.append(school + "_full.csv");

    path = os.path.join(dirname, "../Data/");

    dataframes = [];

    for file in files:

        df = pd.read_csv(path+file);

        dataframes.append(df);

    merged_df = dataframes[0];

    for dataframe in dataframes[1:]:
        merged_df = merged_df.append(dataframe);

    return merged_df;

def get_marks(subjects, schools=["sirisaman","southland"], terms = [1,2,3,4,5,6,7,8,9], index = "yes"):

    """
    Returns a data frame with marks for given subjects and terms for given schools

    Parameters
        ----------
        subjects : list of subjects ["History","Sinhala","English"]
        schools : list of schools ["Sirisaman","Southland"]
        terms : list of terms from 1 to 9 [1,2]
                if not specified return marks for all the terms.
        index : {'yes','no'} adds index number of the student for the data frame
    """
    dirname = os.path.dirname(__file__)

    files = [];

    for school in schools:
        files.append(school + "_full.csv");

    path = os.path.join(dirname, "../Data/");

    if(index == 'yes'):
        columns = ['Index No.'];

    elif(index == 'no'):
        columns = [];

    for subject in subjects :

        columns.append(subject)

        for term in terms:
            if(term > 1):
                columns.append(subject + "." + str(term-1));

    dataframes = [];

    for file in files:

        df = pd.read_csv(path+file, usecols=columns);

        dataframes.append(df);

    merged_df = dataframes[0];

    for dataframe in dataframes[1:]:
        merged_df = merged_df.append(dataframe);

    return merged_df;

def get_demographics(schools=["sirisaman","southland"],features=["scholarship","f_edu","m_edu","s_num","s_edu","tution"], index="yes"):
    df = get_all(schools);

    if (index == "yes"):
        features.insert(0,"Index No.");

    return  df[features];

def get_lci(schools=["sirisaman","southland"], index="yes"):
    df = get_all(schools);

    features = []

    if(index == "yes"):
        features=["Index No."];

    for i in range(1,21):
        features.append("Lci_"+str(i));

    return  df[features];

def handle_missing_values(dataframe, how='0', is_nan = False):

    """
    Manages absent values in a data frame

    Parameters
        ----------
        dataframe : dataframe to be modified
        how : {'fill_0', 'fill_prev_avg', 'fill_this_avg', 'drop'}
    """
    if(not(is_nan)):

        if(how == '0'):
             dataframe.replace(-1, 0, inplace=True);

        elif(how == '?'):
            dataframe.replace(-1, '?', inplace=True);

    #     elif(how == 'fill_prev_avg'):
    #         # put previous average here for the subject
    #
    #     elif(how == 'fill_this_avg'):
    #         # put average mark for this term
    #
        elif(how == 'drop'):
             columns = list(dataframe.columns.values);

             for column in columns:
                dataframe = dataframe[dataframe[column] != 0]

    else :

        if (how == '0'):
            dataframe.fillna(0, inplace=True);

        elif (how == '-1'):
            dataframe.fillna(-1, inplace=True);

        elif (how == '?'):
            dataframe.fillna('?', inplace=True);
            # dataframe.astype(object).fillna('?', inplace=True);

        #     elif(how == 'fill_prev_avg'):
        #         # put previous average here for the subject
        #
        #     elif(how == 'fill_this_avg'):
        #         # put average mark for this term
        #
        elif (how == 'drop'):
            dataframe.dropna(inplace=True);

    return dataframe;

def discretize_marks(dataframe, subject):

    subjects = [subject];

    for i in range(1,9):
        subjects.append(subject+"."+str(i))

    for sub in subjects:
        grades=[]
        marks = dataframe[sub]
        for val in marks:
            if val != '?':
                if val >= 75:
                    grades.append('A')
                elif (val < 75 and val >= 65):
                    grades.append('B')
                elif (val < 65 and val >= 55):
                    grades.append('C')
                elif (val < 55 and val >=40):
                    grades.append('S')
                elif (val < 40 and val >= 0):
                    grades.append('F')
                    
        grade_series = pd.Series(grades)
        dataframe[sub] = grade_series

    return dataframe;



def generate_dataset_orange(subject, tution_score = "no", discretize = 'no'):

    features = ["Index No.", subject, subject + ".1", subject + ".2", subject + ".3", subject + ".4", subject + ".5",
                subject + ".6", subject + ".7", subject + ".8", "scholarship", "f_edu", "m_edu", "s_num", "s_edu",
                "tution", ]

    for i in range(1, 21):
        features.append("Lci_" + str(i));

    df = get_all()[features];
    df = handle_missing_values(df, '?');
    df = handle_missing_values(df, '?', is_nan=True);

    if(tution_score == "yes"):
        tution_score = sc.getTutionScore(df, subject);
        tution_score_series = pd.Series(tution_score);
        df["tution"] = tution_score_series;

    else:
        tution_category = sc.getTutionCategory(df, subject)
        tution_category_series = pd.Series(tution_category)
        df["tution"] = tution_category_series

    sibiling_score = sc.getSibilingEducationScore(df);
    sibiling_score_series = pd.Series(sibiling_score);
    df["s_edu"] = sibiling_score_series;

    if(discretize == 'yes'):
        df = discretize_marks(df,subject)
        df.to_csv('out_dec.csv')
    else:
        df.to_csv('out.csv')

def isNaN(val):
    return val != val

generate_dataset_orange(subject="Mathematics",tution_score = "no", discretize="yes")
generate_dataset_orange(subject="Mathematics",tution_score = "no", discretize="no")
    
            

