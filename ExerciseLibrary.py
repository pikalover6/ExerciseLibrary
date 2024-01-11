import json

# Read the JSON data from the file
file_path = 'exercises.json'

with open(file_path, 'r', encoding='utf-8') as file:
    exercises_data = json.load(file)

class Exercise:
    def __init__(self, exercise_data):
        self.name = exercise_data['name']
        self.force = exercise_data['force']
        self.level = exercise_data['level']
        self.mechanic = exercise_data['mechanic']
        self.equipment = exercise_data['equipment']
        self.primary_muscles = exercise_data['primaryMuscles']
        self.secondary_muscles = exercise_data['secondaryMuscles']
        self.instructions = exercise_data['instructions']
        self.category = exercise_data['category']
        self.images = exercise_data['images']
        self.id = exercise_data['id']

    def __str__(self):
        return f"Exercise: {self.name}\nLevel: {self.level}\nCategory: {self.category}\nEquipment: {self.equipment}"

class ExerciseLibrary:
    def __init__(self):
        self.exercises = [Exercise(exercise_data) for exercise_data in exercises_data]

    def list_exercises(self):
        return [exercise.name for exercise in self.exercises]

    def find_exercises(self, name=None, muscle_group=None, equipment=None, level=None, category=None):
        results = self.exercises
        if name:
            results = [exercise for exercise in results if name.lower() in exercise.name.lower()]
        if muscle_group:
            results = [exercise for exercise in results if muscle_group.lower() in exercise.primary_muscles + exercise.secondary_muscles]
        if equipment:
            results = [exercise for exercise in results if equipment.lower() in exercise.equipment.lower()]
        if level:
            results = [exercise for exercise in results if level.lower() == exercise.level.lower()]
        if category:
            results = [exercise for exercise in results if category.lower() == exercise.category.lower()]
        return results

    def get_exercise_details(self, exercise_name):
        for exercise in self.exercises:
            if exercise_name.lower() == exercise.name.lower():
                return exercise
        # Try again
        for exercise in self.exercises:
            if "barbell " + exercise_name.lower() == exercise.name.lower():
                return exercise
        # Try again
        for exercise in self.exercises:
            if exercise_name.lower() in exercise.name.lower():
                return exercise
        # Try again, find similar
        for exercise in self.exercises:
            if exercise.name.lower() in exercise_name.lower():
                return exercise
        return None

    def suggest_random_exercise(self):
        import random
        return random.choice(self.exercises)