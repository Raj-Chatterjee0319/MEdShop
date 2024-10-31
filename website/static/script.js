let cart = [];
let total = 0;

function addToCart(productName, productPrice) {
    cart.push({ name: productName, price: productPrice });
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = '';
    total = 0;

    cart.forEach(item => {
        const listItem = document.createElement('li');
        listItem.textContent = `${item.name} - $${item.price}`;
        cartItems.appendChild(listItem);
        total += item.price;
    });

    document.getElementById('total-price').textContent = `Total: $${total}`;
}

function placeOrder() {
    if (cart.length === 0) {
        alert('Your cart is empty!');
        return;
    }

    fetch("/placeorder")
    //alert('Order placed successfully!');
    cart = [];
    updateCart();
}
