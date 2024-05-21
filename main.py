import patch
from experta import *

#LEGENDA (Elementy - możliwe stany elementów) :
#lejek kawy - luźny lub zapchany
#jednostka zaparzająca - brudna, czysta, odpowiednio nasmarowana, nieodpowiednio nasmarowana, ustawiona prawidłowo, ustawiona nieprawidłowo
#obieg wody - powietrze wewnątrz, brak powietrza wewnątrz
#filtr AquaClean - nieprawidłowo przygotowany przed instalacją, prawidłowo przygotowany przed instalacją, zapchany, luźny
#urządzenie - przegrzane, nieprzegrzane

#klasa rozszerzająca KnowledgeEngine
class PhilipsEspressoMachine(KnowledgeEngine):

    #definicja bazy faktów początkowych
    #są one wywoływane przy użyciou metody "reset" 
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

        #prośba wybrania przez użytkownika opcji,
        #która dotyczy elementu
        option=input(
            """Wybierz element:
            1 - całe urządzenie
            2 - lejek kawy
            3 - jednostka zaparzająca
            4 - obieg wody
            5 - filtr AquaClean
            Wybór: """
            )
        
        #definiowany jest nowy fakt,
        #według którego element będzie równy elementowi 
        #wybranemu przez użytkownika
        #Wykorzystana jest tu funkcja wyboru "selectedElement"
        self.declare(Fact(element=self.selectedElement(f'{option}start')))

    #reguła wywoływana pod warunkiem istnienia faktów,
    #według których action='start',
    #element='urządzenie' (wybranym elementem jest cale urządzenie),
    #not state=MATCH.state 
    #(nie został podany jeszcze stan elementu / nie dopasowano stanu)
    @Rule(
        AND(
            Fact(action='start'),
            Fact(element='urządzenie'),
            NOT(Fact(state=MATCH.state))
        )
    )        
    def device(self):
        element='urządzenie'

        #prośba wybrania przez użytkownika opcji,
        #która dotyczy stanu elementu
        option=input(
            f"""Jaki jest stan elementu {element}?:
            1 - przegrzane
            2 - nieprzegrzane
            Wybór: """
            )
        #definiowany jest nowy fakt,
        #według którego stan elementu będzie równy stanowi 
        #wybranemu przez użytkownika
        self.declare(Fact(state=self.selectedElement(f'{option}device')))

    #poniższe reguły są analogiczne do powyższych

    @Rule(
        AND(
            Fact(action='start'),
            Fact(element='lejek kawy'),
            NOT(Fact(state=MATCH.state))
        )
    )        
    def coffeFunnel(self):
        element='lejek kawy'
        option=input(
            f"""Jaki jest stan elementu {element}?:
            1 - luźny
            2 - zapchany
            Wybór: """
            )
        self.declare(Fact(state=self.selectedElement(f'{option}coffeFunnel')))

    @Rule(
        AND(
            Fact(action='start'),
            Fact(element='jednostka zaparzająca'),
            NOT(Fact(state=MATCH.state))
        )
    )        
    def brewingUnit(self):
        element='jednostka zaparzająca'
        option=input(
            f"""Jaki jest stan elementu {element}?:
            1 - brudna
            2 - czysta
            3 - odpowiednio nasmarowana
            4 - nieodpowiednio nasmarowana
            5 - ustawiona prawidłowo
            6 - ustawiona nieprawidłowo
            Wybór: """
            )
        self.declare(Fact(state=self.selectedElement(f'{option}brewingUnit')))

    @Rule(
        AND(
            Fact(action='start'),
            Fact(element='obieg wody'),
            NOT(Fact(state=MATCH.state))
        )
    )        
    def waterCirculation(self):
        element='obieg wody'
        option=input(
            f"""Jaki jest stan elementu {element}?:
            1 - powietrze wewnątrz
            2 - brak powietrza wewnątrz
            Wybór: """
            )
        self.declare(Fact(state=self.selectedElement(f'{option}waterCirculation')))

    @Rule(
        AND(
            Fact(action='start'),
            Fact(element='filtr AquaClean'),
            NOT(Fact(state=MATCH.state))
        )
    )        
    def aquaCleanFilter(self):
        element='filtr AquaClean'
        option=input(
            f"""Jaki jest stan elementu {element}?:
            1 - nieprawidłowo przygotowany przed instalacją
            2 - prawidłowo przygotowany przed instalacją
            3 - zapchany
            4 - luźny
            Wybór: """
            )
        self.declare(Fact(state=self.selectedElement(f'{option}aquaCleanFilter')))


    #reguła wywoływana pod warunkiem istnienia faktów,
    #według których action='start',
    #element=MATCH.element
    #state=MATCH.state 
    #(element i stan zostały podane 
    #i pomyślnie dopasowano ich wartości)
    @Rule(
        AND(
            Fact(action='start'),
            Fact(element=MATCH.element),
            Fact(state=MATCH.state)
        )
    )  
    def printConclusion(self, element, state):
        
        #drukowany jest wniosek,
        #wynikający z podanych 
        #przez użytkownika faktów
        print(f'Wniosek: {element} jest {state}')

    #funkcja zwracająca napis, 
    #w zależności od wybranej przez użytkownika opcji
    #dla danego elementu / dla danej reguły
    def selectedElement(self, option):
        match option:
            case '1start':
                return 'urządzenie'
            case '2start':
                return 'lejek kawy'
            case '3start':
                return 'jednostka zaparzająca'
            case '4start':
                return 'obieg wody'
            case '5start':
                return 'filtr AquaClean'
            case '1device':
                return 'przegrzane'
            case '2device':
                return 'nieprzegrzane'
            case '1coffeFunnel' | '4aquaCleanFilter':
                return 'luźny'
            case '2coffeFunnel' | '3aquaCleanFilter':
                return 'zapchany'
            case '1brewingUnit':
                return 'brudna'
            case '2brewingUnit':
                return 'czysta'
            case '3brewingUnit':
                return 'odpowiednio nasmarowana'
            case '4brewingUnit':
                return 'nieodpowiednio nasmarowana'
            case '5brewingUnit':
                return 'ustawiona prawidłowo'
            case '6brewingUnit':
                return 'ustawiona nieprawidłowo'
            case '1waterCirculation':
                return 'powietrze wewnątrz'
            case '2waterCirculation':
                return 'brak powietrza wewnątrz'
            case '1aquaCleanFilter':
                return 'nieprawidłowo przygotowany przed instalacją'
            case '2aquaCleanFilter':
                return 'prawidłowo przygotowany przed instalacją'
            case _:
                return None

if __name__ == '__main__':

    #stworzenie instancji PhilipsEspressoMachine
    engine=PhilipsEspressoMachine()

    #wykonanie funkcji reset
    engine.reset()

    #wykonanie funkcji run
    engine.run()