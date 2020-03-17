product = [
    ('car',1000),
    ('car1',2000),
    ('car2',3000)
]
saving = input('input your saving:');

if saving.isdigit():
    saving=int(saving);
print(saving)
print(product)
for i in product:
    print(product.index(i),i)