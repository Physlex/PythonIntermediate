students = [
    dict(id = 0, credits = dict(math = 9, physics = 6, history = 7)),
    dict(id = 1, credits = dict(math = 2, physics = 6, history = 3)),
    dict(id = 3, credits = dict(math = 2, physics = 3, history = 7)),
    dict(id = 2, credits = dict(math = 1, physics = 4, history = 9)),
]   

def decorate(student:list)->tuple :
    global NUMCOURSES
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student) :
    return decorated_student[1]

decorated_students = list(map(decorate, students))
decorated_students.sort(reverse=True)
undecorated_students = list(map(undecorate, decorated_students))

print(list(map(print, undecorated_students)))
