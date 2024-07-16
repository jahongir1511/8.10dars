#  https://www.codewars.com/kata/58a08e622e7fb654a300000e/train/python

def sort_grades(lst):
    grade_order = ['VB', 'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13',
                   'V14', 'V15', 'V16', 'V17']

    grade_to_position = {grade: index for index, grade in enumerate(grade_order)}

    sorted_grades = sorted(lst, key=lambda grade: grade_to_position[grade])

    return sorted_grades


# Example usage
grades = ['V3', 'VB', 'V2', 'V0+', 'V5', 'V1']
print(sort_grades(grades))

