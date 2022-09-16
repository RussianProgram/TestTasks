from transitions import Machine

class PizzaOrder:
    size = None
    payment = None
    message = None

    def __init__(self,name):
        self.name = name

    def choose_size(self):
        self.size = self.state
        self.message = 'Оплата Наличкой или Банковской картой?'

    def choose_payment(self):
        self.payment = self.state
        self.message = f'Вы хотите {self.size} пиццу, оплата - {self.payment}?'

    def clear_order(self):
        self.size = None
        self.payment = None
        self.message = 'Чтобы заказать снова, нажмите /start'





states = [
    'Ждем заказ',
    'Заказ в обработке',
    'Большую',
    'Маленькую',
    'Наличкой',
    'Банковской картой',
]

transitions = [
    {'trigger':'start_taking_order',
     'source':'Ждем заказ',
     'dest':'Заказ в обработке'},

    {'trigger':'big',
     'source':'Заказ в обработке',
     'dest':'Большую',
     'after':'choose_size'},

    {'trigger':'small',
     'source':'Заказ в обработке',
     'dest':'Маленькую',
     'after':'choose_size'},

    {'trigger':'cash',
     'source':['Большую','Маленькую'],
     'dest':'Наличкой',
     'after':'choose_payment'},

    {'trigger':'with_card',
     'source':['Большую','Маленькую'],
     'dest':'Банковской картой',
     'after':'choose_payment'},

    {'trigger':'yes',
     'source':['Банковской картой','Наличкой'],
     'dest':'Ждем заказ',
     'after':'clear_order'},

    {'trigger':'no',
     'source':['Банковской картой','Наличкой'],
     'dest':'Ждем заказ',
     'after':'clear_order'},

]

cashier = PizzaOrder('Sergey')
machine = Machine(cashier,states=states,transitions=transitions,initial='Ждем заказ')



