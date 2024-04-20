def main(): 
   menu = {
       "TACO TACO": 4.3, 
       "BURRITO": 4.56, 
       "BOWL": 8.95, 
       "NACHOS": 7.14
       }

   ordertotal = 0.0
   while True:
      try:
        item = input("ingrese un articulo de su pedido: ")
      except EOFError:
         break
      item = item.upper()
      if item in menu:
         ordertotal += menu[item] 
         print(f"${ordertotal:.2f}")
      elif item == "CONTROL -D" :
         print(f"El total de su pedido es ${ordertotal:.2f}")
         break
      else:
       print("Articulo invalido")
if __name__=="__main__":
    main()
