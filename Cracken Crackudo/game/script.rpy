#By PintoMoldeGamesLtda

#Variaveis de teste
$genericBool = "xerecao"

#Nome dos Personagens

define v = Character("Heroi")
define c = Character("Cigarro")
define e = Character("Emos da Grama")
define n = Character("Arthur Dev")
define m = Character("Marina")
define bf = Character("bodao")
#Personagens e Fundos

image cigarro = ("images/c1.png")
image Heroi = ("images/vr1.png")
image concha = ("images/concha.jpg")
image emos = ("images/emos.png")
image fumando = ("images/f1.png")
image marina = ("images/m1.png")
image pb = ("images/pb.jpg")
image oBodeFinal = ("images/bodeFinal.png")
image inferno = ("images/inferno.jpg")
image ceu = ("images/heaven.jpg")
image balneario = ("images/balneario.jpg")
image balneario2 = ("images/balneario2.jpg")
image pedreiro = ("images/pedreiro.jpg")

#Sons e Audios

define audio.mychemical = "audio/FOFDCAY.mp3"

#Start

label start:
    scene concha:
        zoom 1.5

    show Heroi at truecenter:
        zoom 1.2
    v "Nossa que belo dia aqui na concha acustica de santos"
    v "Nada melhor do que 2 semanas sem fumar"
    hide Heroi

    show emos at truecenter:
        zoom 1.7
    e "nossa que saudade de voce"
    e "vamos fumar um cigarro"
    hide emos

    show Heroi at truecenter:
        zoom 1.2
    v "ta looooco mano"
    v "sei la velho"
    hide Heroi

    show cigarro at truecenter
    c "vem me fumar gostoso"
    c "eu sei que você quer"
    hide cigarro

    #MENU FUMAR OU NÃO FUMAR 1
    menu:
        "Vou fumar porraaa!!!!":
            show fumando at center:
                zoom 2
            v "nossa fumar é muito foda"
            v "preciso comprar um maço"
            hide fumando

            n "você voltou a ser um fumante fedido"

            jump gameOver

        "Não quero ser brocha!!!!!":
            show Heroi at truecenter:
                zoom 1.2
            v "vou pra PB pra relaxar"
            hide Heroi

            jump nf1

label nf1:
    scene pb:
        zoom 2.1

    show marina at truecenter:
        zoom 1.3
    m "SIIIIIIXX"
    m "Six, mano, ce ta maluco?"
    m "O que voce tava fazendo com os emos da grama?"
    hide marina

    #MENU MARINA PUTA POR CONTA DOS EMOS DA GRAMA
    menu:
        "côe mano, a vida é minha taligado?":
            show marina at truecenter:
                zoom 2
            m "vai se fuder então"
            hide marina

            jump marinaPuta

        "Eles que me chamaram mano, eu não tinha nada a ver com isso":
            show marina at truecenter:
                zoom 1.3
            m "ainda bem, eles são poser, nem escutam my chemical romance"
            hide marina

            jump marinaMyChemicalRomance

        "eles me ofereceram cigarro mas eu não quis fumar":
            show marina at truecenter:
                zoom 1.3
            m "ainda bem que você não fumou o cigarro deles, fuma o meu!!!!"
            hide marina

            jump marinaOferecendoCigarro

        "correr para o balneário":
            jump balneario

label marinaPuta:
    scene pb at truecenter:
        zoom 2.7

    show marina at truecenter:
        zoom 1.3
    m "filho da puta, sai daqui entao"
    hide marina

    scene balneario at truecenter:
        zoom 2.5

    v "acho que posso me esconder aqui"

    jump balneario

label marinaMyChemicalRomance:
    scene pb:
        zoom 2.7

    show marina at truecenter:
        zoom 1.3
    m "vamo ouvi my chemical?"
    hide marina

    call simOuNao
    if genericBool == "xerecao":
        call ouvindoMyChemical
        jump pedreiro
    else:
        show marina at truecenter:
            zoom 1.3
        m "tabom"
        hide marina

        jump marinaMyChemicalRomance
    
label marinaOferecendoCigarro:
    scene pb:
        zoom 2.7

    show marina at truecenter:
        zoom 1.3
    m "escolha um cigarro"

    menu:
        "cigarro 4":
            hide marina
            jump deuBom
        "cigarro 7":
            hide marina
            jump deuBom
        "cigarro 8":
            hide marina
            jump deuBom
        "cigarro 12":
            hide marina
            jump deuRuim
        "cigarro 13":
            hide marina
            jump deuBom
        "cigarro 14":
            hide marina
            jump deuBom
        "cigarro 17":
            hide marina
            jump deuBom

label ouvindoMyChemical:
    scene pb:
        zoom 2.7

    play sound mychemical

    show marina at truecenter:
        zoom 1.3
    m "escolha uma musica"
    

label deuBom:
    jump youWin

label deuRuim:
    jump gameOver

label simOuNao:
    menu:
        "sim":
            $genericBool = "xerecao"
        "nao":
            $genericBool = "pirocao"
    return

label gameOver:
    scene inferno at truecenter:
        zoom 2.7

    show oBodeFinal at truecenter:
        zoom 1.3

    bf "vamo ali mija"

    hide oBodeFinal
    jump labelReturn

label youWin:
    scene heaven at truecenter:
        zoom 2.7

    show emos at truecenter:
        zoom 1.3
    e "bem vindo ao céu emo"
    hide emos

    jump pedreiro

label labelReturn:
    return

label balneario:
    scene balneario at truecenter: 
        zoom 2.5 
    
    show Heroi at truecenter: 
    
    v "nossa, quase fumei aquele cigarro"
    v "vou dar um role por aqui" 
    v "pra onde eu devo ir?"

    hide Heroi

    menu: 
        "entrar no balneario":
            jump pedreiro 

        "ir para lateral":
            jump pedreiro 

label pedreiro: 
    scene pedreiro at truecenter:
        zoom 3

    n "em construção"
    n "somos vagabundos e ainda não fizemos essa parte"
    jump labelReturn