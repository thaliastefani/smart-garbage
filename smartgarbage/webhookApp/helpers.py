class Helpers():

    def __init__(self):
        pass

    def waste_types(self):
      waste_types = [
        {
          "value": "tipo organico",
          "synonyms": [
            "tipo organico",
            "restos de comida",
            "caroço",
            "casca",
            "alimento estragado",
            "resto",
            "chá",
            "café",
            "caroço de fruta",
            "casca de banana"
          ]
        },
        {
          "value": "tipo papel",
          "synonyms": [
            "tipo papel",
            "jornal",
            "revista",
            "jornais",
            "papelão",
            "folha de sulfite",
            "folha de caderno",
            "envelope",
            "caixa de papelão"
          ]
        },
        {
          "value": "tipo metal",
          "synonyms": [
            "tipo metal",
            "tampa de garrafa",
            "material de aço",
            "clipes",
            "grampo",
            "lata de aluminio",
            "latinha de refrigerante",
            "lata de refrigerante"
          ]
        },
        {
          "value": "tipo plastico",
          "synonyms": [
            "tipo plastico",
            "garrafa pet",
            "embalagem de plastico",
            "sacos"
          ]
        },
        {
          "value": "tipo vidro",
          "synonyms": [
            "tipo vidro",
            "copo de vidro",
            "garrafa de vidro",
            "pote de vidro",
            "frasco de medicamento",
            "perfume",
            "material de vidro",
            "frasco de perfume"
          ]
        }
      ]

      return waste_types

    def trash_types(self):
      trash_types = [
        {
          "value": "lixeira de papel",
          "synonyms": [
            "papeis",
            "papel",
            "lixeira de papel",
            "lixo para papel",
            "lixeira de papeis",
            "lixo de papel"
          ]
        },
        {
          "value": "lixeira de metal",
          "synonyms": [
            "metais",
            "metal",
            "lixeira de metal",
            "lixo para metal",
            "lixeira de metais"
          ]
        },
        {
          "value": "lixeira de plastico",
          "synonyms": [
            "plasticos",
            "plastico",
            "lixeira de plastico",
            "lixo para plastico",
            "lixo de plasticos"
          ]
        },
        {
          "value": "lixeira de vidro",
          "synonyms": [
            "vidros",
            "vidro",
            "lixeira de vidro",
            "lixo para vidro",
            "lixeira de vidros"
          ]
        },
        {
          "value": "lixeira de organico",
          "synonyms": [
            "organicos",
            "organico",
            "lixeira de organico",
            "lixo para organico",
            "lixo organico"
          ]
        }
      ]

      return trash_types

    def verify_param(self, type_synonyms, param):
      synonyms = type_synonyms

      for synonym in synonyms:
          if synonym == param:
            return True
