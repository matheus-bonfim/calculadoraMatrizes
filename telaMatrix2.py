import PySimpleGUI as sg
import copy

def det2x2(matriz):
    det1 = matriz[0][0] * matriz[1][1]
    det2 = matriz[0][1] * matriz[1][0]
    det = det1 - det2
    return det

def redutormatriz(matriz, linha, coluna):
    matriznova = copy.deepcopy(matriz)
    matriznova.remove(matriznova[linha])
    for i in range(0, len(matriznova),1):
        del matriznova[i][coluna]    
    return matriznova

def C(matriz, linha, coluna):
    oLinha = linha + 1
    oColuna = coluna + 1
    if len(matriz) == 3:
        Ck = (-1)**(oLinha + oColuna) * det2x2(redutormatriz(matriz, linha, coluna))
    else:
        Ck = (-1)**(oLinha + oColuna) * det(redutormatriz(matriz, linha, coluna))
    return Ck

def det(matriz):
    if len(matriz) == 2:
        soma = det2x2(matriz)
    else:
        linha = 0
        soma = 0
        for i in range(0, len(matriz), 1):
            a = matriz[linha][i]*C(matriz, linha, i)
            soma = soma + a 

    return soma





def janela_inicial():
    sg.theme('Reddit')
    layout = [  
            [sg.Text('Deseja calcular o determinante de qual matriz?')],
            [sg.Button('2x2'), sg.Button('3x3'), sg.Button('4x4'), sg.Button('5x5')] ]
    return sg.Window('Calculadora de Determinante',layout=layout,finalize=True)

def janela_mat2x2():
    sg.theme('Reddit')
    layoutmat2x2 = [
            [sg.Text('Matriz 2x2')],
            [sg.Input(size=(2,0),key='a11'),sg.Input(size=(2,0),key='a12')],
            [sg.Input(size=(2,0), key = 'a21'),sg.Input(size=(2,0),key='a22')],
            [sg.Button('Calcular'),sg.Button('Voltar')],
            [sg.Output(size=(20,5))]
        ]
    return sg.Window('Matriz 2x2',layout=layoutmat2x2,finalize=True)

def janela_mat3x3():
    sg.theme('Reddit')
    layoutmat3x3 = [
            [sg.Text('Matriz 3x3')],
            [sg.Input(size=(2,0),key='a'),sg.Input(size=(2,0),key='b'),sg.Input(size=(2,0),key='c')],
            [sg.Input(size=(2,0), key = 'd'),sg.Input(size=(2,0),key='e'),sg.Input(size=(2,0),key='f')],
            [sg.Input(size=(2,0), key = 'g'),sg.Input(size=(2,0),key='h'),sg.Input(size=(2,0),key='i')],
            [sg.Button('Calcular'), sg.Button('Voltar')],
            [sg.Output(size=(20,5))]
            ]
    return sg.Window('Matriz 3x3',layout=layoutmat3x3,finalize=True)

def janela_mat4x4():
    sg.theme('Reddit')
    layoutmat4x4 = [
        [sg.Text('Matriz 4x4')],
        [sg.Input(size=(2,0),key='a'),sg.Input(size=(2,0),key='b'),sg.Input(size=(2,0),key='c'),
        sg.Input(size=(2,0), key = 'd')],

        [sg.Input(size=(2,0),key='e'),sg.Input(size=(2,0), key = 'f'),sg.Input(size=(2,0),key='g'),sg.Input(size=(2,0),key='h')],

        [sg.Input(size=(2,0),key='i'),sg.Input(size=(2,0),key='j'),
        sg.Input(size=(2,0), key = 'k'),sg.Input(size=(2,0),key='l')],

        [sg.Input(size=(2,0), key = 'm'),sg.Input(size=(2,0),key='n'),sg.Input(size=(2,0),key='o'), 
        sg.Input(size=(2,0),key='p')],

        [sg.Button('Calcular'), sg.Button('Voltar')],
        [sg.Output(size=(20,5))]
        ]
    return sg.Window('Matriz 4x4',layout=layoutmat4x4,finalize=True)

