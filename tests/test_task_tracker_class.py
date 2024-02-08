from lib.task_tracker_class import *
import pytest

"""
Given a task, I want to add it and view the task list

# no task inputted raises an exception
"""
def test_task_add_view_list():
    task_tracker = TaskTracker()
    task_tracker.add_task ("Walk the dog")
    assert task_tracker.tasks_list() == ["Walk the dog"]

    # add_task raises an error with the message "No task set."

"""
Given multiple tasks added, I want to view the entire task list

"""

def test_track_multiple_tasks_added_and_viewed():
    task_tracker = TaskTracker()
    task_tracker.add_task ("Walk the dog")
    task_tracker.add_task ("take the rubbish out")
    assert task_tracker.tasks_list() == ["Walk the dog", "take the rubbish out"]

# add_task raises an error with the message "No task set!"

"""
Given multiple tasks and then an empty string, as a task, there will be raised an exception saying that no task was inputteded 

"""
def test_multiple_tasks_one_task_no_string_exception_viwed():
    task_tracker = TaskTracker()
    task_tracker.add_task ("Walk the dog")
    with pytest.raises(Exception) as e:
        task_tracker.add_task("")
    error_message = str(e.value)
    assert error_message == "No task set!"
    assert task_tracker.tasks_list() == ["Walk the dog"]
    # add_task raises an exception with the message "No task set!"


"""
Given multiple tasks being added, then completing a task that is on the list of tasks, then adding another task, then viewing the task list.

"""
def test_multiple_tasks_added_completed_mark_disappear():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task ("Wash the dishes")
    task_tracker.add_task ("Go grocery shopping")
    task_tracker.add_task ("Do the laundry")
    task_tracker.mark_complete ("Go grocery shopping")
    task_tracker.add_task ("Make carbonara")

    assert task_tracker.tasks_list() == ["Walk the dog", "Wash the dishes", "Do the laundry", "Make carbonara"]


"""
Given multiple tasks being added, then completing a task that is NOT on the list of tasks, it throws an exception

"""

def test_multiple_tasks_added_mark_complete_task_not_on_list():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task ("Wash the dishes")
    task_tracker.add_task ("Go grocery shopping")
    task_tracker.add_task ("Do the laundry")
    with pytest.raises(Exception) as e:
        task_tracker.mark_complete ("Go groce shopping") # => raises an exception to say "No task exists on your list!"
    error_message = str(e.value)
    assert error_message == "No task exists on your list!"

"""
Given multiple tasks being added, then completing a task that is NOT on the list of tasks, then viewing the task list, it has not removed anything!

"""
def test_multiple_added_mark_complete_task_view():
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task ("Wash the dishes")
    task_tracker.add_task ("Go grocery shopping")
    task_tracker.add_task ("Do the laundry")
    with pytest.raises(Exception) as e:
        task_tracker.mark_complete ("Go groce shopping") # => raises an exception to say "No task exists on your list!"
    error_message = str(e.value)
    task_tracker.add_task ("Make carbonara")
    assert error_message == "No task exists on your list!"

    assert task_tracker.tasks_list() == ["Walk the dog", "Wash the dishes", "Go grocery shopping", "Do the laundry", "Make carbonara"]

#if test by index for mark_complete, then tests to have would be if index < 0, and > length of the list.