#!/usr/local/bin/python3
def main():
    cases = open('./input.txt', 'r').read().splitlines()
    labels = [ 'Prima', '1', '2', '3', '4', '5', '6', '7', '8',
    '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '20', '21', '22', '23', '27', '29', '30', '31', '32', '33',
    '34', '35', '36' ]
    labels = [ 'C. ' + item + ', d.init.' for item in labels]
    print("listofdicts = [")
    for i in range(len(cases)):
        print("{ 'project': 'Gratian',", end = ' ')
        print("'source': 'Sg',", end = ' ')
        print("'label': '" + labels[i] + "',", end = ' ')
        print("'text': '''" + cases[i] + "''' },")
    print("]")

if __name__ == '__main__':
    main()
