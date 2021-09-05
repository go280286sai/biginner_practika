select DISTINCT(order_id), created_at, status_name from public.users inner join public.carts on public.users.user_id=users_user_id inner join public."'Order'"
on public."'Order'".carts_cart_id=public.carts.carts_id inner join public.order_status on public.order_status.order_status_id=public."'Order'".order_status_order_status_id
inner join public.cart_product on public.cart_product.carts_cart_id=public.carts.carts_id inner join public.products
on public.cart_product.products_product_id=public.products.product_id inner join public.categories on
public.categories.category_id=public.products.category_id WHERE created_at<='2020-12-31' AND status_name='In progress' or status_name='Paid'