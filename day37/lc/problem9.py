# 690. Employee Importance


def getImportance(employees,id):
    mp={}
    for emp in employees:
        mp[emp.id]=emp
    def dfs(emp_id):
        emp=mp[emp_id]
        total=emp.importance
        for child in emp.subordinates:
            total+=dfs(child)
        return total
    return dfs(id)