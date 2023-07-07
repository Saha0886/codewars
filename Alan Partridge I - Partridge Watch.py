def part(arr):
  a=['Partridge','PearTree','Chat','Dan','Toblerone','Lynn','AlphaPapa','Nomad']
  d=0
  for i  in range(len(arr)):
    if arr[i] in a:
       d+=1
  if d==0:
    return( "Lynn, I've pierced my foot on a spike!!")
  else:
    return( "Mine's a Pint"+ "!"*d)
