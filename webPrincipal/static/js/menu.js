export default function menu(panel,btn) {

    const $panel = document.querySelector(panel),
        $btn = document.querySelector(btn);

    document.addEventListener('click', (e) => {
        
        if (e.target.matches(btn) || e.target.matches(`${btn} *`)) {
            $btn.classList.toggle('is-active');
            $panel.classList.toggle('is-active');
        }

        if (e.target.matches(panel) || e.target.matches(`${panel} *`)) {
            $btn.classList.toggle('is-active');
            $panel.classList.toggle('is-active');
        }

    })
}