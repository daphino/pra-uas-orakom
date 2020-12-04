"""
ToDo:
  - Membuat input (bilangan desimal)
  - Membuat step-by-step proses konversi bilangan desimal ke bil. Binner, 
    Hexa, Octal
    - Rumus decimal ke biner : bil % 2
    - Rumus decimal ke octal : bil % 8
    - Rumus decimal ke hexa : bil % 16
  - Melakukan perulangan sampai user melakukan exit program
"""

import os

def steps(number=0):
  # Inisialiasi base biner, octal, dan hexa
  baseBiner = 2
  baseOctal = 8
  baseHexa = 16

  resultBiner = ''
  resultOctal = ''
  resultHexa = ''

  numberForBinner = number
  numberForOctal = number
  numberForHexa = number

  while numberForBinner > 0:
    outputHeadHexa = f'{toHexa(numberForHexa)}' if numberForHexa > 0 else ""
    print(
        f'{numberForBinner}'.center(16), # Column 1
        f'{numberForOctal if numberForOctal > 0 else ""}'.center(16), # Column 2
        f'{outputHeadHexa}'.center(16) # Column 3
    )

    outputBiner = f'{baseBiner} ---- {numberForBinner % baseBiner}' if numberForBinner > (baseBiner-1) else ""
    outputOctal = f'{baseOctal} ---- {numberForOctal % baseOctal}' if numberForOctal > (baseOctal-1) else ""
    outputHexa = f'{baseHexa} ---- {toHexa(numberForHexa % baseHexa)}' if numberForHexa > (baseHexa-1) else ""

    print(
      f'{outputBiner}'.center(16), #Column 1
      f'{outputOctal}'.center(16), #Column 2
      f'{outputHexa}'.center(16), #Column 3
    )

    resultBiner = f'{numberForBinner%baseBiner}{resultBiner}'
    resultOctal = f'{(numberForOctal%baseOctal) if numberForOctal>0 else ""}{resultOctal}'
    resultHexa = f'{toHexa(numberForHexa%baseHexa) if numberForHexa > 0 else ""}{resultHexa}'

    numberForBinner //= baseBiner
    numberForOctal //= baseOctal
    numberForHexa //= baseHexa

  return resultBiner,resultOctal,resultHexa

def toHexa(number=0):
  if number > 15: return number
  formatHexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9', 'A', 'B', 'C', 'D', 'E', 'F'][number]
  return formatHexa

def main():
  # Lakukan perulangan terus-menerus sampai user menghentikan program
  while True:
    # Cetak judul dan deskripsi program
    print('Aplikasi Konversi Sederhana'.center(50, '='))
    print('Program sederhana untuk konversi bilangan\ndesimal ke biner,octal, dan hexa')
    print('='*50)

    try:
      # Membuat input dari user untuk memasukkan bilangan desimal
      number = int(input('Masukkan bilangan desimal : '))

      # Cetak header table
      print('Biner'.center(16), 'Octal'.center(16), 'Hexa'.center(16))

      resultBinner, resultOctal, resultHexa = steps(number)

      print('='*50)
      print(
          f'Biner = {resultBinner}'.center(16),  # column 1
          f'Octal = {resultOctal}'.center(16),  # column 2
          f'Hexa = {resultHexa}'.center(16),  # column 3
      )

      print();repeat = input('Program selesai. Ulangi ? [Y=Yes | N=No] ? ')
      if repeat in ['Y', 'y', 'Yes', 'YES', 'YEs', 'yes', 'yES', 'yeS']:
        clearTerminal()
        continue
      else:
        break

    except:
      print();repeat = input('Masukkan bilangan yang benar !. Ulangi [Y=Yes | N=No] ? ')
      if repeat in ['Y', 'y', 'Yes', 'YES', 'YEs', 'yes', 'yES', 'yeS']:
        clearTerminal()
        continue
      else:break

def clearTerminal():
  os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
