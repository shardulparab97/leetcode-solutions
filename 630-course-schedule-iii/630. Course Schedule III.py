# class Solution:
#     # heap and queue combination 
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
#         courses.sort(key = lambda x: x[1])

#         pq = []
#         total_duration = 0

#         for duration, last_day in courses:
#             heapq.heappush(pq, -duration)
#             total_duration += duration

#             if last_day < total_duration:
#                 days_to_be_removed = heapq.heappop(pq)
#                 total_duration += -1*days_to_be_removed

#         return len(pq)

from typing import List, Set
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Prioritize adding those courses with earlier last days
        # to collection of courses taken.
        # Think about the last day as an expiry date of courses.
        courses_sorted_by_last_day = sorted(courses, key=lambda course: course[1])

        durations_of_courses_taken = []

        total_duration = 0

        for course in courses_sorted_by_last_day:
            duration = course[0]
            last_day = course[1]
            # Keep the course with longest duration ready to be popped out
            # when we run out of time for completing all courses before their respective deadlines
            # i.e. total duration exceeded the last day of the newly added course
            heapq.heappush(durations_of_courses_taken, -duration)
            total_duration += duration

            if total_duration > last_day:
                # oops!
                # we have exceeded the deadline by having added
                # one more too lengthy course.
                # Let's remove the one with the longest duration
                # to make maximum space for adding new courses in future.
                duration_of_removed_course = heapq.heappop(durations_of_courses_taken)
                total_duration += duration_of_removed_course


        # Let's return the number of courses remaining in our collection
        # of courses taken after having iterated through all possible choice
        # of courses available to be taken.
        return len(durations_of_courses_taken)
