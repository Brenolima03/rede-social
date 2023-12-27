const modalMenu = document.querySelector('#modalMenu');
const modalConta = document.querySelector('#modalConta');
const botaoAbrir = document.querySelector('#btn-menuModal');
const fechaModal = document.querySelector('#fechaModal');
const btnConta = document.querySelector('button#btnConta');

btnConta.addEventListener('click', () => {
  modalConta.showModal();
  document.querySelector('body').classList.add('overflow-hidden');
});

botaoAbrir.addEventListener("mouseenter", () => {
  modalMenu.classList.remove('w-0', 'overflow-x-hidden');
});

fechaModal.addEventListener('click', () => {
  modalMenu.classList.add('w-0', 'overflow-x-hidden');
  
});

modalConta.addEventListener('close', () => document.querySelector('body').classList.remove('overflow-hidden'))

botaoAbrir.addEventListener("mouseleave", () => {
  modalMenu.classList.add('w-0', 'overflow-x-hidden');
  modalMenu.classList.remove('p-3');
});

console.log(modalMenu);
console.log(botaoAbrir);

(function () {
    select_variacao = document.getElementById('select-variacoes');
    variation_preco = document.getElementById('variation-preco');
    variation_preco_promocional = document.getElementById('variation-preco-promocional');

    if (!select_variacao) {
        return;
    }

    if (!variation_preco) {
        return;
    }

    select_variacao.addEventListener('change', function () {
        preco = this.options[this.selectedIndex].getAttribute('data-preco');
        preco_promocional = this.options[this.selectedIndex].getAttribute('data-preco-promocional');


        if (preco && variation_preco) {
            variation_preco.innerHTML = preco;
        }
        
        if (variation_preco_promocional && preco_promocional) {
            variation_preco_promocional.innerHTML = preco_promocional;
        } else {
            variation_preco_promocional.innerHTML = preco;
            variation_preco.innerHTML = ''
        }

    })
})();