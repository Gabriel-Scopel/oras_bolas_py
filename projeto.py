from math import *
import math
"""import matplotlib.pyplot as plt"""

def TrajetoriaBola():
    tempo=[]
    lista = []
    with open("Ora_bolas-trajetoria _bola_oficial.txt", "r") as dados_bola:
        linha = dados_bola.readlines()
        for i in linha:
            lista.append(i.replace("\x00", "").replace(",", ".").strip("").split())
        dados_bola.close
    for i in range(1003):
        if len(lista[i]) == 0:
            lista.pop(i)
        else:
            pass
    lista.pop(-1)
    lista.pop(0)
    for i in range(len(lista)):
        tempo.append(lista[i][0])
    return lista, tempo

"""def campo(SxBola, SyBola, SxRobo, SyRobo):
    plt.figure(figsize=(9,6))
    plt.plot(SxBola, SyBola, label = "Bola")
    plt.plot(SxRobo, SyRobo, label = "Robo")
    plt.xlabel("eixo X")
    plt.ylabel("eixo Y")
    plt.title("Campo")
    plt.ylim(0,6)
    plt.xlim(0,9)
    plt.yticks(range(0, 7))
    plt.legend()
    plt.show()
    pass

def posiçãoRBX(SxBola, SxRobo, tempo):
    plt.plot(tempo, SxRobo, label= "Robo")
    plt.plot(tempo[:-1], SxBola, label = 'Bola')
    plt.ylabel("Sxrobo e Sxbola")
    plt.xlabel("tempo")
    plt.legend()
    plt.show()
    pass

def posiçãoRBY(SyBola, SyRobo, tempo):
    plt.plot(tempo, SyRobo, label= "Robo")
    plt.plot(tempo[:-1], SyBola, label = 'Bola')
    plt.ylabel("Syrobo e Sybola")
    plt.xlabel("tempo")
    plt.legend()
    plt.show()
    pass

def VeloRBY(VyBola, VyRobo, tempo):
    plt.plot(tempo[:-1], VyBola, label = 'Bola')
    plt.plot(tempo, VyRobo, label= "Robo")
    plt.ylabel("Vyrobo e Vybola")
    plt.xlabel("tempo")
    plt.legend()
    plt.show()
    pass"""

def MovRoboXY2(t2i, xri2, yri2, trajbola, tempo, SxRobo, SyRobo, VxRobo, VyRobo, AxRobo, AyRobo):
    m, c, angulo, deltaX, deltaY= RetaRoboTraj2(xri2, yri2, trajbola)
    print(f"A SEGUNDA RETA DO ROBO NO CAMPO É: y = {m:.3f}x + {c:.3f}")
    print(f"o angulo da reta é: {angulo:.2f}")
    print(f"O cosseno do angulo é: {math.cos(math.radians(angulo)):.3f}")
    print(f"O seno do angulo é: {math.sin(math.radians(angulo)):.3f}")
    coss = math.cos(math.radians(angulo))
    seno = math.sin(math.radians(angulo))
    ay = (2.8*seno)
    ax = (2.8*coss)
    if ((deltaX<0) and (deltaY>=0)) or ((deltaX<0 and deltaY<0)):
        ay *= -1
        ax *= -1
    tpara = sqrt((deltaX/ax)**2)
    ti = float(tempo[t2i])
    Vox = sqrt(ax*deltaX)
    tpara1 = deltaX/Vox
    print(f"O valor de DEltaX é {deltaX:.3f}e DEltay é {deltaY:.3f}")
    print(f"O valor de ti é {ti:.3f} e o valor de parada é {tpara:.3f} tpara1{tpara1:.3f}")
    print(f"O valor de AX é {ax:.3f}e Ay é {ay:.3f}")
    for i in range(t2i, 1001):
        t = float(tempo[i])
        Vox = sqrt(ax*deltaX)
        tpara = sqrt((deltaX/Vox)**2)
        if t <= (tpara+ti):
            print("entrou 1")
            SRoboY = (ay*((t-ti)**2))/2 + yri2
            Vy = ay*(t-ti)
            SRoboX = (ax*((t-ti)**2))/2 + xri2
            Vx = ax*(t-ti)
        elif (tpara+ti)<t<(tpara*2+ti):
            print("entrou 2")
            Vox = -1*sqrt(ax*deltaX)
            Vx =  Vox - (ax*(t-(tpara+ti)))
            SRoboX = Vox*(t-(tpara+ti)) - ((ax*((t-(tpara+ti))**2))/2)+ deltaX/2 +xri2
            Voy = -1*sqrt(ay*deltaY)
            Vy =  Voy - (ay*(t-(tpara+ti)))
            SRoboY = Voy*(t-(tpara+ti)) - ((ay*((t-(tpara+ti))**2))/2) + deltaY/2 + yri2
        elif t>=(tpara*2+ti):
            print("entrou 3")
            Vy = 0
            Vx = 0
            SRoboX = deltaX + xri2
            SRoboY = deltaY + yri2
        SxRobo.append(round(SRoboX, 4))
        SyRobo.append(round(SRoboY, 4))
        VxRobo.append(round(Vx, 4))
        VyRobo.append(round(Vy, 4))
        AxRobo.append(round(ax, 4))
        AyRobo.append(round(ay, 4))         
        print(f"Em {t} segundos o X vale {SRoboX:.3f} e a VelocidadeX é igual a {Vx:.3f}")
        print(f"Em {t} segundos o Y vale {SRoboY:.3f} e a VelocidadeY é igual a {Vy:.3f}")
       
        if RaioInterceptação(SRoboX , SRoboY, tempo[i], trajbola) == 1:
            Tencontro = t
            indice = i
            break
        else:
            pass
    return Tencontro, SxRobo, SyRobo, VxRobo, VyRobo, AxRobo, AyRobo, indice

