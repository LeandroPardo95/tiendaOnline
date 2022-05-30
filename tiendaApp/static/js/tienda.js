import {load_Cart} from "./carro.js";
import load_Products from "./productos.js";

load_Products('.tienda','#template-card')
load_Cart('/tienda/operar','#load_Cart','.carrito')