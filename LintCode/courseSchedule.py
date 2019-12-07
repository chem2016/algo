class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def __init__(self):
        pass

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        queue = []
        courses_indegree = {x: 0 for x in range(numCourses)}
        course_dict = {}
        
        # getting courses_indegree and their adv_courses in dict
        for prerequisite in prerequisites:
            if len(prerequisite) > 1:
                course1, course2 = prerequisite[0], prerequisite[1]
                courses_indegree[course1] += 1 
                if course2 in course_dict:
                    course_dict[course2].append(course1)
                else:
                    course_dict[course2] = [course1]

        for key, value in courses_indegree.items():
            if value == 0:
                queue.append(key)
        
        if len(queue) == 0:
            return False
        # bfs
        while(len(queue)):
            base_course = queue.pop(0)
            if base_course in course_dict:
                adv_courses = course_dict[base_course]
            else:
                continue
            for adv_course in adv_courses:
                courses_indegree[adv_course] -= 1
                if courses_indegree[adv_course] == 0:
                    queue.append(adv_course)
        
        for key, value in courses_indegree.items():   # check the indegree at the end, not the queue
            if value != 0:
                return False
        
        return True

solution = Solution()
result = solution.canFinish(3, [[0, 1], [2, 0]])
print(result)



