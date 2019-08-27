import pandas as pd

# Math Test
math_ans = pd.read_csv("https://raw.githubusercontent.com/youmin817/Data_Analysis/master/dashboard_app/ACT_Math_Answer_Key").T

header = math_ans.iloc[0]
math_ans = math_ans[1:]
math_ans = math_ans.rename(columns=header)
math_ans.index = range(50)


sd_ans=pd.read_csv("https://raw.githubusercontent.com/youmin817/Data_Analysis/master/dashboard_app/P01_Answers.csv").T
header=sd_ans.iloc[0]
sd_ans = sd_ans[1:51]
sd_ans = sd_ans.rename(columns=header)
sd_ans.index = range(0, 50)


def math_grader(math_ans,sd_ans,sd_id):
    index = []
    for num in range(len(math_ans["Key"])):
        record = []
        # checking answers
        ans = math_ans.iloc[num,0]
        if sd_ans.loc[num,sd_id] == ans:
            record.append(True)
            index.append(record)
        else:
            record.append(False)
            index.append(record)
    result = pd.DataFrame(index, columns = ["Grade"])
    math_ans['Grade'] = result['Grade']
    grade = pd.DataFrame(math_ans['Grade'].value_counts())
    grade["Ans"] = ["Right", 'Wrong']
    math_ans.loc[math_ans['Grade'] == True, "Grade"] = "Right"
    math_ans.loc[math_ans['Grade'] == False, "Grade"] = "Wrong"
    return math_ans, grade


def math_table(math_ans,sd_ans ,sd_id):
    math_result, grade_table = math_grader(math_ans,sd_ans,sd_id)
    math = pd.DataFrame(sd_ans[sd_id])
    math['Ans_Key'] = math_result['Key']
    math["Grade"] = math_result["Grade"]
    return math, grade_table
