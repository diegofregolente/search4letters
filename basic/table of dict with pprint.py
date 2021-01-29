import pprint

people = {}
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'
                  }

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-maker',
                    'Home Planet': 'Earth'
                    }

people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematician',
                      'Home Planet': 'Earth'
                      }

people['Robot'] = {'Name': 'Marvin',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknow'
                   }

pprint.pprint(people) # mostra as estruturas de dados de forma bonita

print(people["Robot"]['Occupation']) # Mostra a ocupação de robo em people
