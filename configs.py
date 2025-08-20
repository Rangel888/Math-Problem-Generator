import ujson

class Config:
    def __init__(self, filepath):

        # Load configs from JSON
        with open(filepath, 'r') as f:
            data = ujson.load(f)
        
        # Set attributes with defaults if keys 
        self.number_of_problems = data.get('numberOfProblems', 5)
        self.use_division_remainders = data.get('useDivisionRemainders', False)



