def product(str: String):Long = {
  var pro = 1L
  if (str.length == 0) 0
  else if(str.length == 1) str.head * pro
  else product(str.head.toString) * product(str.tail)
}

product("Hello")
product("")
product("H")