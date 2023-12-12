_sourceFile = open('Day7\\input.txt', 'r')
_lines = _sourceFile.readlines()
camelCards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
handSize = 5

def CalculateHandRank(hand):
    digitPlace = handSize
    totalRank = 0
    for card in hand:
        totalRank += (camelCards.index(card)+1) * pow(len(camelCards), digitPlace)
        digitPlace -= 1
    return totalRank
# end CalculateHandRank

def DetermineHand(hand):
    handCount = {}
    for itr in range(len(hand)):
        if hand[itr] not in handCount.keys():
            handCount[hand[itr]] = 1
        else:
            handCount[hand[itr]] += 1
    
    if len(handCount) == 1:
        return 7 #5Kind
    elif len(handCount) == 2:
        for key in handCount.keys():
            if 'J' in hand: 
                return 7 # 4Kind & FullHouse + J = 5Kind
            if handCount[key] == 4 or handCount[key] == 1:
                return 6 # 4Kind
            return 5 # FullHouse
    elif len(handCount) == 3:
        for key in handCount.keys():
            if handCount[key] == 3:
                if 'J' in hand: # 3Kind + J = 4Kind
                    return 6
                return 4 # 3Kind
        if 'J' in hand: # 2Pair + J = EITHER 4kind (JJ998) or FullHouse (9988J)
            if (handCount['J'] == 2):
                return 6
            return 5
        return 3 # 2Pair
    elif len(handCount) == 4:
        if 'J' in hand: # Pair + J = 3Kind
            return 4
        return 2 # Pair
    if 'J' in hand: # High + J = Pair
        return 2
    return 1 # High
# end DetermineHand

camelHands = []
for line in _lines:
    hand = line.rsplit(' ')[0]
    bet = line.rsplit(' ')[1]
    handType = DetermineHand(hand)
    handRank = CalculateHandRank(hand)
    camelHands.append(str(handType) + ':' + str(handRank) + ';' + hand + ' ' + bet)

camelHands.sort(key=lambda x:(x[0], int(x.split(':')[1].split(';')[0])))
bidTotal = 0
for idx in range(len(camelHands)):
    bid = int(camelHands[idx].split(' ')[1])
    bidTotal += bid * (idx+1)

print(bidTotal)