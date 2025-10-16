// Aguarda o HTML ser completamente carregado para executar o script
document.addEventListener('DOMContentLoaded', function() {

    // Pega os elementos do HTML
    const botao = document.getElementById("meuBotao");
    const dropdown = document.getElementById("meuDropdown");

    // Adiciona o evento de clique AO BOTÃO
    botao.addEventListener("click", function(event) {
        // Alterna a classe 'mostrar' para abrir/fechar o menu
        dropdown.classList.toggle("mostrar");

        // *** A CORREÇÃO ESTÁ AQUI ***
        // Impede que o evento de clique "borbulhe" para o window,
        // o que fecharia o menu imediatamente.
        event.stopPropagation();
    });

    // Adiciona o evento de clique À JANELA INTEIRA para fechar o menu
    window.addEventListener("click", function(event) {
        // Se o menu estiver aberto (contém a classe 'mostrar')
        if (dropdown.classList.contains('mostrar')) {
            // Fecha o menu
            dropdown.classList.remove('mostrar');
        }
    });
});