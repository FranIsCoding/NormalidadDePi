from manim import *
import random

class PrimeraEscena(Scene):
    def construct(self):
        #Here we create all the necesary objects for the first scene
        text0 = Text("¿Qué es π?").scale(1).shift(2*UP)
        text1 = Text('3.141592 ... y un largo excetera').scale(1)
        text2 = Text("3.141592 ... ×").shift(2.2*LEFT,0.5*DOWN).scale (0.5)
        text3 = Text("=")
        text4 = Text("π").scale(2)
        text5 = Text("Matemáticas",color=BLUE).shift(2.5*UP).scale (0.75)
        text6 = Text("Cinemática",color=WHITE).shift(2.5*DOWN).scale (0.75)
        text7 = Text("Biología",color=GREEN).shift(1.3*UP,2.5*LEFT).scale (0.75)
        text8 = Text("Computación",color=PURPLE).shift(1.3*UP,2.5*RIGHT).scale (0.75)
        text9 = Text("Cuántica",color=YELLOW).shift(1.3*DOWN,2.5*RIGHT).scale (0.75)
        text10 = Text("Relatividad",color=RED).shift(1.3*DOWN,2.5*LEFT).scale (0.75)
        text11 = Text("¿Pero es                  Normal?")
        text12 = Text("Por: Francisco Rodriguez y Santiago Quintero").scale(0.7).shift(1.5*DOWN)
        
        #Here we create all the subtitles
        sub0 = Text("También es la relación entre el perímetro y el diámetro de un círculo.").scale(0.5).shift(3.2*DOWN)
        sub1 = Text("Lo curioso es que Pi no se limita a los círculos.").scale(0.5).shift(3.2*DOWN)
        sub2 = Text("Es parte de la solución del problema de Basilea.").scale(0.5).shift(3.2*DOWN)
        sub3 = Text("Está en la velocidad angular.").scale(0.5).shift(3.2*DOWN)
        sub4 = Text("En las redes neuronales no lineales").scale(0.5).shift(3.2*DOWN)
        sub5 = Text("Incluso en la ecuación más bella del mundo.").scale(0.5).shift(3.2*DOWN)
        sub6 = Text("La conexión con Pi y otras áreas de la ciencia, es clara.").scale(0.5).shift(3.2*DOWN)


        circle1 = Circle(radius=1.0,color=WHITE)
        circle2 = Circle(radius=1.0,color=WHITE)  # create a circle
        
        perimeter = Line(color=BLUE,start=3.14*LEFT,end=3.14*RIGHT).shift(0.5*UP)
        diameter = Line(color=RED)
        
        basilea = Tex(r"$\sum_{i=0}^{\infty}{\frac{1}{i^{2}}}$ = $\frac{\pi^{2}}{6}$",font_size=100,color=BLUE)
        angularSpeed = Tex(r"$\nu$ = $\pi \omega$",font_size=80,color=RED).shift(1.5*DOWN,2.0*LEFT)
        neuralTrigonometrics = Tex(r"$y_{i}$ = $sin(\pi x_{i})$",font_size=80,color=YELLOW).shift(1.5*DOWN,2.0*RIGHT)
        theMostBeauty = Tex(r"$e^{i\pi}-1=0$",font_size=80,color=GREEN).shift(2.5*DOWN)
        #Herr we start creating the animations
        self.add(text0)
        self.wait(2)
        self.play(Create(text1))
        self.wait(5)
        self.remove(text1)
        self.wait(1)
        self.add(sub0)
        self.play(Create(circle1))
        self.wait(2)
        self.play(Create(diameter))
        self.wait(1)
        self.play(diameter.animate.shift(0.5*DOWN))
        self.play(Transform(circle1,perimeter))
        self.wait(1)
        self.play(Create(text2))
        self.play(Create(text3))
        self.wait(4)
        self.remove(text3,text2,diameter,circle1,sub0)
        self.add(sub1)
        self.wait(2)
        self.remove(sub1)
        self.add(sub2)
        self.play(Create(basilea))
        self.wait(2)
        self.remove(sub2)
        self.add(sub3)
        self.play(Create(angularSpeed))
        self.wait(2)
        self.remove(sub3)
        self.add(sub4)
        self.play(Create(neuralTrigonometrics))
        self.wait(2)
        self.remove(sub4)
        self.add(sub5)
        self.play(Create(theMostBeauty))
        self.wait(2)
        self.remove(text0,basilea,angularSpeed,neuralTrigonometrics,theMostBeauty,sub5)
        self.add(sub6)
        self.wait(1.5)
        self.play(Create(circle2))
        self.play(Create(text4))
        self.wait(1.5)
        self.play(Create(text5))
        self.play(Create(text6))
        self.play(Create(text7))
        self.play(Create(text8))
        self.play(Create(text9))
        self.play(Create(text10))
        self.wait(2)
        self.remove(text5,text6,text7,text8,text9,text10,sub6)
        self.wait(2.5)
        self.add(text11,text12)
        self.wait(3)
        self.remove(text11,text12,text4,circle2)

