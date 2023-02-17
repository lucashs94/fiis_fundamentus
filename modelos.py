

class FundoImobiliario:
    
    def __init__(self, codigo, segmento, cotacao_atual, ffo_yield, dividend_yield, p_pv, valor_mercado, liquidez, qt_imoveis, preco_m2,
                 aluguel_m2, cap_rate, vacancia_media):
        
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao_atual = cotacao_atual
        self.ffo_yield = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_pv = p_pv
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qt_imoveis = qt_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia_media = vacancia_media
        
        
        
class Estrategia:
    
    def __init__(self, segmento="", cotacao_atual_minima=0, ffo_yield_minimo=0, dividend_yield_minimo=0, p_pv_minimo=0, valor_mercado_minimo=0,
                 liquidez_minima=0, qt_imoveis_minima=0, preco_m2_minimo=0, aluguel_m2_minimo=0, cap_rate_minimo=0, vacancia_maxima=0):
        self.segmento = segmento
        self.cotacao_atual_minima = cotacao_atual_minima
        self.ffo_yield_minimo = ffo_yield_minimo
        self.dividend_yield_minimo = dividend_yield_minimo
        self.p_pv_minimo = p_pv_minimo
        self.valor_mercado_minimo = valor_mercado_minimo
        self.liquidez_minima = liquidez_minima
        self.qt_imoveis_minima = qt_imoveis_minima
        self.preco_m2_minimo = preco_m2_minimo
        self.aluguel_m2_minimo = aluguel_m2_minimo
        self.cap_rate_minimo = cap_rate_minimo
        self.vacancia_maxima = vacancia_maxima
    
    
    def aplica_estrategia(self, fundo: FundoImobiliario):
        if self.segmento != '':
            if fundo.segmento != self.segmento:
                return False
        
        if fundo.cotacao_atual < self.cotacao_atual_minima \
            or fundo.ffo_yield < self.ffo_yield_minimo \
            or fundo.dividend_yield < self.dividend_yield_minimo \
            or fundo.p_pv < self.p_pv_minimo \
            or fundo.valor_mercado < self.valor_mercado_minimo \
            or fundo.liquidez < self.liquidez_minima \
            or fundo.qt_imoveis < self.qt_imoveis_minima \
            or fundo.preco_m2 < self.preco_m2_minimo \
            or fundo.aluguel_m2 < self.aluguel_m2_minimo \
            or fundo.cap_rate < self.cap_rate_minimo \
            or fundo.vacancia_media > self.vacancia_maxima:
                
            return False
        else:
            return True    
        