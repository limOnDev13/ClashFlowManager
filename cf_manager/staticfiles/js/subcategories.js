// 1. Ждём загрузки страницы
document.addEventListener('DOMContentLoaded', function() {

    // 2. Находим нужные элементы на странице
    const categorySelect = document.getElementById('id_category');
    const subcategorySelect = document.getElementById('id_subcategory');

    // 3. Проверяем, что элементы существуют
    if (!categorySelect || !subcategorySelect) return;

    // 4. Функция для обновления списка подкатегорий
    function updateSubcategories() {
        // Получаем выбранную категорию
        const categoryId = categorySelect.value;

        // Формируем URL запроса
        const url = categoryId
            ? `/reference_books/api/subcategories/?category_id=${categoryId}`
            : '/reference_books/api/subcategories/';

        console.log('Make request to Subcategory API:', url);

        // Делаем запрос к API
        fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log('Received data:', data);
                const subcategories = data.results || [];

                // Очищаем текущий список
                subcategorySelect.innerHTML = '';

                // Добавляем варианты подкатегорий
                subcategories.forEach(item => {
                    const option = document.createElement('option');
                    option.value = item.id;
                    option.textContent = item.name;
                    subcategorySelect.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

    // 5. Вешаем обработчик на изменение категории
    categorySelect.addEventListener('change', updateSubcategories);

    // 6. Вызываем сразу при загрузке
    updateSubcategories();
});