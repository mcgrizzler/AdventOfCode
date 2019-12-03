import os

inputList = ['142156\n', '108763\n', '77236\n', '78186\n', '110145\n', '126414\n', '115436\n', '133275\n', '132634\n', '82606\n', '118669\n', '90307\n', '134124\n', '102597\n', '128607\n', '109214\n', '50160\n', '72539\n', '99033\n', '145334\n', '135409\n', '97525\n', '109865\n', '142319\n', '79027\n', '96924\n', '72530\n', '85993\n', '109594\n', '115991\n', '107998\n', '112934\n', '85198\n', '112744\n', '129637\n', '95515\n', '90804\n', '107052\n', '89707\n', '93658\n', '60115\n', '118752\n', '94315\n', '59645\n', '115668\n', '139320\n', '70734\n', '56771\n', '74741\n', '69284\n', '92228\n', '145376\n', '103317\n', '55143\n', '58370\n', '54873\n', '52424\n', '95392\n', '67892\n', '90858\n', '74693\n', '77363\n', '51496\n', '79375\n', '71206\n', '103492\n', '94065\n', '72084\n', '144311\n', '67381\n', '129958\n', '86741\n', '148906\n', '123383\n', '147575\n', '136327\n', '118108\n', '136529\n', '66356\n', '70746\n', '147569\n', '107267\n', '122434\n', '69688\n', '122127\n', '94072\n', '110203\n', '50546\n', '57836\n', '139334\n', '113240\n', '96729\n', '68516\n', '74635\n', '126951\n', '138948\n', '88312\n', '101477\n', '129730\n', '93816']


def partTwo(mass):
    return (int(mass) // 3) - 2

def openFile():
    inFile = open('data2.txt', 'r')
    lines = inFile.readlines()
    inFile.close()
    lines = map(lambda s: s.strip('\n'), inputList)
    return lines

def processFuel(intialMass):
    result = 0
    temp = intialMass
    done = False

    while not done:
        temp = partTwo(temp)

        if temp <= 0:
            #result += temp
            done = True
            return result
        
        else: 
            result += temp
            done = False
        

    return result
    

def main(inputList):
    result = 0
    inputList = map(lambda s: s.strip('\n'), inputList)
    print()
    for i in inputList:
        print('Input: {}\nOutput: {}'.format(i ,processFuel(i)))
        result += processFuel(i)
    return result

print(main(inputList))

