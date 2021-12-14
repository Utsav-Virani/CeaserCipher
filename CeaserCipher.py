def main():
    _inputText = input("Enter the cipher text : ")
    _inputText=str(_inputText).upper()
    _inputTextList=[]
    _inputTextList[:0]=_inputText
    # print(_inputTextList)
    _inputTextObj = {  }
    for i in _inputTextList:
        if(i in _inputTextObj.keys):
            _inputTextObj[i] +=1
        _inputTextObj[i] =1
    print(_inputTextObj)

  


if __name__=="__main__":
    main()


# uzqsovuohxm