def janela_mat5x5():
    sg.theme('Reddit')
    layoutmat5x5 = [
        [sg.Text('Matriz 5x5')],
        [sg.Input(size=(2,0),key='a'),sg.Input(size=(2,0),key='b'),sg.Input(size=(2,0),key='c'),
        sg.Input(size=(2,0), key = 'd'),sg.Input(size=(2,0),key='e')],

        [sg.Input(size=(2,0),key='f'),sg.Input(size=(2,0), key = 'g'),sg.Input(size=(2,0),key='h'),sg.Input(size=(2,0),key='i'),
        sg.Input(size=(2,0),key='j')],

        [sg.Input(size=(2,0),key='k'),sg.Input(size=(2,0),key='l'),
        sg.Input(size=(2,0), key = 'm'),sg.Input(size=(2,0),key='n'),sg.Input(size=(2,0),key='o')],

        [sg.Input(size=(2,0), key = 'p'),sg.Input(size=(2,0),key='q'),sg.Input(size=(2,0),key='r'), 
        sg.Input(size=(2,0),key='s'),sg.Input(size=(2,0),key='t')],

        [sg.Input(size=(2,0),key='u'),sg.Input(size=(2,0), key = 'v'),sg.Input(size=(2,0),key='w'),sg.Input(size=(2,0),key='x'),
        sg.Input(size=(2,0), key = 'y')],
        [sg.Button('Calcular'), sg.Button('Voltar')],
        [sg.Output(size=(20,5))]
        ]
    return sg.Window('Matriz 5x5',layout=layoutmat5x5,finalize=True)


janela1, janela2, janela3, janela4, janela5 = janela_inicial(), None, None, None, None

while True:
    window, event, values = sg.read_all_windows()

    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == '2x2':
        janela2 = janela_mat2x2()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela1 and event == '3x3':
        janela3 = janela_mat3x3()
        janela1.hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    if window == janela1 and event == '5x5':
        janela5 = janela_mat5x5()
        janela1.hide()
    if window == janela5 and event == 'Voltar':
        janela5.hide()
        janela1.un_hide()
    if window == janela1 and event == '4x4':
        janela1.hide()
        janela4 = janela_mat4x4()
    if window == janela4 and event == 'Voltar':
        janela4.hide()
        janela1.un_hide()




    
    if window == janela2 and event == 'Calcular':
       
        a11 = int(values['a11'])
        a12 = int(values['a12'])
        a21 = int(values['a21'])
        a22 = int(values['a22'])
        matriz2x2 = [[a11,a12],[a21,a22]]   
        print(f"Sua matriz: {matriz2x2}")
        print(F"DETERMINANTE: {det(matriz2x2)}") 

    if window == janela3 and event == 'Calcular':

        a11 = int(values['a'])
        a12 = int(values['b'])
        a13 = int(values['c'])
        a21 = int(values['d'])
        a22 = int(values['e'])
        a23 = int(values['f'])
        a31 = int(values['g'])
        a32 = int(values['h'])
        a33 = int(values['i'])
        matriz3x3 = [[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]]
        print(f"Sua matriz: {matriz3x3}")
        print(F"DETERMINANTE: {det(matriz3x3)}")

    if window == janela4 and event == 'Calcular':
        a11 = int(values['a'])
        a12 = int(values['b'])
        a13 = int(values['c'])
        a14 = int(values['d'])
        a21 = int(values['e'])
        a22 = int(values['f'])
        a23 = int(values['g'])
        a24 = int(values['h'])
        a31 = int(values['i'])
        a32 = int(values['j'])
        a33 = int(values['k'])
        a34 = int(values['l'])
        a41 = int(values['m'])
        a42 = int(values['n'])
        a43 = int(values['o'])
        a44 = int(values['p'])

        matriz4x4 = [[a11,a12,a13,a14],[a21,a22,a23,a24],[a31,a32,a33,a34],[a41,a42,a43,a44]]
        print(f"Sua matriz: {matriz4x4}")
        print(F"DETERMINANTE: {det(matriz4x4)}")


    if window == janela5 and event == 'Calcular':

        a11 = int(values['a'])
        a12 = int(values['b'])
        a13 = int(values['c'])
        a14 = int(values['d'])
        a15 = int(values['e'])
        a21 = int(values['f'])
        a22 = int(values['g'])
        a23 = int(values['h'])
        a24 = int(values['i'])
        a25 = int(values['j'])
        a31 = int(values['k'])
        a32 = int(values['l'])
        a33 = int(values['m'])
        a34 = int(values['n'])
        a35 = int(values['o'])
        a41 = int(values['p'])
        a42 = int(values['q'])
        a43 = int(values['r'])
        a44 = int(values['s'])
        a45 = int(values['t'])
        a51 = int(values['u'])
        a52 = int(values['v'])
        a53 = int(values['w'])
        a54 = int(values['x'])
        a55 = int(values['y'])
        
        matriz5x5 = [[a11,a12,a13,a14,a15],[a21,a22,a23,a24,a25],[a31,a32,a33,a34,a35],[a41,a42,a43,a44,a45],[a51,a52,a53,a54,a55]]
        print(f"Sua matriz: {matriz5x5}")
        print(F"DETERMINANTE: {det(matriz5x5)}")


        
        

