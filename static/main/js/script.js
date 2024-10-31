var currentPage = 1;
var booksPerPage = 6;
var totalBooks = cardsCount;
var cardsCount = document.currentScript.getAttribute('data-cards-count');
var totalPages = Math.ceil(totalBooks / booksPerPage);

function showPage(page, direction) {
    var startIndex = (page - 1) * booksPerPage;
    var endIndex = startIndex + booksPerPage;
    var cards = document.querySelectorAll('.card-book');

    cards.forEach(function(card, index) {
        if (index >= startIndex && index < endIndex) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });

    // Добавим небольшую задержку перед добавлением/удалением классов, чтобы анимация сработала
    setTimeout(function() {
        cards.forEach(function(card, index) {
            if (index >= startIndex && index < endIndex) {
                card.classList.remove('card-book-hidden');

                // При нажатии вперед или назад устанавливаем разные классы анимации
                if (direction === 'next') {
                    card.classList.remove('animate-prev');
                    card.classList.add('animate-next');
                } else if (direction === 'prev') {
                    card.classList.remove('animate-next');
                    card.classList.add('animate-prev');
                }
            } else {
                card.classList.add('card-book-hidden');
            }
        });
    }, 100);
}

function nextPage() {
    if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage, 'next');
    }
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        showPage(currentPage, 'prev');
    }
}

// Показать первую страницу при загрузке страницы
showPage(currentPage, 'next');