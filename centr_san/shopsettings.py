__author__ = 'eri'

# shop config
SHOP_SHIPPING_BACKENDS = (
    'shop.shipping.backends.flat_rate.FlatRateShipping',
)

SHOP_PAYMENT_BACKENDS = (
    'shop.payment.backends.pay_on_delivery.PayOnDeliveryBackend',
    #'myshop.payment.ExamplePayment',
)

SHOP_SHIPPING_FLAT_RATE = "10.00"

SHOP_CART_MODIFIERS = [
    'shop.cart.modifiers.tax_modifiers.TenPercentGlobalTaxModifier',
    'shop.cart.modifiers.rebate_modifiers.BulkRebateModifier',
    ]

SHOP_PRODUCT_MODEL = 'myshop.models.SimpleProduct'

SHOP_CATEGORIES_CATEGORY_MODEL = 'myshop.models.category.Category'