class SegundaEscena(Scene):
    def construct(self):

        text0 = Text("¿Qué es un número normal?").scale(1).shift(2*UP)
        text1 = Text("En general no es trivial saber si un número es normal o no. \n No existe algoritmo alguno para determinarlo.").scale(0.5)
        text2 = Text("1 aparece un total de 19 veces de 1 a 100 \n 2 aparece un total de veces de 19 de 1 a 100.")
        
        sub0 = Text("Okay, eso fue algo ... difícil.").scale(0.5).shift(3.2*DOWN)
        sub1 = Text("Es mejor pensarlo de esta forma, \n 'Si tengo un número de infinitos dígitos, ¿qué probilidad tiene cada dígito en aparecer?'.").scale(0.5).shift(3.2*DOWN)
        sub2 = Text("Si la probabilidad es la misma, entonces el número es normal. \n Similar a como funciona un dado.").scale(0.5).shift(3.2*DOWN)
        sub3 = Text("Ambas constantes son números normales en base 10.").scale(0.5).shift(3.2*DOWN)
        sub4 = Text("Hay números que, según la base, son normales o no.").scale(0.5).shift(3.2*DOWN)
        sub5 = Text("La constante Binaria de Champernowne es normal, pero no en una base mayor").scale(0.5).shift(3.2*DOWN)
        sub6 = Text("La medida de Lebesgue es 0 en el caso de los números anormales. \n Sabemos por ello que hay más números normales.").scale(0.5).shift(3.2*DOWN)
        sub7 = Text("Por ejemplo, observemos la constante de Champernowne").scale(0.5).shift(3.2*DOWN)
        sub8 = Text("Si tomamos las cadenas de tamaño 1, se ve que tiene la misma probabilidad.").scale(0.5).shift(3.2*DOWN)
        sub9 = Text("Si tomamos las cadenas de tamaño 2, se ve el mismo patrón.").scale(0.5).shift(3.2*DOWN)
        sub10 = Text("En general, se tiene ésto para cualquier longitud k.").scale(0.5).shift(3.2*DOWN)



        def0 = Tex(r"Sea b $>$ 1 un número entero y x un número real. \\ Consideremos la sucesión de cifras de x en la base de numeración b. \\ Si s es una sucesión finita de cifras en base b, escribiremos N(s, n) \\ para expresar el número de apariciones de la sucesión s entre las n primeras cifras de x. El número x se considera normal en base b (b-normal) si .",font_size=30)
        def1 = Tex(r"$\lim_{n\rightarrow \infty} \frac{N(s,n)}{n} = \frac{1}{b^{k}}$",font_size=30).shift(2*DOWN)
        def2 = Tex(r"para cada sucesión s de longitud k.",font_size=30).shift(3*DOWN)
        lebesgue = Tex(r"$\lambda(\text{No Normales})$ = 0").shift(1.5*DOWN)

        champernowne = Text("Champernowne = 0,1234567891011121314151617...",color=BLUE).scale(0.5).shift(0.75*UP)
        copelandErdos=Text("Copealand-Erdos = 0.23571113171923293137414347535961677173798389...",color=RED).scale(0.5).shift(0.75*DOWN)
        champernowneBin = Text("ChampernowneBin = 0,0110111001011101111000100110101011...   Es normal",color=BLUE).scale(0.5).shift(0.75*UP)
        champernowneBinB10 = Text("Conversion en base 10 = 0.4311200628872029483318328857420...  No es normal").scale(0.5).shift(0.75*DOWN)
        

        self.add(text0)
        self.play(Write(def0))
        self.play(Write(def1))
        self.play(Write(def2))
        self.wait(5)
        self.remove(def0,def1,def2)
        self.play(Write(sub0))
        self.wait(2)
        self.remove(sub0)
        self.play(Write(sub1))
        imagen = ImageMobject("dice.png").shift(2*LEFT)
        prob1 = Tex(r"P(\text{Digito entre 1 y 6}) = $\frac{1}{6}$").shift(2*RIGHT)
        self.add(imagen)
        self.play(Write(prob1))
        self.remove(sub1)
        self.play(Write(sub2))
        self.wait(4)
        self.remove(imagen,prob1)
        self.play(Write(champernowne))
        self.play(Write(copelandErdos))
        self.wait(3)
        self.remove(sub2)
        self.play(Write(sub3))
        self.wait(2)
        self.remove(sub3,champernowne,copelandErdos)
        self.play(Write(champernowneBin))
        self.play(Write(champernowneBinB10))
        self.play(Write(sub4))
        self.wait(2)
        self.remove(sub4)
        self.play(Write(sub5))
        self.wait(4)
        self.remove(sub5,champernowneBin,champernowneBinB10)
        self.play(Write(text1))
        self.play(Write(lebesgue))
        self.play(Write(sub6))
        self.wait(3)
        self.remove(sub6,lebesgue,text1)
        self.play(Write(sub7))
           
        numero_texto = Text("012345678910111213141516..")

   
        self.play(Write(numero_texto))

        self.remove(sub7)
        self.play(Write(sub8))

        probc1 = Tex(r"$P(cifra) = \frac{1}{10}$").shift(1*DOWN)
        
        self.wait(1)
        self.play(Write(probc1))


        for cifra in numero_texto:
            self.play(cifra.animate.set_color(YELLOW), run_time=1)
            self.play(cifra.animate.set_color(WHITE), run_time=1)


        self.remove(sub8,probc1)
        self.play(Write(sub9))

        probc2 = Tex(r"$P(cifra) = \frac{1}{100}$").shift(1*DOWN)
        
        self.wait(1)
        self.play(Write(probc2))


        for i in range(0, len(numero_texto), 2):
            cifras_a_iluminar = VGroup(numero_texto[i], numero_texto[i+1])
            self.play(cifras_a_iluminar.animate.set_color(YELLOW), run_time=1)
            self.play(cifras_a_iluminar.animate.set_color(WHITE), run_time=1)
       
        self.wait(1)

        self.play(numero_texto.animate.set_color(BLACK))
        self.remove(probc2)
        self.remove(text0,sub9)

        self.wait(1)
        



