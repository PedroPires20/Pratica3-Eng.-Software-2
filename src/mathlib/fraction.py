import re
from .auxiliary import sign, mdc

FRACTION_RPR_REGEX = r"((-)?\d+)(\/((-)?\d+))?"

class Fraction:
    # Cria uma fração com os valores de numerador e denominador dados. Por
    # padrão, o valor 0 é utilizado
    def __init__(self, numerator = 0, denominator = 1):
        self._numerator = abs(numerator)
        self._denominator = abs(denominator)
        self._sign = sign(numerator) * sign(denominator)
        self.__simplify()
    
    # Cria uma fração a partir de uma string no formato "a/b" ou "a", em que
    # a e b são inteiros
    @staticmethod
    def from_string(str_rpr: str) -> 'Fraction':
        regex_match = re.match(FRACTION_RPR_REGEX, str_rpr)
        if not regex_match:
            raise None
        numerator = int(regex_match.group(1))
        if regex_match.group(4):
            denominator = int(regex_match.group(4))
        else:
            denominator = 1
        return Fraction(numerator, denominator)
    
    # Retorna a fração inversa da atual
    def inverse(self) -> 'Fraction':
        return Fraction(self._denominator * self._sign, self._numerator)
    
    # Retorna o valor do numerador da fração atual
    def numerator(self) -> int:
        return self._numerator
    
    # Retorna o denominador da fração atual
    def denominator(self) -> int:
        return self._denominator
    
    # Retorna o sinal da fração atual (-1 para negativo e 1 para positivo)
    def sign(self) -> int:
        return self._sign
    
    # Retorna o valor de ponto flutuante correspondente à fração atual
    def to_float(self) -> float:
        return (self._numerator / self._denominator) * self._sign
    
    # Verifica se a fração atual representa um inteiro
    def is_integer(self) -> bool:
        return  self._denominator == 1
    
    # Retorna a representação da fração atual como uma string. Se a fração
    # atual possui denominador 1, a representação do inteiro correspondente 
    # é retornada
    def __str__(self) -> str:
        if self._denominator == 1:
            return str(self._sign * self._numerator)
        return f"{self._sign * self._numerator}/{self._denominator}"

    # Operador para calcular o oposto da fração atual
    def __neg__(self) -> 'Fraction':
        return Fraction(-self._numerator, self._denominator)

    # Operador para adição de duas frações
    def __add__(self, f2: 'Fraction') -> 'Fraction':
        sum_numerator = (self._numerator * f2._denominator) + (f2._numerator * self._denominator)
        sum_denominator = self._denominator * f2._denominator
        return Fraction(sum_numerator, sum_denominator)
    
    # Operador para subtração de duas frações
    def __sub__(self, f2: 'Fraction') -> 'Fraction':
        sum_numerator = (self._numerator * f2._denominator) - (f2._numerator * self._denominator)
        sum_denominator = self._denominator * f2._denominator
        return Fraction(sum_numerator, sum_denominator)

    # Operador para multiplicação de duas frações
    def __mul__(self, f2: 'Fraction') -> 'Fraction':
        result_sign = self._sign * f2._sign
        return Fraction(self._numerator * f2._numerator * result_sign, self._denominator * f2._denominator)
    
    # Operador para divisão de duas frações
    def __truediv__(self, f2: 'Fraction') -> 'Fraction':
        return self * f2.inverse()

    # Operador para verificar se duas frações são iguais
    def __eq__(self, f2: 'Fraction') -> bool:
        return (self._sign == f2._sign) and (self._numerator == f2._numerator) and (self._denominator == f2._denominator)

    # Operador para verificar se duas frações são diferentes
    def __neq__(self, f2: 'Fraction') -> bool:
        return not (self == f2)
    
    # Operador para verificar se a fração atual é menor que a fração dada
    def __lt__(self, f2: 'Fraction') -> bool:
        return self.to_float() < f2.to_float()
    
    # Operador para verificar se a fração atual é maior que a fração dada
    def __gt__(self, f2: 'Fraction') -> bool:
        return self.to_float() > f2.to_float()
    
    # Operador para verificar se a fração atual é menor ou igual que a fração dada
    def __le__(self, f2: 'Fraction') -> bool:
        return (self < f2) or (self == f2)
    
    # Operador para verificar se a fração atual é maior ou igual que a fração dada
    def __ge__(self, f2: 'Fraction') -> bool:
        return (self > f2) or (self == f2)
    
    # Simplifica a fração atual
    def __simplify(self) -> 'Fraction':
        divisor = mdc(self._numerator, self._denominator)
        self._numerator //= divisor
        self._denominator //= divisor
