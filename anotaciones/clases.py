class user:
    def __init__(self, username:str, password:str) -> None:
        self.username = username
        self.password = password
        
    def saluda(self) -> str:
        return f'hola {self.username} {self.password}'

cody = user('user123', 444)
print(cody.saluda())