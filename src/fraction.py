from auxiliary import sign, mdc

class Fraction:
    # Cria uma fração com os valores de numerador e denominador dados. Por
    # padrão, o valor 0 é utilizado
    def __init__(self, numerator = 0, denominator = 1):
        self._numerator = numerator
        self._denominator = denominator
        self._sign = sign(numerator) * sign(denominator)
    
    # Retorna a fração inversa da atual
    def inverse(self) -> 'Fraction':
        return Fraction(self._denominator, self._numerator)
    
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
    
    # Retorna a forma simplificada (irredutível) da fração atual
    def simplify(self) -> 'Fraction':
        divisor = mdc(self._numerator, self._denominator)
        return Fraction(self._numerator // divisor, self._denominator // divisor)
    
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
    def __lte__(self, f2: 'Fraction') -> bool:
        return (self < f2) or (self == f2)
    
    # Operador para verificar se a fração atual é maior ou igual que a fração dada
    def __gte__(self, f2: 'Fraction') -> bool:
        return (self > f2) or (self == f2)
