const d = document, w = window;

export function load_Cart(jsonCarro,btn, div) {

    const $carro = d.querySelector(div),
        $btn = d.querySelector(btn),
        $fragment = d.createDocumentFragment(),
        $template = d.getElementById('template-carro').content;

    //console.log($template)

//************* FUNCION PARA CARGAR CARRO
    function load(){
        fetch('http://localhost:8000/tienda/api/carrito/')

            .then((respuesta) => {
                console.log('dentro del primer then')
                return respuesta.json()
            })//fin del primer then
    
            .then((json) => {
                console.log(json.productos)

                json.productos.forEach(el => {

                    let $item = $template.querySelector('.item-carro');

                    console.log($item)

                    $item.textContent = `${el.nombre} - ${el.cantidad}`

                    let $clone = d.importNode($template, true)

                    $fragment.appendChild($clone)
                    
                });

                $carro.innerHTML = '';
                $carro.appendChild($fragment);


            })//fin del segundo then
    
            .catch()
            .finally(
                () => {
                    let p = d.createElement('p');
                    const hora = new Date();

                    p.textContent = `Ultima actualización: ${hora.toLocaleTimeString()}.`

                    $carro.appendChild(p)
            })
    } // AUTOEJECUTABLE
// ********************** FIN DE FUNCION LOAD
    

    d.addEventListener('click', (e)=> {
        if (e.target.matches(btn)) {
            load()
        }
    })
    
}