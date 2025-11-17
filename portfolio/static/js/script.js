/**
 * Inicializa o comportamento do portfólio.
 * Gerencia a animação de texto digitando e o efeito de fade-in ao rolar (scroll).
 */
function initPortolio() {
    
    const typedText = document.getElementById("typed-text");
    if (!typedText) return;

    // --- 1. Animação de Texto Digitando (agora dinâmica) ---
    // Busca o texto do atributo de dados injetado pelo template Django
    const text = typedText.getAttribute("data-typed-text"); 
    let index = 0;
    
    /**
     * Implementa o efeito de digitação de texto.
     */
    function typeEffect() {
        if (!typedText || !text) return; 
        
        try {
            if (index < text.length) {
                typedText.textContent += text.charAt(index);
                index++;
                setTimeout(typeEffect, 150); 
            }
        } catch (error) {
            console.error("Erro na animação de digitação:", error);
            typedText.textContent = text; 
        }
    }

    // --- 2. Efeito de Fade-in ao Rolar (Scroll) ---
    const scrollObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("opacity-100", "translate-y-0");
                scrollObserver.unobserve(entry.target); 
            }
        });
    }, { 
        threshold: 0.2 
    });

    /** @type {NodeListOf<HTMLElement>} */
    const elementsToObserve = document.querySelectorAll("section, .project-card");

    elementsToObserve.forEach(el => {
        el.classList.add("opacity-0", "translate-y-4", "transition", "duration-700");
        scrollObserver.observe(el);
    });

    // Inicia a função principal do portfólio
    typeEffect();
}

document.addEventListener("DOMContentLoaded", initPortolio);