object Test{
    val str = (a:String) =>
      s"sum(case when order_dow='$a' then 1 else 0 end) as dow_$a"

    val array = (1 to 6)
    println(array.map(x=>str(x.toString)))

}
