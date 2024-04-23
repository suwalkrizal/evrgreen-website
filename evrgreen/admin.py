

# Register your models here.
from django.contrib import admin
from .models import CustomerProfile, MerchantProfile, Category, Product, Order, OrderItem, Cart, CartItem, Discount, Payment, Review

# Register your models here.
@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'address', 'phone_number')
    search_fields = ['first_name', 'last_name', 'email']
    list_per_page=5

@admin.register(MerchantProfile)
class MerchantProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'address', 'phone_number')
    search_fields = ['first_name', 'last_name', 'email']
    list_per_page=5
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', 'parent_category')
    search_fields = ['name']
    list_per_page=5

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'price', 'category', 'quantity_in_stock')
    search_fields = ['name', 'description']
    list_per_page=5

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_date', 'customer', 'total_amount', 'status')
    list_filter = ['status']
    search_fields = ['customer__first_name', 'customer__last_name', 'customer__email']
    list_per_page = 5

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_item_id', 'order', 'product', 'quantity', 'price')
    list_filter = ['order__status']
    search_fields = ['order__customer__first_name', 'order__customer__last_name', 'product__name']
    list_per_page = 5
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'customer', 'creation_date')
    list_filter = ['customer']
    search_fields = ['customer__first_name', 'customer__last_name', 'customer__email']
    list_per_page = 5

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_item_id', 'cart', 'product', 'quantity')
    list_filter = ['cart', 'product']
    search_fields = ['cart__customer__first_name', 'cart__customer__last_name', 'product__name']
    list_per_page = 5

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_id', 'code', 'amount', 'start_date', 'end_date')
    list_filter = ['start_date', 'end_date']
    search_fields = ['code']
    list_per_page = 5
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'customer', 'order', 'payment_date', 'amount', 'payment_method', 'transaction_id')
    list_filter = ['payment_date', 'payment_method']
    search_fields = ['customer__first_name', 'customer__last_name', 'order__order_id', 'transaction_id']
    list_per_page = 5

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'product', 'customer', 'rating', 'comment', 'review_date')
    list_filter = ['rating']
    search_fields = ['customer__first_name', 'customer__last_name', 'product__name', 'comment']
    list_per_page = 5
