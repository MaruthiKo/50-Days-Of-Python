def gender_count(students):
    m_count = 0
    f_count = 0
    for i in students:
        if i.lower() == "male":
            m_count += 1
        else:
            f_count += 1
    return [('Male',m_count),('female',f_count)]

print(gender_count(['Male','female','female','male','female','Male']))