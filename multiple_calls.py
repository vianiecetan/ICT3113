
def func_a():
  for i in range(0,1000):
    func_b()
    func_c()

def func_b():
  for i in range(0,17000):
    func_e()

def func_c():
  for i in range(0,15000):
    func_e()

def func_e():
  return

func_a()
