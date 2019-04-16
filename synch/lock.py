'''
A basic mutex. 

This works with each drone throughout the pipeline (ie across processes) rather than 
across threads like the mutexes provided in the Python standard library.
'''

class Lock():
    def __init__(self):
        self.sema = 1 # 1 means available, 0 means taken
        self.holder = None # will be replaced with id of holder when taken

    # Attempts to acquire the lock if possible.
    # _id is the id of the drone attempting to acquire it
    # Returns true if successful, false otherwise
    def lock_try_acquire(self, _id):
        if self.sema:
            self.sema = 0
            self.holder = _id
            return True
        return False

    # Acquires the lock. If it can't be acquired immediately,
    # busy wait until the lock is available. 
    # Returns None upon completion
    def lock_acquire(self, _id):
        while not self.lock_try_acquire(_id):
            pass
        return None

    # Releases the lock.
    # the _id passed in must match the current holder of the lock
    # Returns true if successful, false otherwise
    def lock_release(self, _id):
        if self.holder == _id:
            self.sema = 1
            self.holder = None
            return True
        return False

    # Returns true if lock is being held by drone with _id, false otherwise
    def lock_held_by_drone(self, _id):
        return self.holder == _id

