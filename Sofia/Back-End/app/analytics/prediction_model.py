import app.data.data_parser as dp
from sklearn.externals import joblib
import app.analytics.learning_prediction as lp

subjects = ["Mathematics", "Art", "Science", "Sinhala", "Citizenship_Education", "English", "Geography", "Health",
            "History", "PTS",
            "Religion"]


def get_prediction_marks(df1, df2, subject):
    xgb_regressor = joblib.load('app/analytics/joblibs/xgb/' + subject + '_xgb.joblib')
    adb_classifier = joblib.load('app/analytics/joblibs/adb_clf/' + subject + '_adb.joblib')
    rnd_classifier = joblib.load('app/analytics/joblibs/rnd_clf/' + subject + '_rnd.joblib')

    thresold = 55
    high_thresold = 97
    low_thresold = 9

    predict_mark = xgb_regressor.predict(df1)[0]

    if predict_mark > high_thresold:
        predict_mark = high_thresold

    if predict_mark < low_thresold:
        predict_mark = low_thresold

    if xgb_regressor.predict(df1) > thresold:
        return predict_mark, rnd_classifier.predict(df2)
    else:
        return predict_mark, adb_classifier.predict(df2)


def get_prediction(df):
    dict = {}
    for subject in subjects:
        df1 = dp.generate_dataset(df, [subject])
        df2 = dp.generate_dataset(df, [subject], discretize='yes')
        dict[subject] = get_prediction_marks(df1, df2, subject)

        dict["learning_style"] = lp.get_learning_styles(df)

        print(dict)

    return dict
