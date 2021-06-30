def fatorial(n):
	if n < 0:
		return 0
	i = fat = 1
	while i <= n:
		fat = fat * i
		i = i + 1
	return fat

def test_fatorial0():
	assert fatorial(0) == 1

def test_fatorial01():
	assert fatorial(1) == 1

def test_fatorial_negativo():
	assert fatorial(-10) == 0

def test_fatorial04():
	assert fatorial(4) == 24

def test_fatorial05():
	assert fatorial(5) == 120

# pytest considera que arquivos do tipo test_*.py e *_test.py
# são arquivos de teste

