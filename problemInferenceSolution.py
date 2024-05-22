import patch
from experta import *

#klasa rozszerzająca KnowledgeEngine
class PhilipsEspressoMachine(KnowledgeEngine):

    #definicja bazy faktów początkowych
    #są one wywoływane / tworzone przy użyciu metody "reset" 
    #na obiekcie klasy dziedziczącej po KnowledgeEngine
    @DefFacts()
    def _initial_facts(self):
        #fakt jest taki, że action="start"
        yield Fact(action="start")

    #reguła wywoływana pod warunkiem istnienia faktu,
    #według którego action='start' (program został uruchomiony)
    @Rule(
            Fact(action='start')
    )
    def start(self):
        wrongOption=True
        while wrongOption:

            #prośba wybrania przez użytkownika opcji,
            #która dotyczy kodu błędu, 
            #wyświetlanego na ekranie ekspresu do kawy
            option=input(
                """Który kod błędu jest widoczny na ekranie ekspresu:
                01,
                03,
                04,
                r (problem rozwiązany)
                Wybór: """
                )
        
            #definiowany jest nowy fakt,
            #według którego errorCode będzie równy kodowi błędu 
            #wybranemu przez użytkownika (gdy wybrano kod błędu,
            #jeżeli wybrano 'r' tworzony jest fakt, że solutionFound jest True)
            if option == 'r':
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif option =='01' or option =='03' or option =='04':
                self.declare(Fact(errorCode=f'{option}'))
                wrongOption=False

    ###ERROR CODE 01 (po wybraniu kodu błędu '01')

    #reguła wywoływana pod warunkiem istnienia faktu,
    #według którego action='start' (program został uruchomiony),
    #errorCode='01' (kod błędu wynosi 01)
    #i not solutionFound=True (problem nie został jeszcze rozwiązany)
    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='01'),
                Fact(errorCode=MATCH.errorCode),
                NOT(Fact(solutionFound=True))
                )
    )
    def err01(self):
        #informacja o znaczeniu błędu
        print(f'Kod błędu 01 oznacza, że lejek kawy jest zapchany zmieloną kawą lub obcym przedmiotem')
        print('Sugerowane działania:')

        #definiowany jest nowy fakt,
        #według którego program ma przejść do kroku pierwszego (Fact(int) traktowany jest jak numer kroku
        #w drodze do rozwiązania problemu)
        self.declare(Fact(1))

    #reguła wywoływana pod warunkiem istnienia faktu,
    #według którego action='start' (program został uruchomiony)
    #errorCode='01' (kod błędu wynosi 01)
    #istnieje fakt, który przechowuje wartość 1 (krok pierwszy)
    #i problem nie został jeszcze rozwiązany (not solutionFound=True)
    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='01'),
                Fact(errorCode=MATCH.errorCode),
                Fact(1),
                NOT(Fact(solutionFound=True))
                )
    )
    def err01Step1(self):
        self.takeInpuAndModify(
            'Wyłącz urządzenie i wyjmij jego wtyczkę z gniazdka elektrycznego (d- dalej, r- problem rozwiązany, p- powrót do początku): ', 
            2
            )
    
    #dalsze kroki są analogiczne

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='01'),
                Fact(errorCode=MATCH.errorCode),
                Fact(2),
                NOT(Fact(solutionFound=True))
                )
    )
    def err01Step2(self):
        self.takeInpuAndModify(
            'Wyjmij jednostkę zaparzającą (d- dalej, r- problem rozwiązany, p- powrót do początku): ', 
            3
            )
        
    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='01'),
                Fact(errorCode=MATCH.errorCode),
                Fact(3),
                NOT(Fact(solutionFound=True))
                )
    )
    def err01Step3(self):
        self.takeInpuAndModify(
            'Otwórz pokrywę pojemnika na kawę mieloną (d- dalej, r- problem rozwiązany, p- powrót do początku): ', 
            4
            )
        wrongOption=True
        while wrongOption:
            option = input('Czym zapchany jest lejek kawy: k- kawą, op- obcym przedmiotem? (r- problem rozwiązany, p- powrót do początku): ')
            if option=='k':
                self.declare(Fact(blockedBy='coffe'))
                wrongOption=False
            elif option=='op':
                self.declare(Fact(blockedBy='object'))
                wrongOption=False
            elif option=='r':
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif option=='p':
                self.comeBackToThebeggining()

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='01'),
                Fact(errorCode=MATCH.errorCode),
                Fact(4),
                Fact(blockedBy='coffe'),
                NOT(Fact(solutionFound=True))
                )
    )
    def err01Step4Coffe(self):
        print('Włóż trzonek łyżki i poruszaj nim w górę i w dół, aby zatykająca otwór kawa mielona spadła')
        wrongOption=True
        while wrongOption:
            option = input('Czy problem został rozwiązany? t- tak, n- nie: ')
            if option=='t':
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif option=='n':
                self.comeBackToThebeggining()
                wrongOption=False
    
    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='01'),
                Fact(errorCode=MATCH.errorCode),
                Fact(4),
                Fact(blockedBy='object'),
                NOT(Fact(solutionFound=True))
                )
    )
    def err01Step4Object(self):
        print('Wyjmij obcy przedmiot')
        wrongOption=True
        while wrongOption:
            option = input('Czy problem został rozwiązany? t- tak, n- nie: ')
            if option=='t':
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif option=='n':
                self.comeBackToThebeggining()
                wrongOption=False

    ### END OF ERROR CODE 01

    #pozostałe kody błędu są analogiczne

    ###ERROR CODE 03

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='03'),
                Fact(errorCode=MATCH.errorCode),
                NOT(Fact(solutionFound=True))
                )
    )
    def err03(self):
        print(f'Kod błędu 03 oznacza, że Jednostka zaparzająca jest brudna lub nie jest odpowiednio nasmarowana')
        print('Sugerowane działania:')

        self.declare(Fact(1))

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='03'),
                Fact(errorCode=MATCH.errorCode),
                Fact(1),
                NOT(Fact(solutionFound=True))
                )
    )
    def err03Step1(self):
        self.takeInpuAndModify(
            'Wyłącz urządzenie głównym wyłącznikiem (d- dalej, r- problem rozwiązany, p- powrót do początku): ', 
            2
            )

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='03'),
                Fact(errorCode=MATCH.errorCode),
                Fact(2),
                NOT(Fact(solutionFound=True))
                )
    )
    def err03Step2(self):
        self.takeInpuAndModify(
            'Opłucz jednostkę zaparzającą świeżą wodą, pozostaw ją do wyschnięcia, a następnie nasmaruj (d- dalej, r- problem rozwiązany, p- powrót do początku): ', 
            3
            )
        
    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='03'),
                Fact(errorCode=MATCH.errorCode),
                Fact(3),
                NOT(Fact(solutionFound=True))
                )
    )
    def err03Step3(self):
        self.takeInpuAndModify(
            '''
            Zapoznaj się z rozdziałem "Czyszczenie jednostki zaparzającej" 
            lub odwiedź strone www.philips.com/coffee-care aby zapoznać się z filmem instruktażowym 
            (d- dalej, r- problem rozwiązany, p- powrót do początku): 
            ''', 
            4
            )

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='03'),
                Fact(errorCode=MATCH.errorCode),
                Fact(4),
                NOT(Fact(solutionFound=True))
                )
    )
    def err03Step4(self):
        print('Włącz urządzenie ponownie')
        wrongOption=True
        while wrongOption:
            option = input('Czy problem został rozwiązany? t- tak, n- nie: ')
            if option=='t':
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif option=='n':
                self.comeBackToThebeggining()
                wrongOption=False

    ### END OF ERROR CODE 03

    ###ERROR CODE 04

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='04'),
                Fact(errorCode=MATCH.errorCode),
                NOT(Fact(solutionFound=True))
                )
    )
    def err04(self):
        print(f'Kod błędu 04 oznacza, że Jednostka zaparzająca nie jest ustawiona prawidłowo')
        print('Sugerowane działania:')

        self.declare(Fact(1))

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='04'),
                Fact(errorCode=MATCH.errorCode),
                Fact(1),
                NOT(Fact(solutionFound=True))
                )
    )
    def err04Step1(self):
        self.takeInpuAndModify(
            'Wyłącz urządzenie głównym wyłącznikiem (d- dalej, r- problem rozwiązany, p- powrót do początku): ', 
            2
            )

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='04'),
                Fact(errorCode=MATCH.errorCode),
                Fact(2),
                NOT(Fact(solutionFound=True))
                )
    )
    def err04Step2(self):
        self.takeInpuAndModify(
            '''
            Wyjmij jednostkę zaparzającą i włóż ją ponownie. 
            Zanim włożysz jednostkę zaparzającą na miejsce, 
            upewnij się, że jej zaczep blokujący 
            znajduje się w prawidłowej pozycji (d- dalej, r- problem rozwiązany, p- powrót do początku): 
            ''', 
            3
            )
        
    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='04'),
                Fact(errorCode=MATCH.errorCode),
                Fact(3),
                NOT(Fact(solutionFound=True))
                )
    )
    def err04Step3(self):
        self.takeInpuAndModify(
            '''
            Zapoznaj się z rozdziałem "Obsługa jednostki zaparzającej" 
            lub odwiedź strone www.philips.com/coffee-care aby zapoznać się z filmem instruktażowym 
            (d- dalej, r- problem rozwiązany, p- powrót do początku): 
            ''', 
            4
            )

    @Rule(
            AND(
                Fact(action='start'),
                Fact(errorCode='04'),
                Fact(errorCode=MATCH.errorCode),
                Fact(4),
                NOT(Fact(solutionFound=True))
                )
    )
    def err04Step4(self):
        print('Włącz urządzenie ponownie')
        wrongOption=True
        while wrongOption:
            option = input('Czy problem został rozwiązany? t- tak, n- nie: ')
            if option=='t':
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif option=='n':
                self.comeBackToThebeggining()
                wrongOption=False

    ### END OF ERROR CODE 04

    #reguła gratulująca użytkownikowi
    #znalezienie rozwiązania problemu
    @Rule(

        Fact(solutionFound=True)
    )
    def problemSolved(self):
        print('Gratulacje! Problem rozwiązany')

    #funkcja przywracajaca początkowy stan faktów
    def comeBackToThebeggining(self):
        self.facts.clear()
        self.reset()
        self.run()

    #funkcja drukująca użytkownikowi sugerowana operacje,
    #która ma doprowadzić do rozwiązania problemu
    # oraz przechodząca do następnego kroku (po wybranmiu opcji 'd')
    #lub kończąca działanie programu (po wybranmiu opcji 'r')
    #lub powracająca do początkowego stanu programu
    #(po wybranmiu opcji 'p')
    def takeInpuAndModify(self, inputText, nextStep):
        wrongOption=True
        while wrongOption:
            i=input(inputText)
            if i=='d':
                #modyfikowany jest fakt, który przechowuje wartość
                #kroku "step" -> zmiana wartości z currentStep na nextStep
                #(przejście do następnego kroku)
                self.declare(Fact(nextStep))
                wrongOption=False
            elif i=='r':
                #modyfikowany jest fakt, który przechowuje wartość
                #solutionFound -> zmiana wartości z False na True
                #(problem został rozwiazany)
                #UWAGA: pomoc chata gpt, jak poprawnie wykonać metodę modify
                #jak ma powinien wyglądać atrybut, przedstawiający fakt do modyfikacji
                self.declare(Fact(solutionFound=True))
                wrongOption=False
            elif i=='p':
                #stan faktów jest przywracany
                #do tego z początku programu
                self.comeBackToThebeggining()
                wrongOption=False
    

if __name__ == '__main__':

    #stworzenie instancji PhilipsEspressoMachine
    engine=PhilipsEspressoMachine()

    #wykonanie funkcji reset
    engine.reset()

    #wykonanie funkcji run
    engine.run()