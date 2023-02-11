"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def find_importance(self, cur_id, employees):
        for i in range(len(employees)):
            if employees[i].id == cur_id:
                cur_employee = employees[i]

        if not cur_employee.subordinates:
            return cur_employee.importance

        cur_importance = cur_employee.importance
        for j in range(len(cur_employee.subordinates)):
            cur_importance += self.find_importance(cur_employee.subordinates[j], employees)
        
        return cur_importance

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        for i in range(len(employees)):
            if employees[i].id == id:
                return self.find_importance(id, employees)
    
        