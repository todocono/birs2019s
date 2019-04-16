from turtle import *

color('red', 'yellow')
begin_fill()
while True:
  forward(400)
  left(200)
  if abs(pos()) < 1:
    break
end_fill()
done()
