class Fecha:
    def __init__(self, dia, mes, anio):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    @property
    def dias(self):
        return self.__dia

    @dias.setter
    def dias(self, dia):
        self.__dia = dia

    @property
    def meses(self):
        return self.__mes

    @meses.setter
    def meses(self, mes):
        self.__mes = mes

    @property
    def anios(self):
        return self.__anio

    @anios.setter
    def anios(self, anio):
        self.__anio = anio

    def valida(self):
        if (self.__dia < 1) or (self.__dia > 31):
            return False

        if (self.__mes < 1) or (self.__mes > 12):
            return False

        diasMes = self.diasMes()

        if (self.__dia > diasMes):
            return False
        else:
            return True

    def diasMes(self):
        # determinamos la cantidad de días del mes
        diasMes = 0
        if self.__mes in (1, 3, 5, 7, 8, 10, 12):
            diasMes = 31
        elif self.__mes in (4, 6, 9, 11):
            diasMes = 30
        elif self.__mes == 2:
            diasMes = self.esBisitesto(diasMes)
        return diasMes

    def esBisitesto(self, diasMes):
        # verificación de año bisiesto
        esAnioMultipo400 = self.__anio % 400 == 0
        esMultiplo4NoDe100 = (self.__anio % 4 == 0) and (self.__anio % 100 != 0)
        if (esAnioMultipo400) or (esMultiplo4NoDe100):
            diasMes = 29
        else:
            diasMes = 28
        return diasMes


if __name__ == '__main__':
    fecha = Fecha(12, 12, 1945)

    if (fecha.valida()):
        print("fecha es valida")
    else:
        print("La fecha no es valida")

    fecha.dias = 31
    fecha.meses = 11
    fecha.anios = 2023
    if (fecha.valida()):
        print("fecha es valida")
    else:
        print("La fecha no es valida")
