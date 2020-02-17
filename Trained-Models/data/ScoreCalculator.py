def getTutionScore(dataframe, subject):
    scores = []
    tution_list = dataframe["tution"]
    tution_list = tution_list.tolist()

    for entry in tution_list:
        score = 0

        if(entry != -1):

            entry = entry.split(",")

            for sub in entry:

                if(sub.strip()[:2].lower() == subject[:2].lower()):
                    try:
                        score = int(sub[-3]) + int(sub[-2]) + int(sub[-1])
                    except:
                        score = 3
                else:
                    continue

            scores.append(score)

        else:
            scores.append(score)

    return scores

def getSibilingEducationScore(dataframe):
    scores = []
    sibilings_list = dataframe["s_edu"]
    sibilings_list = sibilings_list.tolist()

    for entry in sibilings_list:
        score = 0

        if(entry != -1):

            if(len(entry) != 1):
                entry = entry.split(",")

                for i in range(0,len(entry)):
                    if(entry[i] != ''):
                        score = score + int(entry[i])

                scores.append(score+1)

            else:
                score = int(entry)
                scores.append(score)

        else:
            scores.append(score)

    return scores;

def getLCIScore(dataframe):
    return 0;


def getExtraActivitiesScore(dataframe):
    return 0;

def getTutionCategory(dataframe, subject):
    categories = []
    tution_list = dataframe["tution"]
    tution_list = tution_list.tolist()

    for entry in tution_list:
        category = "0"

        if(entry != '?'):
            entry = entry.split(",")

            for sub in entry:

                if(sub.strip()[:2].lower() == subject[:2].lower()):
                    if(len(sub.split("_"))>1):
                        category = sub.split("_")[-1]

                else:
                    continue

            categories.append(category)

        else:
            categories.append(category)

    return categories


def getExtraActivitiesCategory(dataframe):
    return 0;