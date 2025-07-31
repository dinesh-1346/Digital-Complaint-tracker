from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def view_cart(request):
    """
    This view renders the cart contents page
    """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    messages.success(request, 'You have successfully added this item to your shopping cart.')
    return redirect('view_issue', id)
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified Issue to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


'''
<!-- Reference: 
Author: CodeInstitute (2019).
Title: "Putting It All Togther: Ecommerce".
Version: Unknown.
Type: HTML, CSS, Python, Jinja, sqlite3, postgres.
Retrieved from: https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/tree/master/03-HostingYourEcommerceWebApp/06-travis_continuous_integration
-->
'''