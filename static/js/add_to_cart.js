document.addEventListener("DOMContentLoaded", function() {

    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartCount = document.getElementById('cart-count');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();

            const productId = this.dataset.id;
            const url = `/cart/ajax/add/${productId}/`;

            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if(data.success){
                        alert('Product added to cart!');
                        cartCount.textContent = data.total_items;
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });

});




document.addEventListener("DOMContentLoaded", function() {

    const cartCount = document.getElementById('cart-count');

    function updateCart(url) {
        fetch(url)
        .then(res => res.json())
        .then(data => {
            if(data.success){
                // تحديث العدد
                cartCount.textContent = data.total_items;

                // تحديث قيمة كل منتج
                if(data.item_total && data.item_id){
                    const el = document.getElementById('item-total-' + data.item_id);
                    if(el) el.textContent = data.item_total;
                }

                // إعادة تحميل الصفحة إذا السلة فاضية
                if(data.empty){
                    window.location.reload();
                }
            }
        });
    }

    document.querySelectorAll('.increase').forEach(btn => {
        btn.addEventListener('click', () => {
            const id = btn.dataset.id;
            updateCart(`/cart/ajax/increase/${id}/`);
        });
    });

    document.querySelectorAll('.decrease').forEach(btn => {
        btn.addEventListener('click', () => {
            const id = btn.dataset.id;
            updateCart(`/cart/ajax/decrease/${id}/`);
        });
    });

    document.querySelectorAll('.remove').forEach(btn => {
        btn.addEventListener('click', () => {
            const id = btn.dataset.id;
            updateCart(`/cart/ajax/remove/${id}/`);
        });
    });

});
