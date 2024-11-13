print('Type in the list of criminal records below: ')

def main():
    while True:
        name = input('Type in the name of the individual here: ')
        drug_usage = input('Has individual consumed drugs? (Y/N) ')
        murder = input('Has individual committed murder before? (Y/N) ')
        tax_fraud = input('Has individual committed tax fraud before? (Y/N) ')

        if drug_usage == 'Y':
            drug_use = True
        elif drug_usage == 'N':
            drug_use = False

        if murder == 'Y':
            kill = True
        elif murder == 'N':
            kill = False

        if tax_fraud == 'Y':
            fraud = True
        elif tax_fraud == 'N':
            fraud = False

        if drug_use or kill or fraud:
            print(f'{name} is a criminal')
        else:
            print(f'{name} is not a criminal')


    
main()


        





        
