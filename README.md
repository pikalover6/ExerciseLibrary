### Documentation for `ExerciseLibrary`

```python
import ExerciseLibrary
```

#### Overview
`ExerciseLibrary` is a Python library designed to interact with a dataset of physical exercises. It allows users to list exercises, search for specific exercises, retrieve detailed information about an exercise, and get random exercise suggestions.

#### Class: Exercise
This class represents a single exercise entry.

**Attributes:**
- `name`: String. The name of the exercise.
- `force`: String. The type of force (push/pull) involved in the exercise.
- `level`: String. Difficulty level of the exercise (e.g., beginner, intermediate).
- `mechanic`: String. The type of mechanics involved (compound/isolation).
- `equipment`: String. The equipment required for the exercise.
- `primary_muscles`: List. Primary muscles targeted by the exercise.
- `secondary_muscles`: List. Secondary muscles targeted by the exercise.
- `instructions`: List. Step-by-step instructions for performing the exercise.
- `category`: String. The category of the exercise (e.g., strength, stretching).
- `images`: List. URLs or paths to images demonstrating the exercise.
- `id`: String. Unique identifier for the exercise.

#### Class: ExerciseLibrary
This class encapsulates the functionalities for managing and querying the exercise data.

**Methods:**
1. `__init__(self)`: Initializes the ExerciseLibrary with a list of exercises.

2. `list_exercises(self)`: Returns a list of all exercise names.
    - **Returns**: List of strings. Names of all exercises.

3. `find_exercises(self, name=None, muscle_group=None, equipment=None, level=None, category=None)`: Searches for exercises based on specified criteria.
    - `name`: String (optional). Name of the exercise to search for.
    - `muscle_group`: String (optional). Muscle group to search for.
    - `equipment`: String (optional). Equipment to search for.
    - `level`: String (optional). Difficulty level to search for.
    - `category`: String (optional). Category to search for.
    - **Returns**: List of `Exercise` objects matching the criteria.

4. `get_exercise_details(self, exercise_name)`: Retrieves detailed information about a specific exercise.
    - `exercise_name`: String. The name of the exercise.
    - **Returns**: `Exercise` object if found, else `None`.

5. `suggest_random_exercise(self)`: Suggests a random exercise.
    - **Returns**: An `Exercise` object chosen randomly.

#### Example Usage
```python
import ExerciseLibrary

def main():
    # Initialize the ExerciseLibrary
    exercise_lib = ExerciseLibrary.ExerciseLibrary()

    # List all exercises
    all_exercises = exercise_lib.list_exercises()
    print("List of All Exercises:")
    for exercise in all_exercises:
        print(exercise)

    # Find exercises for a specific muscle group
    muscle_group = "neck"
    back_exercises = exercise_lib.find_exercises(muscle_group=muscle_group)
    print(f"\nExercises for {muscle_group.capitalize()}:")
    for exercise in back_exercises:
        print(exercise.name)

    # Get details of a specific exercise
    exercise_name = "Deadlift"
    deadlift_details = exercise_lib.get_exercise_details(exercise_name)
    if deadlift_details:
        print(f"\nDetails of {exercise_name}:")
        print(f"Name: {deadlift_details.name}")
        print(f"Force: {deadlift_details.force}")
        print(f"Level: {deadlift_details.level}")
        print(f"Mechanic: {deadlift_details.mechanic}")
        print(f"Equipment: {deadlift_details.equipment}")
        print(f"Primary Muscles: {', '.join(deadlift_details.primary_muscles)}")
        print(f"Secondary Muscles: {', '.join(deadlift_details.secondary_muscles)}")
        print(f"Instructions: {', '.join(deadlift_details.instructions)}")
        print(f"Category: {deadlift_details.category}")
        print(f"Images: {', '.join(deadlift_details.images)}")
    else:
        print(f"{exercise_name} not found in the library.")

    # Suggest a random exercise
    random_exercise = exercise_lib.suggest_random_exercise()
    print(f"\nRandom Exercise Suggestion: {random_exercise.name}")

if __name__ == "__main__":
    main()
```
