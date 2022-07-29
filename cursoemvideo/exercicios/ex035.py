# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    triangulo = 'PODEM FORMAR'
else:
    triangulo = 'NÃO PODEM FORMAR'
print('Os segmentos acima {} um triângulo.'.format(triangulo))
