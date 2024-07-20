class Widget():
    def __init__(self,text,x,y):
        self.x = x
        self.y = y 
        self.text = text
    def print_info(self):
        print('інформація про віджет')    
        print(self.text,self.x,self.y)
class Button(Widget):
    def __init__(self, text,x,y,is_click):
        super().__init__(text,x,y)
        self.is_click = is_click    
    def click(self):
        print("ти людина")
        self is_click = 1
adolf = Button("я адольф", 56,14,False)     
adolf.print_info()
a=input('а ти адольф').lover
if a == 'так':
    adolf.click()
                     