def MovRoboXY(sen,cos, xri, yri, deltaX, deltaY, tempo, trajbola):
    SxRobo=[]
    SyRobo=[]
    VxRobo=[]
    VyRobo=[]
    AxRobo=[]
    AyRobo=[]
    ay = 2.8*sen
    ax = 2.8*cos
    Tencontro = 0
    if ((deltaX<0) and (deltaY>=0)) or ((deltaX<0 and deltaY<0)):
        ay *= -1
        ax *= -1
    tpara = sqrt((deltaX/ax)**2)
    t2i=0
    xri2=0
    yri2=0
    print(f'tpara: {tpara:.3f}')
    print(f'deltaX: {deltaX:.3f}')
    print(f'deltay: {deltaY:.3f}')
    for i in range(0, 1001):
        t = float(tempo[i])
        if tpara>=1:
            if t <= 1:
                SRoboY = (ay*(t**2))/2 + yri
                Vy = ay*t
                SRoboX = (ax*(t**2))/2 + xri
                Vx = ax*t
            elif 1<t<tpara:
                Vy = ay
                SRoboY = Vy*(t-1) + (ay/2 + yri)
                Vx = ax
                SRoboX = Vx*(t-1) + (ax/2 + xri)
            elif tpara<t<(tpara+1):
                Voy = ay
                Vy = Voy - (ay*(t-tpara))
                SRoboY = Voy*(t-tpara) - ((ay*((t-tpara)**2))/2) + deltaY - (Voy/2) + yri
                Vox = ax
                Vx = Vox - (ax*(t-tpara))
                SRoboX = Vox*(t-tpara) - ((ax*((t-tpara)**2))/2) + deltaX - (Vox/2) + xri
            elif t>=(tpara+1):
                Vy = 0
                Vx = 0
                SRoboX = deltaX + xri
                SRoboY = deltaY + yri
                t2i= i
                xri2 = SRoboX
                yri2 = SRoboY
                print(f"Em {t} segundos o Y vale {SRoboY:.3f} e a VelociadeY é igual a {Vy:.3f}")
                print(f"Em {t} segundos o X vale {SRoboX:.3f} e a VelociadeX é igual a {Vx:.3f}")
                break
            SxRobo.append(round(SRoboX, 4))
            SyRobo.append(round(SRoboY, 4))
            VxRobo.append(round(Vx, 4))
            VyRobo.append(round(Vy, 4))
            AxRobo.append(round(ax, 4))
            AyRobo.append(round(ay, 4))
            print(f"Em {t} segundos o Y vale {SRoboY:.3f} e a VelociadeY é igual a {Vy:.3f}")
            print(f"Em {t} segundos o X vale {SRoboX:.3f} e a VelociadeX é igual a {Vx:.3f}")
            if RaioInterceptação(SRoboX , SRoboY, tempo[i], trajbola) == 1:
                Tencontro = t
                break
            else:
                pass
        else:
            Vox = sqrt(ax*deltaX)
            tpara = sqrt((deltaX/Vox)**2)
            if t <= tpara:
                SRoboY = (ay*(t**2))/2 + yri
                Vy = ay*t
                SRoboX = (ax*(t**2))/2 + xri
                Vx = ax*t
                SxRobo.append(round(SRoboX, 4))
                SyRobo.append(round(SRoboY, 4))
                VxRobo.append(round(Vx, 4))
                VyRobo.append(round(Vy, 4))
                AxRobo.append(round(ax, 4))
                AyRobo.append(round(ay, 4))
                print(f"Em {t} segundos o X vale {SRoboX:.3f} e a VelociadeX é igual a {Vx:.3f}")
                print(f"Em {t} segundos o Y vale {SRoboY:.3f} e a VelociadeY é igual a {Vy:.3f}")
            elif tpara<t<(tpara*2):
                Voy = sqrt(ay*deltaY)
                Vox = sqrt(ax*deltaX)
                if (deltaX<0 and deltaY<0):
                    Vox *= -1
                    Voy *= -1
                elif deltaY<0:
                    Voy *= -1
                elif deltaX <0:
                    Vox *= -1
                SRoboX = Vox*(t-tpara) - ((ax*((t-tpara)**2))/2) + (ax*(tpara**2))/2 +xri
                Vx = Vox - (ax*(t-tpara))
                Vy = Voy - (ay*(t-tpara))
                SRoboY = Voy*(t-tpara) - ((ay*((t-tpara)**2))/2) + (ay*(tpara**2))/2 + yri
                SxRobo.append(round(SRoboX, 4))
                SyRobo.append(round(SRoboY, 4))
                VxRobo.append(round(Vx, 4))
                VyRobo.append(round(Vy, 4))
                AxRobo.append(round(-ax, 4))
                AyRobo.append(round(-ay, 4))
                print(f"Em {t} segundos o X vale {SRoboX:.3f} e a VelocidadeX é igual a {Vx:.3f}")
                print(f"Em {t} segundos o Y vale {SRoboY:.3f} e a VelocidadeY é igual a {Vy:.3f}")
            elif t>=(tpara*2):
                Vy = 0
                Vx = 0
                SRoboX = deltaX + xri
                SRoboY = deltaY + yri
                t2i= i
                xri2 = SRoboX
                yri2 = SRoboY
                SxRobo.append(round(SRoboX, 4))
                SyRobo.append(round(SRoboY, 4))
                VxRobo.append(round(Vx, 4))
                VyRobo.append(round(Vy, 4))
                AxRobo.append(round(ax, 4))
                AyRobo.append(round(ay, 4))
                print(f"Em {t} segundos o X vale {SRoboX:.3f} e a VelocidadeX é igual a {Vx:.3f}")
                print(f"Em {t} segundos o Y vale {SRoboY:.3f} e a VelocidadeY é igual a {Vy:.3f}")
                break
            if RaioInterceptação(SRoboX , SRoboY, tempo[i], trajbola) == 1:
                Tencontro = t
                break
            else:
                pass
    if Tencontro == 0:
        Tencontro, SxRobo, SyRobo, VxRobo, VyRobo, AxRobo, AyRobo, indice = MovRoboXY2(t2i, xri2, yri2, trajbola, tempo, SxRobo, SyRobo, VxRobo, VyRobo, AxRobo, AyRobo)
    else:
        pass
    return Tencontro, SxRobo, SyRobo, VxRobo, VyRobo, AxRobo, AyRobo, indice