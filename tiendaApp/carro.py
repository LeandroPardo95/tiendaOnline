


class Carro():
    def __init__(self, request):
        self.request = request
        self.session = self.request.session

        carro = self.session.get('carro')

        if not carro:
            carro = self.session['carro'] = {}

        self.carro = carro

    def add_Prod(self, producto):

        if (str(producto.id) not in self.carro.keys()):

            self.carro[producto.id] = {
                'id':producto.id,
                'nombre':producto.name,
                'cantidad': 1,
            }
        else:
            for key,value in self.carro.items():

                if key == str(producto.id):
                    value['cantidad'] +=1
                    break
        
        self.save_cart()
        
    
    def save_cart(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def clear_cart(self):
        self.session['carro'] = {}

        

        