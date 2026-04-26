def greetings(name = 'noble stranger'):
    if isinstance(name,str):
        print('hello' , name)
    else:
        print('error')
        
if __name__ == '__main__':
    greetings('winston')
    greetings('john')
    greetings()
    greetings(42)


