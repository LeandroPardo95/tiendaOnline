
def total_carro(request):
    cant = 0
    total = 0
    if not request.session.get('carro'):
        request.session['carro']={}

    for key,value in request.session['carro'].items():
        cant+=1
        total += value['precio_total']

    return {
        'total_carro':total,
        'cant_carro':cant,
        }