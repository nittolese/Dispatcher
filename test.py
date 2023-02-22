from dispatcher import dispatcher

@dispatcher
def foo():
    raise NotImplementedError("This method has not been implementated on purpose.")

@foo.register
def _(dimension: str, expression: str, operator: str, append: bool):
    print('')
    print("dimension: str, expression: str, operator: str, append: bool")
    print(f"dimension: {dimension}, expression: {expression}, operator: {operator}, append: {append}")    

@foo.register
def _(arg:int):
    print('')
    print("arg:int")
    print(f"arg:{arg}")
    
@foo.register
def _(arg:list):
    print('')
    print("arg:list")
    print(f"arg:{arg}")
    pass

# @foo.register
# def _(arg:str):
#     print('')
#     print("arg:str")
#     print(f"arg:{arg}")

@foo.register
def _(country:str = ''):
    print('')
    print("country:str")
    print(f"country:{country}")

@foo.register
def _(country, operator, append):
    print('')
    print("country, operator, append")
    print(f"{country}, {operator}, {append}")

@foo.register
def _(country: str, operator: str = 'and', append: bool = False):
    print('')
    print("country: str, operator: str = 'and', append: bool = False")
    print(f"country: {country}, operator: {operator}, append: {append}")


if __name__ == '__main__':
    # Expected to call arg:list - Dispatch to existing method
    # If the method does not exist, it calls arg:str
    # Dispatch to a generic alternative
    foo([1, 2, 3])
    
    # Expected to call arg:int - Dispatch to existing method
    # 
    foo(1)
        
    # Expected to call (country, operator, append)
    foo('a', 'b', 'c')
    foo(1, 2, 3)

    # Expected to call (arg: str) if not commented
    # else (country: str, operator: str = 'and', append: bool = False)
    # The two method cannot exist together
    foo('test') 

    # Expected to call (country: str)
    foo(country='test') 

    # Expected to call (country: str, operator: str, append: bool) 
    # receiving country = test, operator = 'tt' and defaulting the append to False
    foo('test', 'lalal')