import text1,text2,text3

if __name__ == '__main__':
    name = "耳机"
    good_list = text3.get_good(name)
    good_urlList = []
    #for index in range(len(good_list)):
    good_urlList.append(text1.get_good(good_list[0]['商品名称']))
    good_urlList.append(text1.get_good(good_list[1]['商品名称']))
    for index in range(len(good_urlList)):
        text2.mmm(good_urlList[index])