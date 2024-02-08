class TaskTracker():
    # User-facing properties (these are the things that the user interacting with the class and instances of the class will interact with):
    #   task: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   accessible by others --> therefore make private?
        self._tracker_list = []
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object

        if task == "":
            raise Exception("No task set!")
        else:
            return self._tracker_list.append(task)
        #self.tracker_list.append(task)

    def tasks_list(self):
        # Returns:
        #   a list of the tasks
        # Side-effects:
        #   sets the list of the tasks to the self object
        return self._tracker_list


    def mark_complete(self, task): # improvement if delete by index not task
        # Returns:
        #   Nothing
        # Side-effects:
        #   Throws an exception if no task is set
        #   sets the updated list to the self object
        if task not in self._tracker_list: 
            raise Exception("No task exists on your list!")
        
        else:
            self._tracker_list.remove(task) #if by index you can delete it from list with del self._tasks[index]
        
        