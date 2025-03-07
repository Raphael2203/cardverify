def get_card_brand(card_number):
    """
    Identifica a bandeira do cartão de crédito com base no número do cartão.
    
    :param card_number: Número do cartão de crédito como string
    :return: Nome da bandeira do cartão ou 'Desconhecida' se não for possível identificar
    """
    card_number = card_number.replace(" ", "")
    
    if card_number.startswith(('34', '37')) and len(card_number) == 15:
        return "American Express"
    elif card_number.startswith('4') and len(card_number) in [13, 16, 19]:
        return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')) and len(card_number) == 16:
        return "MasterCard"
    elif card_number.startswith('6011') or card_number.startswith(('622126', '622925')) or card_number.startswith(('644', '645', '646', '647', '648', '649')) or card_number.startswith('65') and len(card_number) == 16:
        return "Discover"
    elif card_number.startswith('35') and len(card_number) == 16:
        return "JCB"
    elif card_number.startswith('3') and len(card_number) == 14:
        return "Diners Club"
    elif card_number.startswith('2014') or card_number.startswith('2149') and len(card_number) == 15:
        return "Enroute"
    elif card_number.startswith('8699') and len(card_number) == 15:
        return "Voyager"
    elif card_number.startswith('606282') or card_number.startswith('384100') or card_number.startswith('384140') or card_number.startswith('384160') and len(card_number) == 16:
        return "Hipercard"
    elif card_number.startswith('50') and len(card_number) == 16:
        return "Aura"
    else:
        return "Desconhecida"

# Exemplo de uso
if __name__ == "__main__":
    card_number = "3011 024188 5087"  # Exemplo de número de cartão de crédito
    brand = get_card_brand(card_number)
    print(f"A bandeira do cartão é: {brand}")