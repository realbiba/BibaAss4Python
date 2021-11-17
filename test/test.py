from CoinInfo import CoinInfo

scrapper = CoinInfo()

num = 1
for i in scrapper.get_paragraphs('bitcoin'):
    print(str(num) + ")     Title : " + i['title'] + ".\n    Link: "+ i['link'])
    print("Briefly: " + i['body'])
    print("############################################################################################################")
    num+=1