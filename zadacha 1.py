class StringVar():
    def __init__(self, string):
        self._string = string

    def get(self): 
        return self._string

    def set(self, string): 
        self._string = string
obj = StringVar('Привет!')
print(obj.get())
obj.set('Здравствуй!')
print(obj.get())