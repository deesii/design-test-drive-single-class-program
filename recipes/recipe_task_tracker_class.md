# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

Assumptions:

You will be only to add one task at a time, when invoking a method of add that task..

Nouns: tasks, list
Verbs: keep track, add todo tasks, see , focus , mark as complete, disappear,



## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker():
    # User-facing properties (these are the things that the user interacting with the class and instances of the class will interact with):
    #   task: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   accessible by others --> therefore make private?
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def tasks_list(self):
        # Returns:
        #   a list of the tasks
        # Side-effects:
        #   sets the list of the tasks to the self object
        pass # No code here yet

    def mark_complete(self, task):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Throws an exception if no task is set
        #   sets the updated list to the self object
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task, I want to add it and view the task list

# no task inputted raises an exception
"""
task_tracker = TaskTracker()
task_tracker.add_task ("Walk the dog")
task_tracker.tasks_list() # => ["Walk the dog"]

# add_task raises an error with the message "No task set."

"""
Given multiple tasks added, I want to view the entire task list

"""
task_tracker = TaskTracker()
task_tracker.add_task ("Walk the dog")
task_tracker.add_task ("take the rubbish out")
task_tracker.tasks_list() # => ["Walk the dog", "take the rubbish out"]

# add_task raises an error with the message "No task set!"

"""
Given multiple tasks and then an empty string, as a task, there will be raised an exception saying that no task was inputteded 

"""
task_tracker = TaskTracker()
task_tracker.add_task ("Walk the dog")
task_tracker.add_task ("") # => "No task set!"

# add_task raises an exception with the message "No task set!"


"""
Given multiple tasks and then an empty string, as a task, viewed will not have that empty string

"""
task_tracker = TaskTracker()
task_tracker.add_task ("Walk the dog")
task_tracker.add_task ("") # => "No task set!"
task_tracker.tasks_list() #=> ["Walk the dog"]

# add_task raises an exception with the message "No task set!"


"""
Given multiple tasks being added, then completing a task that is on the list of tasks, then adding another task, then viewing the task list.

"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.add_task ("Wash the dishes")
task_tracker.add_task ("Go grocery shopping")
task_tracker.add_task ("Do the laundry")
task_tracker.mark_complete ("Go grocery shopping")
task_tracker.add_task ("Make carbonara")

task_tracker.tasks_list() # => ["Walk the dog", "Wash the dishes", "Do the laundry", "Make carbonara"]

"""
Given multiple tasks being added, then completing a task that is NOT on the list of tasks, it throws an exception

"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.add_task ("Wash the dishes")
task_tracker.add_task ("Go grocery shopping")
task_tracker.add_task ("Do the laundry")
task_tracker.mark_complete ("Go groce shopping") # => raises an exception to say "No task exists on your list!"

"""
Given multiple tasks being added, then completing a task that is NOT on the list of tasks, then viewing the task list, it has not removed anything!

"""
task_tracker = TaskTracker()
task_tracker.add_task("Walk the dog")
task_tracker.add_task ("Wash the dishes")
task_tracker.add_task ("Go grocery shopping")
task_tracker.add_task ("Do the laundry")
task_tracker.mark_complete ("Go groce shopping") # => raises an exception to say "No task exists on your list!"
task_tracker.add_task ("Make carbonara")



task_tracker.tasks_list() # => ["Walk the dog", "Wash the dishes", "Go grovery shopping", "Do the laundry", "Make carbonara"]


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
