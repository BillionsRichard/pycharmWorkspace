class ConstructorDemo {
  var a:Int = 0
  println("constructor study..")

  def this(a1:Int) = {
    this()
    this.a = a1
  }
}

object ConstructorDemoTest{
  def main(args: Array[String]): Unit = {
    val obj:ConstructorDemo = new ConstructorDemo(100)
    print(obj.a)
  }
}
