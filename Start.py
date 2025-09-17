var_Nome = input('Digite o seu nome: ')
var_Empresa = input('Digite o nome da empresa: ')
var_DiasSuporte = input('Digite a quantidade de dias de Suporte da Semana: ')
var_Semana = input('Digite a quantidade de semanas no Mês do Suporte: ')
var_DiasSuporteMes = int(var_DiasSuporte) * int(var_Semana)
var_DiasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
var_meses = ['Janeiro', 'Fevereiro', 'Março']
var_DiasSemana.extend(var_meses)
var_meses.remove('Março')
var_Lista_Funcionario = open('Lista_Funcionarios.txt', 'r')

print('A funcionária ' + var_Nome + ' da empresa ' + var_Empresa + ' trabalha ' + str(var_DiasSuporte) + ' dias de Suporte na semana.')
print('A funcionária '+var_Nome + ' trabalhará ' + str(int(var_DiasSuporte) * int(var_Semana)) + ' dias de suporte no Mes.')
print('Dias Suporte Mes: ' + str(var_DiasSuporteMes))
print(var_DiasSemana[1:3])
print('Dias da Semana com extensão dos meses: '+str(var_DiasSemana))
print(var_meses)
print('O mês de Janeiro está na posição: '+ var_meses.index('Janeiro'))
print('Lista de Funcionários da empresa '+var_Empresa + ' : '+var_Lista_Funcionario.read())




