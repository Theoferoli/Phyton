pop_a = 80000
pop_b = 200000
anos = 0

while pop_a < pop_b:
    pop_a += pop_a * 0.03   # Cresce 3%
    pop_b += pop_b * 0.015  # Cresce 1.5%
    anos += 1

print(f"Serão necessários {anos} anos.")
