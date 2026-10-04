class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    # Your code here
    
    def is_worth_it(self):
        value=self.crew * 1.5
        draft=self.draft-value
        if draft>20:
            return True
        else:
            return False