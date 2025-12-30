import threading


class ThreadSafeSingleton:
    """
    A thread-safe singleton implementation.
    Only one instance of this class can exist.
    """
    # Class-level variable to store the single instance
    _instance = None

    # Class-level lock to ensure thread safety
    _lock = threading.Lock()

    def __new__(cls):
        """
        Override __new__ method for thread-safe singleton implementation.
        """
        # Acquire the lock to ensure thread safety
        with cls._lock:
            # Check if instance has been created yet
            if not cls._instance:
                # Create the single instance of the class
                cls._instance = super().__new__(cls)
            # Return the single instance
            return cls._instance

    def __init__(self):
        """
        Initialize the singleton instance.
        Note: This will be called every time the class is instantiated,
        but __new__ ensures only one instance exists.
        """
        pass


# Example usage
if __name__ == "__main__":
    # Create multiple instances
    s1 = ThreadSafeSingleton()
    s2 = ThreadSafeSingleton()
    s3 = ThreadSafeSingleton()

    # Verify they are all the same instance
    print(f"s1 id: {id(s1)}")
    print(f"s2 id: {id(s2)}")
    print(f"s3 id: {id(s3)}")
    print(f"s1 is s2: {s1 is s2}")
    print(f"s2 is s3: {s2 is s3}")

    # Test with multiple threads
    instances = []


    def create_instance():
        instance = ThreadSafeSingleton()
        instances.append(instance)


    threads = [threading.Thread(target=create_instance) for _ in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Verify all instances are the same
    print(f"\nAll instances from threads are identical: {all(inst is instances[0] for inst in instances)}")