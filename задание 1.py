class Car:
 pass
 class Car:
  color1 = None # цвет автомобиля
  fuel1 = None #количество топлива
  wheels1 = None #количество колес 
  classification1 = None #классификация/вид
 def go(self):
  # Команда ехать:
  pass
	
 def turn(self):
  # Команда поворачивать:
  pass

 def stop(self):
 # Команда остановиться:
  pass
myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.wheels = 4 # добавляем колеса
myCar.classification = 'sports'# определяем вид 
myCar.go() 
myCar.turn() 
myCar.stop() 
print(myCar.color, myCar.fuel, myCar.wheels, myCar.classification)

class Car:
  color1 = None # цвет автомобиля
  fuel1 = None #количество топлива
  wheels1 = None #количество колес 
  classification1 = None #классификация/вид
  def go(self):
  # Команда ехать:
    pass
	
  def turn(self):
  # Команда поворачивать:
    pass

  def stop(self):
 # Команда остановиться:
   pass
myCar1 = Car()
myCar.color1 = 'pink'  # красим в розовый цвет
myCar.fuel1 = 60    # заливаем топливо
myCar.wheels1 = 4 # добавляем колеса
myCar.classification1 = 'ordinary'# определяем вид 
myCar.go() 
myCar.turn() 
myCar.stop() 
print(myCar.color1, myCar.fuel1, myCar.wheels1, myCar.classification1)
