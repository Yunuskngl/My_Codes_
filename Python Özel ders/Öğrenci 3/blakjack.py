def ranks():
    return ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']




def score(hand):
    #kart rütbeleri tanımlama
    values = {'2' : 2 ,'3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 , '7' : 7 , '8' : 8, '9' : 9 , '10' : 10 , 'J' : 10 , 'Q' : 10 , 'K' : 10,'A': 11}
    
    #elin toplam puanını ve As sayısını başlatır.
    result =0 
    aces= 0
    
    #eldeki her kart için puan ekler ve as sayısını arttırır
    for card in hand:
        result +=values[card.rank]
        if card.rank == 'A':
            aces +=1
            
    #eğer toplam puan 21'i geçiyorsa ve en az bir as varsa , aces sayısını 1'e indirir . 1 olarak sayar yani.
    while result > 21 and aces>=1:
        result -=10
        aces -=1
    #hesaplanan tutar 
    return result 
    