class TerceraEscena(Scene):
    def construct(self):

        text0 = Tex(
            "En las primeras 10 cifras, cada dígito tiene la misma probabilidad de aparecer. ",
            "Es fácil ver que en las primeras cien cifras, 0 a 100, 1 se repite 19 veces,",
            " 2 se repite 19 veces, y lo mismo ocurre para las demás cifras en base 10.",
            " Si aumentamos la longitud de las cadenas a 2, veremos que en las cien primeras cifras",
            " cada número aparece una sola vez, y en 1000 cifras aparece la misma cantidad de veces"
            
        ).scale(0.8)

        self.play(Write(text0))

        self.wait(3)

        self.remove(text0)

        texto_inicial = Text("¿Entonces es Pi Normal?", font_size=48)

        # Agrega el objeto de texto a la escena
        self.play(Write(texto_inicial))

        # Espera un momento
        self.wait(1)
        imagen = ImageMobject("ComputosDePI.png")

        self.remove(texto_inicial)
        self.add(imagen)
        # Espera otro momento
        self.wait(1)

        # Agrega otro texto
        text1 = Text("Mediante cálculos computacionales sabemos que es normal, \n pero hoy en día no hay una prueba fehaciente de que sea un número normal.", font_size=25).next_to(imagen, DOWN)

        self.play(Write(text1))

        # Espera un poco más antes de finalizar
        self.wait(4)

        self.remove(text1,imagen)

        text2 = Tex("Números irracionales como la $\sqrt{2}, \pi, e, \phi$ se sospecha que son normales,",
        " pues de no serlo, mediante métodos probabilísticos, podríamos determinar cuáles serían las siguientes",
        " cifras de estos números. En general, solo se conoce la normalidad de números que son explicitamente normales.",
        " Quiza en un futuro, nuevos criterios puedan responder esta pregunta sobre el patrón de los números irracionales").scale(0.8)

        self.play(Write(text2))

        self.wait(4)

        self.remove(text2)

        text3 = Tex("Muchas gracias por vernos.")

        self.play(Write(text3))

        self.wait(4)

        self.remove(text3)



class scene(Scene):
    def construct(self):
        PrimeraEscena.construct(self)
        SegundaEscena.construct(self)
        TerceraEscena.construct(self)
