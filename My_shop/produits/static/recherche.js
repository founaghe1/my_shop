document.addEventListener('DOMContentLoaded', function() {
    let categorySelect = document.getElementById('category-select');
    if (categorySelect) {
        categorySelect.addEventListener('change', function() {
            this.form.submit();
        });
    }
});
