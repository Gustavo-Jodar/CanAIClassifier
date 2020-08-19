import math
import matplotlib.pyplot as plt
import random

def dist_euclides(Xa, Ya, Za, Ka, La, Ma, Xb, Yb, Zb, Kb, Lb, Mb):
    return math.sqrt(pow((Xa-Xb),2) + pow((Ya-Yb),2) + pow((Za-Zb),2)+ pow((Ka-Kb),2)+ pow((La-Lb),2)+ pow((Ma-Mb),2))

def sortingDados_dist(Dados_novos):
    mudou = 1
    while(mudou):
        mudou = 0
        for i in range(1, len(Dados_novos)):
            if(Dados_novos[i-1]['distancia'] > Dados_novos[i]['distancia']):
                aux = Dados_novos[i-1]
                Dados_novos[i-1] = Dados_novos[i]
                Dados_novos[i] = aux
                mudou = 1
    return Dados_novos

def definindo_K(n):
    x = int(math.sqrt(n))
    if(x%2 == 0):
        x = x - 1
    return x

def KNN(Dados_novos, media_red_amostra, media_green_amostra, media_blue_amostra,
        DP_red, DP_green, DP_blue):
    #definido distancias entre o teste e as amostras
    for i in range(len(Dados_novos)):
        Dados_novos[i]['distancia'] = dist_euclides(media_red_amostra, media_green_amostra, media_blue_amostra, DP_red, DP_green, DP_blue,
        Dados_novos[i]['media_R'], Dados_novos[i]['media_G'], Dados_novos[i]['media_B'],
        Dados_novos[i]['DP_red'],Dados_novos[i]['DP_green'],Dados_novos[i]['DP_blue'])

    Dados_novos = sortingDados_dist(Dados_novos)

    votos_amstel = 0
    votos_guara = 0
    votos_tonic = 0
    votos_bram = 0
    votos_boem = 0
    votos_cocac = 0
    votos_orig = 0
    votos_petr = 0

    #Votos dos K next neighbors
    for i in range(0, definindo_K(len(Dados_novos))):
        if(Dados_novos[i]['latinha'] == 1):
            votos_guara = votos_guara + 1
        if(Dados_novos[i]['latinha'] == 2):
            votos_amstel = votos_amstel + 1
        if(Dados_novos[i]['latinha'] == 3):
            votos_tonic = votos_tonic + 1
        if(Dados_novos[i]['latinha'] == 4):
            votos_bram = votos_bram + 1
        if(Dados_novos[i]['latinha'] == 5):
            votos_boem = votos_boem + 1
        if(Dados_novos[i]['latinha'] == 6):
            votos_cocac = votos_cocac + 1
        if(Dados_novos[i]['latinha'] == 7):
            votos_orig = votos_orig + 1
        if(Dados_novos[i]['latinha'] == 8):
            votos_petr = votos_petr + 1

    
    votos = [votos_guara, votos_amstel, votos_bram, votos_tonic, votos_boem, votos_cocac, votos_orig, votos_petr]
    votos.sort()
    somador = 0
    for qntd_votos in votos:
        somador = somador + qntd_votos
    print("{0:.2f}% chance of being ".format((votos[7] / somador)*100))
    if(votos[7] == votos[6]):
        if(Dados_novos[0]['latinha'] == 1):
            return 1
        if(Dados_novos[0]['latinha'] == 2):
            return 2
        if(Dados_novos[0]['latinha'] == 3):
            return 3
        if(Dados_novos[0]['latinha'] == 4):
            return 4
        if(Dados_novos[0]['latinha'] == 5):
            return 5
        if(Dados_novos[0]['latinha'] == 6):
            return 6
        if(Dados_novos[0]['latinha'] == 7):
            return 7
        if(Dados_novos[0]['latinha'] == 8):
            return 8
    if(votos[7] == votos_guara):
        return 1
    if(votos[7] == votos_amstel):
        return 2
    if(votos[7] == votos_bram):
        return 4
    if(votos[7] == votos_tonic):
        return 3
    if(votos[7] == votos_boem):
        return 5
    if(votos[7] == votos_cocac):
        return 6
    if(votos[7] == votos_orig):
        return 7
    if(votos[7] == votos_petr):
        return 8
