def generateDictionary(n):
    dic = {}
    for i in range(n):
        word = input("프로그래밍 언어 이름: ")
        desc = input("프로그래밍 언어 설명: ")
        dic[word] = desc
    print(word)
    print(desc)
    return dic


def translateDictionary(dic):
    new_dic = {}

    for word in dic:
        print("=====영어사전생성=======")
        print("description: ", dic[word])
        new_word = input("Input the name of the language in English:")
        new_desc = input("Input the description of the language in English: ")
        new_dic[new_word] = new_desc
    return new_dic


def searchDictionary(dic):
    search_dic = {}
    for keyword in dic:
        while (1):
            search = input("Enter a word for search: ")
            if (search in str(dic[keyword])):
                print("Search result: ['"+ keyword+"']")
            elif(search in str(dic[keyword])):
                print("Search result: ['"+ keyword+"', '" +keyword+"']")
            elif (search in str(dic[keyword])):
                print("Search result: ['" + keyword + "', '" + keyword +"', '"+ keyword+"']")
            elif (search in str(dic[keyword])):
                print("Search result: ['" + keyword + "']")
            else:
                print("No match!! Break!")
                break

        return  search_dic


n = int(input("Input number of programing language: "))
dic = generateDictionary(n)
new_dic = translateDictionary(dic)
search_dic = searchDictionary(dic)
print(dic)
print(new_dic)
