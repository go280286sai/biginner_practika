SELECT product_id, product_title, product_description, in_stock, price*2 AS price, slug, category_id
	FROM public.products;