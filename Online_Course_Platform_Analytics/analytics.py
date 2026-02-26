from typing import Any

from data import courses
from collections import Counter



def get_all_progress_values(courses):

	score =  [students["progress"]
		  for course in courses
		  for students in course["students"]]
	return score

def get_unique_students(courses):
	name = [{students["name"]
			 for course in courses
			 for students in course["students"]}]
	return name
def get_students_above_75(courses):
	students_above_75 = [students["name"]
			 for course in courses
			 for students in course["students"] if  students["progress"]>75]
	return students_above_75

def get_course_titles(courses):
	course_titles = [{course["title"]
			 for course in courses}]

	return course_titles

def get_total_students(courses):
	total_students = [students["name"]
			 for course in courses
			 for students in course["students"]]
	total_count = len(total_students)

	return total_count

def get_students_progress_grester_than_80(courses):
	total_students = [students["name"]
			 for course in courses
			 for students in course["students"] if students["progress"] >= 80 ]


	return total_students


def get_students_category(courses):
	total_students = [students["name"]
			 for course in courses
			 for students in course["students"] if course["category"] == "Programming"]


	return total_students

def get_average_progress(courses):
	avg_progress_per_course = {
		course["title"]: sum(student["progress"] for student in course["students"]) / len(course["students"])
		for course in courses
	}
	return avg_progress_per_course


def num_stduents(courses):
	num_student={course["title"]: len(course["students"]) for course in courses}
	return num_student

def num_stduents_names(courses):
	num_student={course["title"]: student["name"] for course in courses for student in course["students"]}
	return num_student