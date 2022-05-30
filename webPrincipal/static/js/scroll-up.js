export default function scroll_Up(btn) {

    const $btn = document.querySelector(btn);


    document.addEventListener('scroll', (e) => {
        let scroll = window.scrollY;
        if (scroll > 300) $btn.classList.remove('hidden');
        if (scroll < 300) $btn.classList.add('hidden')
    })

    document.addEventListener('click', (e) => {
        if (e.target.matches(btn)) window.scrollTo({top:0})
    })



}