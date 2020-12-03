def call():
  import module

  obj = module.AddSub()
  
  print(obj.add(5,5))
  print(obj.sub(5,5))
   
  obj.display('edd')
call()
