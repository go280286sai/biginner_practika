ALTER TABLE public.users ADD COLUMN phone_number INT;
ALTER TABLE public.users ALTER COLUMN phone_number SET DATA TYPE VARCHAR(50);
