"""

2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
 Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
 Проверить на практике полученные на этом уроке знания:
  реализовать абстрактные классы для основных классов проекта,
  проверить на практике работу декоратора @property.

"""


class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def sguare_c(self):
        return self.width / 6.5 + 0.5

    def sguare_j(self):
        return self.height * 2 + 0.3

    @property
    def sguare_full(self):
        return str(f'Общая площадь ткани \n'
                   f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.sguare_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто \n\t{self.sguare_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.sguare_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм \n\t{self.sguare_j}'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.sguare_full)
print(jacket.sguare_full)
print(jacket.sguare_c())
print(coat.sguare_j())