from igualdad import Igualdad
conjunto='{a,b,d,c}={a,b,c,c,a,a,a,a,d}'
turing=Igualdad()
val = turing.reglas_igualdad(conjunto)

print(val)