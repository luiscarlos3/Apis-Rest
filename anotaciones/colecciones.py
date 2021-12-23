from typing import List
from typing import Tuple
from typing import Union
from typing import Dict

calificaciones : List[int] = [2,3,4,5,6,7,8,9,10,11]

def promedio(calificaciones:List[int]) -> float:
    return sum(calificaciones) / len(calificaciones)

print(promedio(calificaciones))


configuraciones: Tuple[str] = ('localhost', '3306', 'root')
print(configuraciones)

valores: Tuple[Union[str, str, bool, int]] = ('root', 'localhost', True, 3306) # isplicitamente
print(valores)


usuarios: Dict[str, int] = {
    'Eduardo':10,
    'Cody':10   
    
}


print(usuarios)

