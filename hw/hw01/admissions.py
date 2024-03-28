# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True

# define your functions here
def convert_row_type(lst):

    new_list = []
    for i in lst:
        if type(i) is not float:
            num = float(i)
            new_list.append(num)
    return new_list

def calculate_score(lst):

    sat = (lst[0] / 160) * 0.3
    gpa = (lst[1] * 2) * 0.4
    int = lst[2] * 0.1
    curr = lst[3] * 0.2
    score = sat + gpa + int + curr
    return score

def is_outlier(lst):

    norm_sat = (lst[0] / 160)
    norm_gpa = (lst[1] * 2)
    if lst[2] == 0:
        return True
    elif norm_gpa - norm_sat > 2:
        return True
    else:
        return False

def calculate_score_improved(lst):
    if is_outlier(lst) or calculate_score(lst) >= 6:
        return True
    else:
        return False

def grade_outlier(lst):
    sorted_lst=sorted(lst)
    if sorted_lst[1] - sorted_lst[0] > 20:
        return True
    return False

def grade_improvement(lst):
    new_list = lst[:]
    new_list.sort()
    if new_list == lst:
        return True
    else:
        return False

def check_composite(score, grade):
    if is_outlier(score):
        return True
    elif grade_outlier(grade):
        return True
    elif grade_improvement(grade):
        return True
    else:
        return False
def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()

    # TODO: loop through the rest of the file

    for line in input_file:
        curr_line = line.split(",")
        string_scores = [curr_line[i] for i in range(len(curr_line)) if i > 0]
        name = curr_line[0]
        num_scores = convert_row_type(string_scores)
        scores = num_scores[:4]
        grades = num_scores[4:]
        overall_score = calculate_score(scores)
        outlier = is_outlier(scores)
        grade_out = grade_outlier(grades)
        improvement = grade_improvement(grades)


        if overall_score >= 6:
            with open("chosen_students.csv", "a") as outfile:
                outfile.write(f"{name}\n")

        if overall_score >= 6 or outlier and overall_score >= 5:
            with open("chosen_improved.csv", 'a') as outfile:
                outfile.write(f'{name}\n')

        with open("student_scores.csv", 'a') as outfile:
            outfile.write(f"{name},{overall_score:.2f}\n")

        if calculate_score_improved(scores):
            with open("better_improved.csv" ,'a') as outfile:
                outfile.write(f"{name},{scores[0]},{scores[1]},{scores[2]},{scores[3]}\n")

        if outlier:
            with open("outliers.csv", 'a') as outfile:
                outfile.write(f"{name}\n")

        if overall_score >= 6.0:
            with open("composite_chosen.csv", 'a') as outfile:
                outfile.write(f"{name}\n")
        elif overall_score >= 5.0 and check_composite(scores,grades):
            with open("composite_chosen.csv", 'a') as outfile:
                outfile.write(f"{name}\n")

        print(f"{name},{overall_score:.2f}")


    # TODO: make sure to close all files you've opened!
    input_file.close()
    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
