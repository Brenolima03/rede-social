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

// botaoAbrir.addEventListener("mouseleave", () => {
//   modalMenu.classList.add('w-0', 'overflow-x-hidden');
//   modalMenu.classList.remove('p-3');
// });

console.log(modalMenu);
console.log(botaoAbrir);


