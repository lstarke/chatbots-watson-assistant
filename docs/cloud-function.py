#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
import sys

def main(dict):
    
    result = {}
    
    if 'cadastro' in dict:
        cadastro = dict['cadastro']
        if cadastro == "1071":
            result =  {
                "erro": False,
                "nome":"Leandro Starke",
                "saldo_ferias": 10
            }
        elif cadastro == "1070":
            result = {
                "erro": False,
                "nome":"Peter Riemer",
                "saldo_ferias": 30
            }
        elif cadastro == "418":
            result = {
                "erro": False,
                "nome":"Klaus Fontana",
                "saldo_ferias": 20
            }    
        else:
            result = {
                "erro": True,
                "nome":"Desconhecido",
                "saldo_ferias": 0
            }
    elif 'meio' in dict:
        meio = dict['meio']
        if meio == "agua":
            result = {
                "erro": False,
                "borracha": "286"
            }
        elif meio == "aditivo":
            result = {
                "erro": False,
                "borracha": "SBE"
            }
        elif meio == "amido cozido":
            result = {
                "erro": False,
                "borracha": "451"
            }
        elif meio == "lodo":
            result = {
                "erro": False,
                "borracha": "PCI"
            }    
        elif meio == "polpa de fruta":
            result = {
                "erro": True,
                "borracha": "SBBPF"
            }
        else:
            result = {
                "erro": True,
                "borracha": "Desconhecida"
            }

    return result