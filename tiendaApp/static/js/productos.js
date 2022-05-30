const d = document;

export default function load_Products(parent,template){

    const $template = d.getElementById(template).content,
        $parent = d.querySelector(parent),
        $fragment = d.createDocumentFragment();


    fetch("http://localhost:8000/tienda/operar/")

    .then((res)=> {
        //console.log(res)
        return res.json()
    })
    .then((json) =>{
        let jd = json.Productos

        jd.forEach(el => {
            
            $template.querySelector('.precio').textContent = '$'+el.price;
            $template.querySelector('.detalle').textContent = el.name;
            $template.querySelector('img').setAttribute('src','/media/'+el.image);
            $template.querySelector('img').setAttribute('alt', el.name)


            let $clone = d.importNode($template,true)

            $fragment.appendChild($clone)

        });

        $parent.appendChild($fragment)

    })
    
}