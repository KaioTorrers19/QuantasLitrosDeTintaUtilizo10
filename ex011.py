largura= float(input('largura da parede'))
altura = float(input('altura da parede'))
area = largura*altura
print('-' *50)
print('sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
tinta = area /2
print('você precisara de {}l de tinta'.format(tinta))
print('-' *50)