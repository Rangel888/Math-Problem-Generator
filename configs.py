import ujson

class Config:
    def __init__(self, filepath):

        # Load configs from JSON
        with open(filepath, 'r') as f:
            data = ujson.load(f)
        
        # Set attributes with defaults if keys 
        self.number_of_problems = data.get('numberOfProblems', 5)
        
        self.use_division_remainders = data.get('useDivisionRemainders', False)

        self.difficulty_levels = data.get("difficultyLevels", {})

        # Custom Free Play override
        self.custom_ranges_enabled = data.get("customRanges", {}).get("enabled", False)
        self.custom_range_operation = data.get("customRanges", {}).get("operation", "")
        self.custom_range_min = data.get("customRanges", {}).get("min", 1)
        self.custom_range_max = data.get("customRanges", {}).get("max", 10)


