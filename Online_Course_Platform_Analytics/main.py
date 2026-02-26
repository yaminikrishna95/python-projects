
from data import courses
import analytics

if __name__ == "__main__":
	print(analytics.get_all_progress_values(courses))
	print(analytics.get_unique_students(courses))
	print(analytics.get_students_above_75(courses))
	print(analytics.get_course_titles(courses))
	print(analytics.get_total_students(courses))
	print(analytics.get_average_progress(courses))
	print(analytics.get_students_progress_grester_than_80(courses))
	print(analytics.get_students_category(courses))
	print(analytics.num_stduents(courses))
	print(analytics.num_stduents_names(courses))
